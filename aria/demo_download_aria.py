import subprocess
import sys
import os

def is_null_or_empty(string):
    return string is None or len(string) == 0

def download(url: str, path: str):
    if is_null_or_empty(url):
        raise Exception("url 不能为空")
    
    if is_null_or_empty(path):
        path = os.getcwd()
        
    command = rf'./aria2c.exe -d "{path}" "{url}" --check-certificate=false'
    print(command)
    subprocess.run(command)
    
download("https://pic.cnblogs.com/avatar/1168700/20230619202616.png", r'./')

# class ConsoleOption:
#     url: str = None
#     path: str = None


# if __name__ == '__main__':
#     args = sys.argv[1:]
#     option = ConsoleOption()
#     for p in args:
#         if p.startswith('--url='):
#             option.url = p[6:]
#         if p.startswith('--path='):
#             option.path = p[7:]

#     download(option.url, option.path)