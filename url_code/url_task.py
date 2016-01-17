import asyncio
import aiohttp
from url_code.settings import *


class URLTask:
    def __init__(self, url):
        self.url = url
        self.sleep = SLEEP_NORMAL

    def __request_log(self, status):
        print(self.url, status)

    def __request_sleep_inc(self):
        self.sleep = int(self.sleep * SLEEP_STEEP)
        if self.sleep > SLEEP_MAX:
            self.sleep = SLEEP_MAX
        elif self.sleep < SLEEP_MIN:
            self.sleep = SLEEP_MIN

    async def url_code(self):
        while True:
            await asyncio.sleep(self.sleep)
            try:
                async with aiohttp.head(self.url) as head:
                    if head.status not in STATUS_OK:
                        self.__request_log(head.status)
                        self.__request_sleep_inc()
                    else:
                        self.sleep = SLEEP_NORMAL
            except aiohttp.errors.ClientOSError as e:
                self.__request_log(e)
                self.__request_sleep_inc()
