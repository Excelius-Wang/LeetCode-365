from typing import OrderedDict

class HandLRUCache:
    def __init__(Self, capacity: int):
        

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 将 key 移到末尾（表示最近使用）
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新值并移到末尾
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) == self.cap:
            # popitem(last=False) 弹出最老（OrderedDict 头部）
            self.cache.popitem(last=False)

        self.cache[key] = value  # 新插入放在末尾
