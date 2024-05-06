import unittest
from AIP import rules

class TestInteractionProtocol(unittest.TestCase):
    def setUp(self):
        self.aip = rules.AdaptiveInteractionProtocol()

    def tearDown(self):
        pass

    def test_protocol(self):
        # Test the protocol for a simple case of two agents
        agent1 = {'name': 'Agent 1', 'id': 0}
        agent2 = {'name': 'Agent 2', 'id': 1}

        self.aip.add_agent(agent1)
        self.aip.add_agent(agent2)

        # Test the protocol for a simple case of two agents
        self.assertTrue(self.aip.protocol(agent1, agent2))