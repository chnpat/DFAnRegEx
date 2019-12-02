from DFA import DFA
import Conversion

# Get a data from JSON file
dfa = Conversion.collectData();

# Draw an input data as a diagram and
dfa.drawAutomata('Initial DFA', "DFA1")
