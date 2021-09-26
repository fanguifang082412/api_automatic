import logging
import logging.handlers
import os
import sys
sys.path.append(r"C:/Users/Administrator/PycharmProjects/api_automatic")
sys.path.append(r"C:\Users\Administrator\PycharmProjects\api_automatic\venv\Lib\site-packages")
import time


def logging_config():
    #实例化日志器
    logger = logging.getLogger()
    #设置日志级别
    logger.setLevel(logging.DEBUG)

    # 设置日志打印格式
    fmt = '%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s'
    formatter = logging.Formatter(fmt)

    #实例化输出到控制台的处理器
    handler01 = logging.StreamHandler()
    handler01.setFormatter(formatter)

    #实例化输出到文件的处理器
    logging_path = os.path.abspath("..")+"/log/everyday_log_"
    logging_str = time.strftime("%Y_%m_%d", time.localtime())
    handler02 = logging.handlers.TimedRotatingFileHandler(filename=logging_path+logging_str+".log", when="D", interval=1, backupCount=7)
    handler02.setFormatter(formatter)

    #将处理器添加到日志器中
    logger.addHandler(handler01)
    logger.addHandler(handler02)
