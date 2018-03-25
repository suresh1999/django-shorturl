from django.utils.crypto import get_random_string

from .models import ShortUrl
class LongUrlException(Exception):

    def __init__(self, msg=''):
        self.msg = msg

class Short(object):

    def __init__(self, long_url, length=6):
        self.__length = length
        self.__long_url = long_url
        self.__short_url = ''

    def generate(self):
        if ShortUrl.objects.filter(long_url=self.__long_url).count() > 0:
            raise LongUrlException
        while True:
            short_url = get_random_string(length=self.__length)
            try:
                obj = ShortUrl.objects.get(short_url=short_url)
            except ShortUrl.DoesNotExist:
                self.__short_url = short_url
                break
        ShortUrl.objects.create(short_url=self.__short_url, long_url=self.__long_url)
        return self.__short_url

    @staticmethod
    def get_longurl(shorturl):
        try:
            obj = ShortUrl.objects.get(short_url=shorturl)
        except ShortUrl.DoesNotExist:
            raise LongUrlException(msg='Long url is not available for this ShortUrl')
        else:
            return obj.long_url

