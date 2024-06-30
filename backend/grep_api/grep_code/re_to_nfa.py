#!/usr/bin/env python3
import sys
import os

import sys

from .nfa_regops import string_nfa, union_nfa, concat_nfa, star_nfa

class Node:
    # Node class for the syntax tree. Each node represents a part of the regular expression.
    def __init__(self, type, children=None, value=None, nfa=None):
        self.type = type  # The type of node ('symbol', 'union', 'concat', 'star', 'epsilon')
        self.children = children if children is not None else []  # Child nodes for 'union', 'concat', 'star'
        self.value = value  # The character value for 'symbol' nodes
        
        if self.type == 'symbol':
            nfa = string_nfa(self.value)
        elif self.type == 'epsilon':
            nfa = string_nfa('')
        elif self.type == 'union':
            nfa = union_nfa(children[0].nfa, children[1].nfa)
        elif self.type == 'concat':
            nfa = concat_nfa(children[0].nfa, children[1].nfa)
        elif self.type == 'star':
            nfa = star_nfa(children[0].nfa)
        else:
            nfa = None
            
        self.nfa = nfa
        
        # print(nfa)
        
    def __str__(self):
        # Generate a string representation of the node for printing.
        if self.type == 'symbol':
            return f'symbol("{self.value}")'
        elif self.type == 'epsilon':
            return 'epsilon()'
        elif self.children:
            return f'{self.type}({",".join(str(child) for child in self.children)})'
        else:
            return self.type

    # def to_nfa(self):
    #     # Generate a string representation of the node for printing.
    #     if self.type == 'symbol':
    #         return string_nfa(self.value)
    #     elif self.type == 'epsilon':
    #         return string_nfa('')
    #     elif self.type == 'union':
    #         return nfa_union(children[0].nfa, children[1).nfa)
    #     elif self.type == 'concat':
    #         return nfa_concat(to_nfa(children[0]), to_nfa(children[1]))
    #     elif self.type == 'star':
    #         return nfa_star(to_nfa(children[0]), to_nfa(children[1]))
    #     elif self.children:
    #         return f'{self.type}({",".join(str(child) for child in self.children)})'
    #     else:
    #         return self.type
        
        
        # if self.type == 'symbol':
        #     return f'symbol("{self.value}")'
        # elif self.type == 'epsilon':
        #     return 'epsilon()'
        # elif self.children:
        #     return f'{self.type}({",".join(str(child) for child in self.children)})'
        # else:
        #     return self.type

def parse_expression(expr, index=0):
    # Parse an expression, handling the union operator '|' with lower precedence.
    if index >= len(expr):
        # Handle empty expression by returning an epsilon node.
        return Node('epsilon'), index
    
    
    node, index = parse_term(expr, index)
    while index < len(expr) and expr[index] == '|':
        # Handle union by creating a 'union' node with left and right operands.
        next_node, index = parse_term(expr, index + 1)
        node = Node('union', children=[node, next_node])
    return node, index

def parse_term(expr, index):
    # Parse a term, handling concatenation implicitly with higher precedence than union.
    if index >= len(expr) or expr[index] in '|)':
        # If the term is empty or we reach a union or closing parenthesis, return an epsilon node.
        return Node('epsilon'), index
    node, index = parse_factor(expr, index)
    while index < len(expr) and expr[index] not in '|)':
        # Concatenate sequences of factors.
        next_node, index = parse_factor(expr, index)
        if next_node.type != 'epsilon':
            node = Node('concat', children=[node, next_node])
    return node, index

def parse_factor(expr, index):
    # Parse a factor, which can be an expression in parentheses, a symbol, or a symbol followed by '*'.
    if index >= len(expr):
        # Handle end of expression with an epsilon node.
        return Node('epsilon'), index
    if expr[index] == '(':
        if index + 1 < len(expr) and expr[index + 1] == ')':
            # Handle empty parentheses '()' as epsilon.
            node = Node('epsilon')
            index += 2  # Skip the empty parentheses
        else:
            # Recursively parse expressions inside parentheses.
            node, index = parse_expression(expr, index + 1)
            if index >= len(expr) or expr[index] != ')':
                raise ValueError
            index += 1  # Skip the closing parenthesis
    else:
        # Handle symbols.
        node = Node('symbol', value=expr[index])
        index += 1

    if index < len(expr) and expr[index] == '*':
        # Handle Kleene star by wrapping the node with a 'star' node.
        node = Node('star', children=[node])
        index += 1

    return node, index

def parse_re(regexp):
    # Parse the entire regular expression and return the syntax tree's root node.
    tree, index = parse_expression(regexp)
    if index != len(regexp):
        # If not all characters were consumed, it indicates an unexpected character or structure.
        raise ValueError
    
    return tree.nfa


def re_to_nfa(regexp):
    nfa = parse_re(regexp)
    
    # out_file = 're_to_nfa.nfa'
    # # print(nfa)
    # write_nfa(nfa, out_file)
    # os.system(f'cat {out_file}')
    
    return nfa


def main():
    
    if len(sys.argv) != 2:
        print("Usage: re_to_nfa 'regexp'")
        return
    
    regexp = sys.argv[1]
    
    re_to_nfa(regexp)
    
    # print(regexp)
    

if __name__ == "__main__":
    main()