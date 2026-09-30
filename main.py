import argparse

from agents import goal_based_agent, rule_based_agent


def ask_for_temperature(prompt_text):
    while True:
        try:
            value = input(prompt_text)
            return float(value)
        except ValueError:
            print("Please enter a valid number for temperature.")


def main():
    parser = argparse.ArgumentParser(description="Run the calculator agents.")
    parser.add_argument("--temperature", type=float, help="Current temperature value")
    parser.add_argument("--goal", type=float, default=72, help="Target temperature for the goal-based agent")
    args = parser.parse_args()

    if args.temperature is None:
        temp = ask_for_temperature("Enter current temperature: ")
    else:
        temp = args.temperature

    goal_action = goal_based_agent(temp, args.goal)
    rule_action = rule_based_agent(temp)

    print(f"\nCurrent temperature: {temp} F")
    print(f"Goal temperature: {args.goal} F")
    print(f"Goal-based agent: {goal_action}")
    print(f"Rule-based agent: {rule_action}")


if __name__ == "__main__":
    main()
