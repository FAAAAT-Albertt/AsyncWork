# асинхронный парсинг
import asyncio
import aiohttp
from bs4 import BeautifulSoup



headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

async def page_parce(session, page): # работа одной задачи

    url = f"https://com-x.life/comix-read/marvel-read/page/{str(page)}"
    async with session.get(url=url, headers=headers) as response:

        StoryName = []

        soup = BeautifulSoup(await response.text(), 'lxml')
        names = soup.find("div", class_="content-masonry").find_all("article")

        for name in names:
            try:
                name = name.find("div", class_="article-inf").find("a", class_="title").text
                StoryName.append(f"{name.strip()}_{page}")
            except:
                continue

    print("[INFO] ONE MORE PAGE SUCCESS")


async def work_gather(): # список задач
    tasks = []
    url = "https://com-x.life/comix-read/marvel-read"
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        i = soup.text
    pag_block = soup.find("div", class_="wrapper")
    PageEnd = pag_block[2].text

    for page in range(1, int(PageEnd)+1):
        task = asyncio.create_task(page_parce(session, page))
        tasks.append(task)

    await asyncio.gather(*tasks)

    pass


async def main():
    await work_gather()



if __name__ == '__main__':
    asyncio.run(main())