#!/usr/bin/env python3

class NFA():
    # states, alphabet, initial, accepts, transitions
    def __init__(self, states: list=None, alphabet: set=None, initial:str=None, accepts:list=None, transitions:dict[str, dict[str, str]]=None):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial 
        self.accepts = accepts 
        self.transitions = transitions # dict[str, dict[str, str]]
        
    def __str__(self):
        # print("States: ")
        # print(self.states)
        return "States: {}\nAlphabet: {}\nInitial: {}\nAccepts: {}\nTransitions: {}\n".format(self.states, self.alphabet, self.initial, self.accepts, self.transitions)
        # print("self.states\nself.alphabet\nself.initial\nself.accepts\nself.transitions\n")

    def get_json_info(self):
        return {
            'states': self.states,
            'alphabet': self.alphabet,
            'initial': self.initial,
            'accepts': self.accepts,
            'transitions': self.transitions,
        }


def string_nfa(w: str) -> None:
    '''
    Creates an NFA that accepts exactly one string.
    
    usage: "string_nfa w"
    • w: a string (possibly empty)
    • Output: an NFA recognizing the language {w}
    '''
    
    states = ["q" + str(i+1) for i in range(len(w) + 1)]
    alphabet = set(w)
    initial = states[0]
    accepts = [states[-1]]
    transitions = {state: {} for state in states}
    
    for i, symbol in enumerate(w):
        if symbol not in transitions[states[i]]: transitions[states[i]][symbol] = []
        transitions[states[i]][symbol].append(states[i + 1])
        
    # print(change_states(transitions))
    
    return NFA(states, alphabet, initial, accepts, transitions)
    

def union(list1, list2):
    for val in list2:
        if val not in list1: list1.append(val)
        
    return list1

def change_states(M, NFA_num):
    # Transitions: {'q1': {'a': ['q2']}, 'q2': {'b': ['q3']}, 'q3': {'c': ['q4']}, 'q4': {}}
    
    if NFA_num == 0: prefix = "M1_"
    else: prefix = "M2_"
    
    M.initial = prefix + M.initial
    M.accepts = [prefix + accept for accept in M.accepts]
    M.states = [prefix + state for state in M.states]
    d = M.transitions
    
    # for every start
    for start in d:
        # for every symbol
        for symbol in d[start]:
            # get end states
            possible_end_states = d[start][symbol]
            
            # loop through end states and change
            for i, end_state in enumerate(possible_end_states):
                new_end_state = prefix + end_state
                d[start][symbol][i] = new_end_state
            
        # now change symbol for every start
    
    starts = list(d.keys())
    
    # print(starts)
    for start in starts:
        new_start = prefix + start
        d[new_start] = d.pop(start)
    
    return M
        
        # loop through every transitions
        # loop through every end state and change
    

def union_nfa(M1, M2) -> None:
    '''
    Creates an NFA with union from two NFAs
    
    usage: "union_nfa M1 M2"
    • M1: NFA
    • M2: NFA
    • Output: an NFA recognizing the language of union M1, M2
    '''
    
    # union states + new initial
    # union alphabet
    # create new initial
    # create two new E-transitions to previous initial
    # add to transitions
    # change M2 dictionary keys
    # union accepts
    initial = "q0"
    M1 = change_states(M1, 0)
    M2 = change_states(M2, 1)
    # print(M2)
    
    # union states + new initial
    states = union(M1.states, M2.states)
    states.insert(0, initial)
    
    # union alphabet    
    alphabet = M1.alphabet | M2.alphabet

    # create new initial
    
    # union accepts
    accepts = union(M1.accepts, M2.accepts)
    
    transitions = {
                    initial: {
                        '&': [M1.initial, M2.initial],
                    }
                   }
    

    transitions.update(M1.transitions)
    transitions.update(M2.transitions)
    # q1 & q2
    # returns an output file
    # union we want to rename states and rename transitions with that state
    return NFA(states, alphabet, initial, accepts, transitions)
    
    pass
    
