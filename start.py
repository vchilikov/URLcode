import asyncio
from url_code.settings import *
from url_code.url_task import URLTask


def url_list_from_file(path=URLS_FILE):
    with open(path, 'r') as f:
        for url in f:
            yield url.strip()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [URLTask(url).url_code() for url in url_list_from_file()]
    asyncio.ensure_future(asyncio.wait(tasks))
    try:
        loop.run_forever()
    finally:
        loop.close()
