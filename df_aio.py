import os

from Adafruit_IO import Client, Feed, Data
from Adafruit_IO.errors import RequestError

class DFAIO:
    def __init__(self):
        self._username = os.getenv('IO_USERNAME')
        self._api_key = os.getenv('IO_KEY')

        if not self._username:
            raise MissingEnvVar('IO_USERNAME is not set')
        if not self._api_key:
            raise MissingEnvVar('IO_KEY is not set')

        print('connecting to adafruit IO')
        self.aio = Client(self._username, self._api_key)

        self.feeds = {}

    def get_or_create_feed(self, feedname: str) -> Feed:
        print(f'getting feed {feedname}')
        try:
            feed = self.aio.feeds(feedname)
        except RequestError:
            feed = Feed(name=feedname)
            self.aio.create_feed(feed)

        self.feeds[feedname] = feed
        return feed

    def post(self, feedname:str, value:int) -> None:
        self.aio.send_data(self.feeds[feedname].key, value)
