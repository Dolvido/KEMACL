import unittest
from gla_agent_1 import GLATeam
from gla_agent_2 import GLAgent

class TestGLATeams(unittest.TestCase):
    def setUp(self):
        self.team = GLATeam()
        self.agent = GLAgent()

    def test_gla_teams(self):
        # check that the team has the expected number of agents
        self.assertEqual(len(self.team), 2)

        # check that the agent is part of the team
        self.assertIn(self.agent, self.team)

        # check that the team can access its members
        self.assertEqual(self.team[0], self.agent)

if __name__ == '__main__':
    unittest.main()