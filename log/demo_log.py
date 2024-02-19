import logging
from logging.handlers import RotatingFileHandler
import datetime

def get_log_filename(log_type):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f'{current_date}-{log_type}.log'
    return filename

# 配置日志记录
# logging.basicConfig(level=logging.INFO, handlers=[
#     logging.FileHandler('app.log', mode='w', encoding="utf-8")
# ])
logger = logging.getLogger('')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# 创建 RotatingFileHandler 处理程序
info_handler = RotatingFileHandler(get_log_filename('Info'), encoding="utf-8", maxBytes=20*1024*1024, backupCount=10)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = RotatingFileHandler(get_log_filename('Error'), encoding="utf-8", maxBytes=20*1024*1024, backupCount=10)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 将处理程序添加到日志记录器
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug('这是一个调试信息')
logger.info('这是一个普通信息')
logger.warning('这是一个警告信息')
logger.error('这是一个错误信息')
