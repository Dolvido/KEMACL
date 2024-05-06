import logging
import os
import sys
from itertools import chain

from aip.rules import AIPRules
from clem.learning_mechanism import LearningMechanism
from knowledge_retrieval_nodes.krn_agent import KRNAgent
from generative_learning_agents.gla_agent import GLAAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MainSystem:
    def __init__(self):
        self.krn_agents = []
        self.gla_agents = []
        self.aip_rules = AIPRules()
        self.clem = LearningMechanism()

    def start(self):
        self._initialize_agents()
        self._start_agents()

    def _initialize_agents(self):
        for idx in range(3):
            krn_agent = KRNAgent(f"KRN-{idx}")
            gla_agent = GLAAgent(f"GLA-{idx}")
            self.krn_agents.append(krn_agent)
            self.gla_agents.append(gla_agent)

    def _start_agents(self):
        for krn_agent, gla_agent in zip(self.krn_agents, self.gla_agents):
            krn_agent.start()
            gla_agent.start()

    def run(self):
        while True:
            logger.info("Starting iteration...")
            for krn_agent in self.krn_agents:
                krn_agent.run()

            for gla_agent in self.gla_agents:
                gla_agent.run()

            self.aip_rules.apply(self.krn_agents, self.gla_agents)

            logger.info("Applying learning mechanism...")
            self.clem.learn(self.krn_agents, self.gla_agents)

            logger.info("Ending iteration...")

if __name__ == "__main__":
    main_system = MainSystem()
    main_system.start()
    main_system.run()