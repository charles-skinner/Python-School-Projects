'''
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    tr = BST()
    f = open("around-the-world-in-80-days-3.txt","r")
    content = f.readlines()
    for line in content:
        for char in line:
            if char.isalpha() or char.isdigit():
                pair = Pair(char)
                try:
                    tr.find(pair).count += 1
                except:
                    tr.add(pair)
    return tr
    

def main():
    ''' 
    Program kicks off here.

    '''
    tr = make_tree()
    print(tr.preorder())
    print(tr.height())
    print(tr.size())


if __name__ == "__main__":
    main()
