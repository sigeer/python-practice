# 全角字符转半角字符
import unicodedata
import sys

def convert_to_halfwidth(text: str) -> str:
    result = ''
    for char in text:
        halfwidth_char = unicodedata.normalize('NFKC', char)
        result += halfwidth_char
    return result

if __name__ == "__main__":
    print(convert_to_halfwidth(sys.argv[1]))