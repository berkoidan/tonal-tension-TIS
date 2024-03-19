
class HierarchicalTree:
   def __init__(self, value):
      self.children = []
      self.value = value
      self.parent = None
      self.chord = None
   
   def setChord(self, chord):      
      self.chord = chord
   
   def addnode(self, value):
      newnode = HierarchicalTree(value)
      self.children.append(newnode)
      newnode.parent = self
      return newnode
   
   def addsubtree(self, child):
      self.children.append(child)
      child.parent = self
      return self
   
   def addsubtrees(self, child1, child2):
      self.children.append(child1)
      self.children.append(child2)
      child1.parent = self
      child2.parent = self
      return self
    
   def __str__(self):
      if not self.children:
         return f'{self.value} / {self.chord}'
      childrenStr = ' | '.join(map(str, self.children))
      return f'({self.value} / {self.chord} -> [{childrenStr}])'
   
   def cloneTree(self):
      newTree = HierarchicalTree(self.value)
      newTree.chord = self.chord
      for child in self.children:
         newTree.addnode(child.cloneTree())
      return newTree
   
   def isLeaf(self):
      return False if self.children else True
   
   def randomLeaf(self):
      import random
      if not self.children:
         return self
      
      return random.choice(self.children).randomLeaf()
   
   def leaves(self):
      if not self.children:
         yield self
         return
      
      for child in self.children:
         for node in child.leaves():
            yield node

   def dfs(self):
      yield self
      for child in self.children:
         for node in child.dfs():
            yield node
            
