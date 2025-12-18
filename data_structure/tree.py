__author__ = "akhtar"

import logging

logger = logging.getLogger(__name__)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level=None):
        # Print the whole tree if level is not passed in the argument,
        # else print upto the given level.

        if level is None:
            pass
        elif self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "└───" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
