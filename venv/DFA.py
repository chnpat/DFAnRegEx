import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from graphviz import Digraph

class DFA:
    def __init__(self, states, alphabets, init_state, final_states, transition_set):
        self.states = states
        self.alphabets = alphabets
        self.init_state = init_state
        self.final_states = final_states
        self.transition_set = transition_set

    def drawAutomata(self, label, filename):
        graph = Digraph()
        graph.attr('node', shape='point')
        graph.node('qi')
        for i in self.states:
            if i in self.final_states:
                graph.attr('node', shape='doublecircle', color='darkgreen', style='')
            elif i in self.init_state:
                graph.attr('node', shape='circle', color='navy', style='')
            else:
                graph.attr('node', shape='circle', color='black', style='')
            graph.node(str(i))
            if i in self.init_state:
                graph.edge('qi', str(i), 'start')
        for e in self.transition_set:
            graph.edge(e[0], e[2], e[1])

        graph.body.append(r'label = "\n\n{0}"'.format(label))
        graph.render("{0}".format(filename), view=True)

