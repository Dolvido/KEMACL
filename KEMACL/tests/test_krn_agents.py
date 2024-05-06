import unittest
from KEMACL import KnowledgeRetrievalNodes

class TestKRNAgents(unittest.TestCase):
    def setUp(self):
        self.agent1 = KnowledgeRetrievalNodes.KRNAgent(name="Agent 1")
        self.agent2 = KnowledgeRetrievalNodes.KRNAgent(name="Agent 2")

    def tearDown(self):
        pass

    def test_init(self):
        # Test the initialization of KRNAgents
        self.assertEqual(self.agent1.name, "Agent 1")
        self.assertEqual(self.agent2.name, "Agent 2")

    def test_retrieve_data(self):
        # Test the retrieve_data method of KRNAgents
        data = self.agent1.retrieve_data("database_1", ["keywords"])
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0], "keyword 1")
        self.assertEqual(data[1], "keyword 2")
        self.assertEqual(data[2], "keyword 3")