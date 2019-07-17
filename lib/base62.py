import re

class Base62:
    TARGET = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    TARGET_LENGTH = len(TARGET)

    @classmethod
    def encode(cls, num):
        if type(num) != int:
            raise TypeError('[num] must be int type')

        result = []
        if num == 0:
            result.append(cls.TARGET[0])
        while num > 0:
            result.append(cls.TARGET[num % cls.TARGET_LENGTH])
            num //= cls.TARGET_LENGTH
        result = ''.join(reversed(result))
        return result

    @classmethod
    def decode(cls, code):
        if type(code) != str:
            raise TypeError('[code] must be string type')

        regex = re.compile('^[0-9a-zA-Z]+$')
        if not regex.match(code):
            raise ValueError('[code] must be consist of number and alphabet')

        num = 0
        code_list = list(code)
        for index, code in enumerate(reversed(code_list)):
            num += cls.TARGET.index(code) * cls.TARGET_LENGTH ** index
        return num
