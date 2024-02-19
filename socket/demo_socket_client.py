import socket
import threading

# 创建 TCP 客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 服务器地址和端口号
server_address = ('localhost', 8025)

# 连接服务器
client_socket.connect(server_address)
print('已连接到服务器！')

# 发送消息线程
def send_message():
    while True:
        message = input('请输入消息：')
        client_socket.sendall(message.encode())

# 接收消息线程
def receive_message():
    while True:
        data = client_socket.recv(1024)
        print(f'{data.decode()}')

# 启动发送消息线程和接收消息线程
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
