import json

class CLEM:
    def __init__(self, agent_config):
        self.agent_config = agent_config
        self.replay_buffer = []

    def add_experience(self, experience):
        self.replay_buffer.append(experience)

    def learn_from_experience(self, learning_rate):
        experiences = self.replay_buffer
        for experience in experiences:
            state = experience[0]
            action = experience[1]
            next_state = experience[2]
            reward = experience[3]
            done = experience[4]
            if done:
                self.update_model(state, action, reward)
            else:
                self.update_model(state, action, reward, next_state)

    def update_model(self, state, action, reward):
        pass