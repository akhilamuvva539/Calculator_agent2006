import argparse

from agents import goal_based_agent, rule_based_agent


def main():
    parser = argparse.ArgumentParser(description="Run the calculator agents.")
    parser.add_argument("--temperature", type=float, required=True, help="Current temperature value")
    parser.add_argument("--goal", type=float, default=72, help="Target temperature for the goal-based agent")
    args = parser.parse_args()

    goal_action = goal_based_agent(args.temperature, args.goal)
    rule_action = rule_based_agent(args.temperature)

    print(f"Goal-based agent: {goal_action}")
    print(f"Rule-based agent: {rule_action}")


if __name__ == "__main__":
    main()
