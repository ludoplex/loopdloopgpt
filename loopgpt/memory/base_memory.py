from typing import *


class BaseMemory:
    def add(self, key: Optional[str] = None):
        raise NotImplementedError()

    def get(self, k: int) -> List[str]:
        raise NotImplementedError()

    def config(self):
        return {"class": self.__class__.__name__, "type": "memory"}

    @classmethod
    def from_config(cls, config):
        raise cls()

    def clear(self):
        raise NotImplementedError()
