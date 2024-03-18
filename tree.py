
class Tree:
   def __init__(self, value):
      self.children = []
      self.value = value
   
   def addnode(self, value):
      newnode = Tree(value)
      self.children.append(newnode)
      return newnode
    
   def toString(self):
      if(not self.children):
         return str(self.value)
      childrenStr = '|'.join(map(lambda t: f'({t.toString()})', self.children))
      return f'{self.value} -> [{childrenStr}]'


