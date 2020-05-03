
import requests


class AmyError(Exception):
    def __init__(self, text):
        self.__text = text



class Product:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class SpecialOfferCatalog():

    __headers = {
        'User-agent': 'Opera'
    }

    def __init__(self, url: str):
        self.__url = url
        self.__products = []
        self.__parse()

    def __parse(self):
        url = self.__url
        while url:
            response = requests.get(url, headers=self.__headers)
            data = response.json()
            url = data['next']
            self.__products.extend(data['results'])

    def __iter__(self):
        return self.__products.__iter__()


class MyTemp:

    __tmp = 0

    @staticmethod
    def func1():
        return 222


    @classmethod
    def cls_func(cls):
        return cls.__tmp


if __name__ == "__main__":

    print(MyTemp.func1())

    # url = 'https://5ka.ru/api/v2/special_offers'
    # catalog = SpecialOfferCatalog(url)
    #
    # for itm in catalog:
    #     print(itm)
    #     print(1)
