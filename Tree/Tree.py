class Error(Exception):
    pass

class TreeError(Error):
    pass

class BinTreeError(TreeError):
    pass


class Tree:
    def __init__(self):
        self.base = ''
        self.children = []
    def __str__(self):
        return '(' + str(self.base) + ' -> ' + str(self.children) + ')'
    def __repr__(self):
        return '(' + str(self.base) + ' -> ' + str(self.children) + ')'
    def overwriteBase(self, base):
        if isinstance(base, Tree):
            raise TreeError('Cannot have a tree as a base')
        else:
            self.base = base
    def appendChild(self, children):
        self.children.append(children)
    def appendChildren(self, *args):
        for arg in args:
            self.children.append(arg)
    def deleteChild(self, location):
        try:
            x = self.children[location]
            del self.children[location]
            return x
        except:
            raise TreeError('Child does not exist')

#Binary trees
class BinTree(Tree):
    def appendChild(self, children):
        if len(self.children) < 2:
            self.children.append(children)
        else:
            raise BinTreeError('Binary Trees can only have two children. ')
    def appendChildren(self, children):
        raise BinTreeError('Binary Trees cannot append multiple children. ')


