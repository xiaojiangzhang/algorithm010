# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在
# 写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
# 
#  
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计 
#  👍 772 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class DataNode():
    def __init__(self, key=0, value=0):
        self.val = value
        self.key = key
        self.preNode = None
        self.nextNode = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = DataNode()
        self.tail = DataNode()
        self.head.nextNode = self.tail
        self.tail.preNode = self.head
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # check key is in cache ?
        if key not in self.cache:
            return -1
        # else get node.val from cache
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key not in cache
        if key not in self.cache:
            node = DataNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        # else key is in cache
        else:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.preNode = self.head
        node.nextNode = self.head.nextNode
        self.head.nextNode.preNode = node
        self.head.nextNode = node

    def remove_Node(self, node):
        node.preNode.nextNode = node.nextNode
        node.nextNode.preNode = node.preNode

    def remove_tail(self):
        node = self.tail.preNode
        self.remove_Node(node)
        return node

    def move_to_head(self, node):
        self.remove_Node(node)
        self.add_to_head(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
