import random
import re

import pytest

from lib.base62 import Base62



class TestBase62:
    def test_base62_encode(self):
        number = random.randrange(10000000)
        encoded = Base62.encode(number)
        regex = re.compile('^[0-9a-zA-Z]+$')
        assert regex.match(encoded) is not None

    def test_base62_encode_vaildate(self):
        with pytest.raises(TypeError):
            payload = 'input must be int type'
            Base62.encode(payload)

    def test_base62_decode(self):
        encoded = '1A2B3C'
        expect = 1448700036
        decoded = Base62.decode(encoded)
        assert decoded == expect

    def test_base62_decode_vaildate(self):
        with pytest.raises(TypeError):
            payload = random.randrange(10000000)
            Base62.decode(payload)
        with pytest.raises(ValueError):
            payload = 'onlyAlphabetAndNumber!!!'
            Base62.decode(payload)