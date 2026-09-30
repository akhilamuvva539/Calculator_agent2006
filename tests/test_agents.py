import unittest

from agents import goal_based_agent, rule_based_agent


class AgentTests(unittest.TestCase):
    def test_goal_based_agent_cools_when_above_goal(self):
        self.assertEqual(goal_based_agent(110, 72), "cool")

    def test_goal_based_agent_heats_when_below_goal(self):
        self.assertEqual(goal_based_agent(60, 72), "heat")

    def test_goal_based_agent_idles_when_on_goal(self):
        self.assertEqual(goal_based_agent(72, 72), "idle")

    def test_rule_based_agent_cools_when_too_hot(self):
        self.assertEqual(rule_based_agent(101), "cool")

    def test_rule_based_agent_idles_when_not_too_hot(self):
        self.assertEqual(rule_based_agent(100), "idle")


if __name__ == "__main__":
    unittest.main()
