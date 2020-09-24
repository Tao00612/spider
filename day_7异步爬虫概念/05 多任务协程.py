import asyncio
import time


async def request(url):
    print('正在下载', url)
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载成功', url)
    return url


def call_back(task):
    print(task.result())


t1 = time.time()
urls = [
    'www.baidu.com',
    'www.soguo.com',
    'www.duobanjia.com',
]
# 任务列表
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装在wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time() - t1)
