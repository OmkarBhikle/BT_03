from typing import List
import hashlib

class Node:
    def __init__(self, left: 'Node', right: 'Node', value: str) -> None:
        self.left = left
        self.right = right
        self.value = value

    @staticmethod
    def hash(val: str) -> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    @staticmethod
    def doubleHash(val: str) -> str:
        return Node.hash(Node.hash(val))

class MerkleTree:
    def __init__(self, values: List[str]) -> None:
        self.buildTree(values)

    def buildTree(self, values: List[str]) -> None:
        leaves: List[Node] = [Node(None, None, Node.doubleHash(e)) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1])  # Duplicate last element if odd number of elements
        self.root: Node = self.buildTreeRec(leaves)

    def buildTreeRec(self, nodes: List[Node]) -> Node:
        half: int = len(nodes) // 2
        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.doubleHash(nodes[0].value + nodes[1].value))
        left: Node = self.buildTreeRec(nodes[:half])
        right: Node = self.buildTreeRec(nodes[half:])
        value: str = Node.doubleHash(left.value + right.value)
        return Node(left, right, value)

    def printTree(self) -> None:
        self.printTreeRec(self.root)

    def printTreeRec(self, node: Node) -> None:
        if node is not None:
            print("Node:", node.value)
            self.printTreeRec(node.left)
            self.printTreeRec(node.right)

    def getRootHash(self) -> str:
        return self.root.value

def test() -> None:
    n = int(input("Enter number of elements: "))
    elems = []
    for _ in range(n):
        elems.append(input("Enter element: "))
    tree = MerkleTree(elems)
    print("Root hash:", tree.getRootHash())
    tree.printTree()

if __name__ == "__main__":
    test()