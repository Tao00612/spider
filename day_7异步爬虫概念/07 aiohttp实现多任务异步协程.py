import asyncio
import aiohttp

# 使用该模块的ClientSession
urls = [
    'https://www.baidu.com/',
    'https://www.bilibili.com/',
    'https://www.j8dy.org/'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get() post()  headers params/data  proxy="ip:端口" 代理ip
        async with await session.get(url, headers=headers) as response:
            # text() 返回字符串形式的响应数据
            # read() 返回二进制的数据
            # json() 返回json对象
            # 注意： 获取响应数据操作之前一定要使用过await 进行手动挂起
            page_text = await response.text()
            print(page_text)
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
# 需要将任务列表封装在wait中
loop.run_until_complete(asyncio.wait(tasks))
