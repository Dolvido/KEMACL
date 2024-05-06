import random
from agents import KRNAgent, AIPAgent
from modules.knowledge_retrieval import KnowledgeRetrievalNode

class KRNAgent2(KRNAgent):
    """
    This is the second agent in the KEMACL system, which specializes in retrieving knowledge from external
    databases.
    """
    def __init__(self, name, knowledge_graph, dbs):
        super().__init__(name, knowledge_graph)
        self.dbs = dbs
        self.knowledge_retrieval_node = KnowledgeRetrievalNode(name, self.knowledge_graph)

    def retrieve_knowledge(self, query):
        """
        This function retrieves knowledge from external databases based on the input query.
        :param query: A string representing the user's input.
        :return: A list of strings containing relevant information retrieved from the external databases.
        """
        # Sample code for retrieving knowledge from an external database
        return [f"{self.name} retrieved {random.choice(self.dbs)}"]

    def process_input(self, input):
        """
        This function processes the user's input and returns a list of relevant information that can be used to
        generate responses.
        :param input: A string representing the user's input.
        :return: A list of strings containing relevant information that can be used to generate responses.
        """
        # Sample code for processing the user's input and retrieving knowledge from external databases
        knowledge = self.retrieve_knowledge(input)
        return knowledge