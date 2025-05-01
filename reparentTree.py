from typing import List
@dataclass
class Tree():
    root: _Node
    def reParent(self, root):
        newTree=_Node(root)
        currentNode=

    def getNode(self,target):
        currentNode=self.root
        stack=currentNode.children
        while stack!=[]
            currentNode=stack.pop()
            stack+=currentNode.children
            if currentNode.name==target:
                return currentNode
        raise NotFoundError("requested node could not be found.")

@dataclass    
class _Node():
    name:str
    children: List[_Node] =[]