def concat_nfa(M1, M2) -> None:
    '''
    Creates an NFA by concatenating two NFAs
    
    usage: "concat_nfa M1 M2"
    • M1: NFA
    • M2: NFA
    • Output: NFA recognizing language L(M1) ◦ L(M2)
    '''
    
    # union states
    # union alphabet
    # M1 initial
    # create E-transition from M1 accepts to M2 initial
    # add to transitions
    # only M2 accepts
    M1 = change_states(M1, 0)
    M2 = change_states(M2, 1)
    # union states + new initial
    states = union(M1.states, M2.states)
    # union alphabet    
    alphabet = M1.alphabet | M2.alphabet
    # M1 initial
    initial = M1.initial
    
    # only M2 accepts
    accepts = M2.accepts
    
    # create E-transition from M1 accepts to M2 initial
# Transitions: {'q0': {'&': ['q1', 'r1']}, 'q1': {'a': ['q2']}, 'q2': {'b': ['q3']}, 'q3': {'c': ['q4']}, 'q4': {}, 'r1': {'d': ['r2']}, 'r2': {'e': ['r3']}, 'r3': {'f': ['r4']}, 'r4': {}}
    transitions = {}
    # print(transitions)
    
    # print(M1.accepts)

    # new transition from M1 accept to M2 initial
    
    transitions.update(M1.transitions)
    transitions.update(M2.transitions)
    
    for old_accept in M1.accepts:

        # transitions[old_accept]['&'] = [M2.initial]
        try: transitions[old_accept]['&'].append(M2.initial)
        except KeyError: transitions[old_accept]['&'] = [M2.initial]
    
    return NFA(states, alphabet, initial, accepts, transitions)

    

def star_nfa(M) -> None:
    '''
    Creates an NFA by kleene star operation on M
    
    usage: "star_nfa M"
    • M1: NFA
    • M2: NFA
    • Output: NFA recognizing language L(M)^*
    '''
    
    # new initial state (q0) + old states
    # same alphabet
    # new initial state (q0)
    # create E-transition from M1 accept to M2 initial
    # add to transitions
    # q0 and old accepts
    
    # new initial state (q0) + old states
    initial = "q0"
    states = M.states
    states.insert(0, initial)
    
    # same alphabet
    alphabet = M.alphabet
    # new initial state (q0)
    
    # q0 and old accepts
    accepts = M.accepts
    accepts.append(initial)
    
    # create E-transition from M1 accept to M2 initial
    # add to transitions
    
    # add e transition for new initial
    transitions = {initial: {'&': [M.initial]}}   
    # add existing transitions
    transitions.update(M.transitions)
    # add accept --> initial e transition

    for accept in M.accepts:
        if accept == initial: continue
        
        try: transitions[accept]['&'].append(initial)
        except KeyError: transitions[accept]['&'] = [initial]
        
        
    return NFA(states, alphabet, initial, accepts, transitions)
    
    '''
    q1 q2 q3 q4         STATES
    0 1                 ALPHABET
    q1                  INITIAL
    q4                  ACCEPTS
    q1 0 q1             TRANSITIONS: (curr letter next)
    q1 1 q1
    q1 1 q2
    q2 0 q3
    q2 1 q3
    q3 0 q4
    q3 1 q4
    '''
    
    pass

def main():
    # Main function to parse regular expressions passed as command-line arguments.
    # print(read_nfa('test.nfa'))
    pass

if __name__ == "__main__":
    main()

# M0 = string_nfa("abc")
# # print(M0)
# M1 = string_nfa("abc")
# M2 = string_nfa("def")
# M1uM2 = union_nfa(M1, M2)
# print(M1uM2)

# M1 = string_nfa("abc")
# M2 = string_nfa("def")
# M1cM2 = concat_nfa(M1, M2)
# print(M1cM2)

# M1 = string_nfa("abc")
# M1s = star_nfa(M1)
# print(M1s)

# write_nfa(M1, "/escnfs/home/dkim37/theory/Turing-Testers/cp2/test.nfa")
# write_nfa(string_nfa("abksdjfsdfc"), "/escnfs/home/dkim37/theory/Turing-Testers/cp2/test.nfa")