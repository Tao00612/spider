import time
# 导入线程池
from multiprocessing.dummy import Pool
# urls = [
#     'https://www.mjw2020.com/alltop_hit',
#     'https://www.j8dy.org/',
#     'https://www.bilibili.com/video/BV18C4y1a7uk?p=42'
# ]
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
# }

t1 = time.time()


def get_page(data):
    print('正在下载', data)
    time.sleep(2)
    print('下载成功', data)


list_l = ['11', '22', 'aa', 'bb']

# 实例化一个线程池对象
pool = Pool(4)
# 列表中每一个列表元素传递给get_page进行处理.
pool.map(get_page, list_l)
# get_page有返回值 这个map就有一个返回值 执行回调函数

print(f'耗时{time.time() - t1}')
