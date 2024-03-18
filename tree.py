
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
