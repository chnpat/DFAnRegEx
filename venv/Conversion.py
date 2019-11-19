from DFA import DFA

def collectData():
    # For specifying a list of states
    states = set(raw_input("1___Enter all states in DFA, separating with commas (e.g. q0,q1,q2) : ").split(","))

    # For specifying a list of alphabets used in this automata
    alphabets = set(raw_input("2___Enter all alphabets of the language, separating with commas (e.g. a,b,c) : ").split(","))

    # For setting up initial state.
    init_state = set(raw_input("3___Enter an initial state name (It must be in the states list) : ").split(","))
    while(not init_state.issubset(states)):
        print("xxxxxx Error !! please enter only a state name that defined in the list of above states")
        init_state = set(raw_input("3___Enter an initial state name (It must be in the states list) : "))

    # For setting up final states.
    final_states = set(raw_input("4___Enter all final states in DFA, separating with commas (e.g. q1,q2) : ").split(","))
    while(not final_states.issubset(states)):
        print("xxxxxx Error !! please enter only a list of states that defined in the states ")
        final_states = set(
            raw_input("4___Enter all final states in DFA, separating with commas (e.g. q1,q2) : ").split(","))

    # For setting edges between nodes
    edges = set()
    edges_list = list(raw_input("5___Enter all edges in a graph as a set of three value separated by commas, and each set must be seperated by pipe symbol | (e.g. q1,a,q1 | q1,b,q2) : ").split("|"))
    for e in edges_list:
        edge = tuple(e.split(","))
        if(edge[0] in states and edge[2] in states and edge[1] in alphabets):
            edges.add(edge)
        else:
            break

    # Displays the input DFA
    print "========================================"
    print "States : { " + ", ".join(states) + " }"
    print "Alphabets : {" + ", ".join(alphabets) + " }"
    print "Initial State : { " + ", ".join(init_state) + " }"
    print "Final States : { " + ", ".join(final_states) + " }"
    print "Edges : "
    for e in edges:
        print e
    print "========================================"

    dfa = DFA(states, alphabets, set(init_state), final_states, edges)
    return dfa

