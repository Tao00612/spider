import asyncio


async def request(url):
    print('正在请求', url)
    print('请求成功', url)
    return url

# async 修饰的函数,调用之后返回的是一个协程对象
c = request('baidu')

# 创建一个事件循坏对象
# loop = asyncio.get_event_loop()

# 将协程对象注册到loop中,然后启动loop
# loop.run_until_complete(c)

# task的使用
# loop = asyncio.get_event_loop()
# 基于loop创建一个task对象
# task = loop.create_task(c)
# 将协程对象注册到loop中,然后启动loop
# print(task)
# loop.run_until_complete(task)
# print(task)


# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def call_back(task):
    # result() 可以返回协程对象的一个返回值
    print(task.result())


# 回调绑定
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将会调函数 绑定到任务对象中
task.add_done_callback(call_back)
loop.run_until_complete(task)