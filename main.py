import argparse

from agents import goal_based_agent, rule_based_agent


def ask_for_number(prompt_text, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        value = input(f"{prompt_text}{suffix}: ")

        if value.strip() == "" and default is not None:
            return float(default)

        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def main():
    parser = argparse.ArgumentParser(description="Run the calculator agents.")
    parser.add_argument("--temperature", type=float, help="Current temperature value")
    parser.add_argument("--goal", type=float, help="Target temperature for the goal-based agent")
    args = parser.parse_args()

    temp = args.temperature if args.temperature is not None else ask_for_number("Enter current temperature", 72)
    goal = args.goal if args.goal is not None else ask_for_number("Enter goal temperature", 72)

    goal_action = goal_based_agent(temp, goal)
    rule_action = rule_based_agent(temp)

    print(f"\nCurrent temperature: {temp:.1f}°F")
    print(f"Goal temperature: {goal:.1f}°F")
    print(f"Goal-based agent: {goal_action}")
    print(f"Rule-based agent: {rule_action}")


if __name__ == "__main__":
    main()
