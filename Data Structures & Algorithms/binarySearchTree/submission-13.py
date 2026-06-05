class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.root == None:
            self.root = newNode
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return


    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.getMinHelper(self.root)
        if cur:
            return cur.val
        else:
            return -1

    def getMinHelper(self, node: Node):
        while node and node.left:
            node = node.left
        return node
        
    def getMax(self) -> int:
        cur = self.getMaxHelper(self.root)
        if cur:
            return cur.val
        else:
            return -1

    def getMaxHelper(self, node: Node):
        while node and node.right:
            node = node.right
        return node


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(key, self.root)
    
    def removeHelper(self, key: int, cur: Node) -> Node:
        if cur == None:
            return None
        if key < cur.key:
            cur.left = self.removeHelper(key, cur.left)
        elif key > cur.key:
            cur.right = self.removeHelper(key, cur.right)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:
                minNode = self.getMinHelper(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.key, minNode)
        return cur


    def getInorderKeys(self) -> List[int]:
        result = []
        self.getInorderKeysHelper(self.root, result)
        return result
    
    def getInorderKeysHelper(self, node: Node, result: List[int]):
        if node == None:
            return
        self.getInorderKeysHelper(node.left, result)
        result.append(node.key)
        self.getInorderKeysHelper(node.right, result)


