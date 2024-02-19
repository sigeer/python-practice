import os 

# 获取当前执行文件所在目录
current_file_dir = os.path.dirname(os.path.abspath(__file__))
print("当前执行文件所在目录: ", current_file_dir)

file_path = __file__
print(f"origin: {file_path}")

base_name = os.path.basename(file_path)
print(f"file_path + basename {base_name}")

# splitext以小数点（最后一个）分割
print(f"file_path + splitext  {os.path.splitext(file_path)}")
# split以斜杠（最后一个）分割
print(f"file_path + split  {os.path.split(file_path)}")

print(f"base_name + splitext  {os.path.splitext(base_name)}")

print(f"base_name + split  {os.path.split(base_name)}")

# 目录不存在，或者不是目录而是文件也是false
print(f"file_path + isdir {os.path.isdir(file_path)}")

print(f"file_path + listdir 非目录会抛出异常")

print(f"os.path.abspath('./') 返回绝对路径 {os.path.abspath('./')} ")

print(f"__file__ 当前文件路径 {__file__}")

print(f"os.getcwd() 当前工作目录 {os.getcwd()}")
