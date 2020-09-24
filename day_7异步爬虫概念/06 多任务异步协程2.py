import requests
import asyncio
import time
urls = [
    'https://www.baidu.com/',
    'https://www.bilibili.com/',
    'https://www.j8dy.org/'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
async def get_page(url):
    print('正在请求',url)
    # request.get 是基于同步的，必须使用异步的网络请求模块进行请求
    # aiohttp: 基于异步网络请求
    response = requests.get(url=url,headers=headers)
    print('下载完毕',response.status_code)
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
# 需要将任务列表封装在wait中
loop.run_until_complete(asyncio.wait(tasks))


