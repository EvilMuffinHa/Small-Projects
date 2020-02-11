class Error(Exception):
    pass

class TreeError(Error):
    pass

class BinTreeError(TreeError):
    pass


class Tree:
    def __init__(self):
        self.base = ''
        self.values = []
    def __str__(self):
        return '(' + str(self.base) + ' -> ' + str(self.values) + ')'
    def __repr__(self):
        return '(' + str(self.base) + ' -> ' + str(self.values) + ')'
    def overwriteBase(self, base):
        if isinstance(base, Tree):
            raise TreeError('Cannot have a tree as a base')
        else:
            self.base = base
    def appendChild(self, values):
        self.values.append(values)
    def appendChildren(self, *args):
        for arg in args:
            self.values.append(arg)
    def deleteChild(self, location):
        try:
            x = self.values[location]
            del self.values[location]
            return x
        except:
            raise TreeError('Child does not exist')

class BinTree(Tree):
    def appendChild(self, values):
        if len(self.values) < 2:
            self.values.append(values)
        else:
            raise BinTreeError('Binary Trees can only have two children. ')
    def appendChildren(self, values):
        raise BinTreeError('Binary Trees cannot append multiple values. ')


