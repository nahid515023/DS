class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def Print_tree(self):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.Print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level


def main():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('hp'))
    laptop.add_child(TreeNode('lenovo'))

    tv = TreeNode('Tv')
    tv.add_child(TreeNode('Lg'))
    tv.add_child(TreeNode('samsum'))

    cell_phone = TreeNode('Sell-Phone')
    cell_phone.add_child(TreeNode('samsum'))
    cell_phone.add_child(TreeNode('vivo'))
    cell_phone.add_child(TreeNode('oppo'))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = main()
    root.Print_tree()
