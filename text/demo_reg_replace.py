# 字符串替换
import sys
import os
import re

pattern = ".*"

def remove_by_pattern(pattern: str, text_path: str):
    with open(text_path, "r", encoding="utf-8") as fs:
        text = fs.read()
    
    file_path_arr = os.path.splitext(text_path)
    text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    with open(file_path_arr[0] +"_d" + file_path_arr[1], "w", encoding="utf-8") as f:
        f.write(text)

# 判断是否二进制文件
def is_binary_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            # 读取前面的一些字节来判断文件类型
            content = f.read(1024)
            # 使用简单的二进制字符检查
            is_binary = b'\x00' in content
            return is_binary
    except Exception as e:
        print(f"Error checking binary: {e}")
        return False
    
def find_txt_files(directory):
    txt_files = []
    dirs = os.listdir(directory)
    for d in dirs:
        dir = os.path.join(directory, d)
        if os.path.isdir(dir):
            txt_files.extend(find_txt_files(dir))
        elif dir.lower().endswith(".txt"):
            txt_files.append(dir)
    return txt_files


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("file_path required")
        exit()
    path = sys.argv[1]
    if path is None or len(path.strip()) == 0:
        print("file_path required")
        exit()
    
    if not os.path.exists(path):
        print("file_path not existed")
        exit()
    
    files = []
    if os.path.isdir(path):
        files = find_txt_files(path)        
    elif path.lower().endswith(".txt"):
        files.append(path)

    for file in files:
        remove_by_pattern(pattern, file)