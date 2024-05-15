from loguru import logger
import os
import time


# 日志存放目录
log_foldir = os.path.expanduser("logs")

# 如果目录不存在则创建
if not os.path.exists(log_foldir):
    os.mkdir(log_foldir)

# 日志名称
log_filename = os.path.join(log_foldir, "loguru_{time}.log")

# 日志配置
logger.add(
    sink=log_filename,  # 输出位置
    # format="{time:YYYY-MM-DD at HH:mm:ss} - {level} - {message}",  # 格式化
    level="INFO",  # 只记录设定值及以上级别的日志
    rotation="500 KB",  # 回滚策略  time | size | system | when
    compression="zip",  # 压缩 zip | tar | tgz | bz2
    # filter= my_filter,    # 过滤 可以是一个函数
    colorize=True,  # 日志颜色 默认False
    enqueue=False,  # 队列
    backtrace=True,  # 异常 追溯信息
    retention="30 days",  # 保留文件的策略 与rotation类似使用方法
)
for _ in range(500):
    logger.info("this is a info log")
    logger.debug("this is a debug log")
    logger.warning("this is a warning log")
    logger.error("this is a error log")
    logger.critical("this is a critical log")
