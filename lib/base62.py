class Base62:
    TARGET = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    TARGET_LENGTH = len(TARGET)

    @classmethod
    def encode(cls, num):
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
        num = 0
        code_list = list(code)
        for index, code in enumerate(reversed(code_list)):
            num += cls.TARGET.index(code) * cls.TARGET_LENGTH ** index
        return num
