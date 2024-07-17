import pandas as pd


class States:

    def __init__(self):
        self.data = pd.read_csv("50_states.csv")
        self.states_list = self.data.state.to_list()

    def exists(self, name_of_state):
        if name_of_state in self.states_list:
            return True

    def loc(self, name_of_state):
        state = self.data[self.data.state == name_of_state]
        x = int(state.x.iloc[0])
        y = int(state.y.iloc[0])
        loc = (x, y)
        return loc

    def states_to_learn(self, guessed_states):
        for state in guessed_states:
            self.states_list.remove(state)
        self.states_dict = {
            "states": self.states_list
        }
        self.data = pd.DataFrame(self.states_dict)
        self.data.to_csv("states_to_learn.csv")