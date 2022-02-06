import logging
from time import  strftime, localtime,time

date = strftime('%Y-%m-%d', localtime(time()))
my_format = '%(asctime)s-%(filename)s-%(lineno)d'
#设置打印级别
logging.basicConfig(
    level=logging.INFO,
    filename='../../logs/'+ date+'testlogs.log',
    format= my_format
)

logging.info('info')
logging.debug('debug')
logging.warning('warning')
logging.error('error')
logging.critical('critical')