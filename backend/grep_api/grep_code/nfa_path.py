#!/usr/bin/env python3

import sys
from collections import deque
from dataclasses import dataclass
########################        1. NFA        ########################
# design a datastructure to define an NFA

''' NFA FILE:
Line:
    1. list of states                  q1 q2 q3 q4
    2. alphabet                        0 1
    3. initial state                   q1
    4. list of accept states           q4
    5+. transitions                    q1 0 q1
                                       q1 1 q1
                                        ...

'''

# NFA DATASTRUCTURE
# @dataclass
# class NFA():
#     # temporary
#     states: list = []
#     alphabet: list = []
#     initial: str = ""
#     accepts: list = []
#     transitions: list = []

class NFA():
    # states, alphabet, initial, accepts, transitions
    def __init__(self, states, alphabet, initial, accepts, transitions):
        self.states = states
        self.alphabet = alphabet 
        self.initial = initial
        self.accepts = accepts 
        self.transitions = transitions 
        
    def __str__(self):
        return "States: {}\nAlphabet: {}\nInitial: {}\nAccepts: {}\nTransitions: {}\n".format(self.states, self.alphabet, self.initial, self.accepts, self.transitions)
    
    def get_json_info(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'initial': self.initial,
            'accepts': self.accepts,
            'transitions': self.transitions,
        }

def read_nfa(file):
    '''
    • file: File containing definition of NFA M
    • Returns: The NFA M
    
    Reads in a file and converts it to an NFA
    '''
    states = set()
    alphabet = set()
    initial = ""
    accepts = set()
    transitions = []
    
    
    with open(file) as f:
        count = 0
        for line in f:
            # print(line)
            
            # for transitions
            if count > 3:
                line = line.split() # separates into list by whitespace
                transitions.append(line) # adds to M.transitions

                pass
            # for states
            if count == 0:
                line = line.split() # separates into list by whitespace
                # adds to M.states
                for state in line: states.add(state) # adds to M.states

            # for alphabet
            elif count == 1:
                line = line.split()
                for symb in line: alphabet.add(symb)
            # for initial state
            elif count == 2:
                line = line.strip()
                # M.initial = line
                initial = line

                pass
            # for accept states
            elif count == 3:
                line = line.split() # separates into list by whitespace
                # adds to M.accepts
                for accept in line: accepts.add(accept)
                pass
            else:
                pass
                
            count += 1
            pass
        pass
    
    # converting into a dictionary of {str: set}
    t = {state: {} for state in states}
    for start, symbol, end in transitions:
        if symbol not in t[start]:
            t[start][symbol] = set()
        t[start][symbol].add(end)
        
    return NFA(states, alphabet, initial, accepts, t)
    

def write_nfa(M, file):
    '''
    • M: The NFA to write
    • file: File to write to
    • Effect: Writes definition of M to file
    
    Stores and represents NFA (M) to a specified file.
    '''
    
    
    
    with open(file, 'w') as f:
        f.write(' '.join(M.states) + "\n")
        f.write(' '.join(M.alphabet)+ "\n")
        f.write(M.initial + "\n")
        f.write(' '.join(M.accepts)+ "\n")
        for t in M.transitions:
            f.write(' '.join(t) + "\n")
    
    pass

########################        2. MATCHER        ########################
# find all end_nodes
def find_end_nodes(nodes, w_len, accepts):
    # LIST OF VALID ENDING NODES FOR A PATH
    valid_end_nodes = []

    # for every node we've visited
    for node in nodes:
        # check if the ending node is valid
        if node[1] == w_len and node[0] in accepts:
            valid_end_nodes.append(node)
    
    return valid_end_nodes

def match(M, w):
    queue = deque([(M.initial, 0)])
    visited = set()
    nodes = {}  # To track paths and transitions

    while queue:
        current_state, position = queue.popleft()
        
        # Avoid re-transition
        if (current_state, position) in visited:
            continue
        visited.add((current_state, position))

        # Handle epsilon transitions
        for next_state in M.transitions[current_state].get('&', []):
            if (next_state, position) not in visited:
                nodes[(next_state, position)] = (current_state, position, '&')  
                queue.append((next_state, position))

        # Check the next transition
        if position < len(w):
            next_symbol = w[position]
            for next_state in M.transitions[current_state].get(next_symbol, []):
                if (next_state, position + 1) not in visited:
                    # Record symbol transition
                    nodes[(next_state, position + 1)] = (current_state, position, next_symbol)
                    queue.append((next_state, position + 1))

    valid_end_nodes = [(state, pos) for state, pos in visited if state in M.accepts and pos == len(w)]

    # Return the path reconstruction if a valid end node is found
    return find_path(nodes, valid_end_nodes, w)

def find_path(nodes, valid_end_nodes, w):
    if not valid_end_nodes:
        return False, []

    path = []
    
    # Assuming we pick the first valid end node for simplicity
    current_node = valid_end_nodes[0]  

    # Backtrack
    while current_node in nodes and nodes[current_node] is not None:
        prev_node_info = nodes[current_node] 
        prev_state, prev_position, symbol = prev_node_info
        path.insert(0, (prev_state, symbol, current_node[0]))  
        current_node = (prev_state, prev_position)

    return True, path

########################        3. PUTTING IT TOGETHER        ########################
# def test_nfa(file, w):
#     M = read_nfa(file)
#     accept, path = match(M, w)

#     if accept:
#         print("accept")
#         for (start, symbol, end) in path:
#                 print(f"{start} {symbol} {end}")
#     else:
#         print("reject")

# def main():
#     if len(sys.argv) != 3:
#         print("Usage is: nfa.py <nfa_file> <input_string>")
#         return

#     nfa_file = sys.argv[1]
#     input_string = sys.argv[2]
#     test_nfa(nfa_file, input_string)
    
if __name__ == "__main__":
    main()