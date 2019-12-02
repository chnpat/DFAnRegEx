from DFA import DFA
import json

def collectData():

    # Read a JSON file for collecting DFA data
    with open("data1.json", "r") as myfile:
        data = json.load(myfile)

    # Extract data sets from the JSON object
    states = set(data["states"])
    alphabets = set(data["alphabets"])
    init_state = set(data["init_state"])
    final_states = set(data["final_states"])
    edges = set((tuple(edge) for edge in data["edges"]))

    # Create an object instance of DFA class
    dfa = DFA(states,alphabets,init_state,final_states,edges)

    # Return to the main procedure
    return dfa