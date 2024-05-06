import json

class AIPRules:
    def __init__(self, rules):
        self.rules = rules

    def apply(self, agent_a, agent_b, task, action):
        for rule in self.rules:
            if rule["condition"](agent_a, agent_b, task, action):
                return rule["action"]()