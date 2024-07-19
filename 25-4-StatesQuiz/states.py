import pandas as pd


class States:

    def __init__(self):
        self.data = pd.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()

    def exists(self, name_of_state):
        if name_of_state in self.all_states:
            return True

    def loc(self, name_of_state):
        state = self.data[self.data.state == name_of_state]
        x = int(state.x.iloc[0])
        y = int(state.y.iloc[0])
        loc = (x, y)
        return loc

    def states_to_learn(self, guessed_states):
        missing_states = [state for state in self.all_states if state not in guessed_states]
        self.data = pd.DataFrame(missing_states)
        self.data.to_csv("states_to_learn.csv")
