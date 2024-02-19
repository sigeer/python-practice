import socket

# 创建 TCP 服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 IP 地址和端口号
server_address = ('localhost', 8025)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(1)
print('等待客户端连接...')

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f'客户端 {client_address} 连接成功！')

    while True:
        # 接收数据
        data = client_socket.recv(1024)
        recv_str = data.decode()
        if recv_str == 'exit()':
            # 关闭连接
            client_socket.close()
            print("连接已关闭")
            break
        else:
            print(f'收到客户端消息：{data.decode()}')

            # 发送响应数据
            response = 'Hello from the server!'
            client_socket.sendall(response.encode())



# 关闭服务器套接字
server_socket.close()
