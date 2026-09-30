def goal_based_agent(current_temperature, goal_temperature=72):
    """Return an action based on the current temperature relative to a target."""
    if current_temperature > goal_temperature:
        return "cool"
    if current_temperature < goal_temperature:
        return "heat"
    return "idle"


def rule_based_agent(temperature):
    """Return a cooling action when the temperature exceeds the rule threshold."""
    if temperature > 100:
        return "cool"
    return "idle"


def run_goal_based_demo():
    temperatures = [110, 90, 72, 60, 40]
    for temp in temperatures:
        action = goal_based_agent(temp)
        print(
            f"Temperature: {temp}°F -> "
            f"Goal: 72°F -> "
            f"Action: {action}"
        )


def run_rule_based_demo():
    temperatures = [80, 100, 101, 120]
    for temp in temperatures:
        action = rule_based_agent(temp)
        print(f"Temperature:{temp}")
        print(f"Agent action:{action}")
        print("-" * 30)


def run_demo():
    print("Goal-based agent demo")
    run_goal_based_demo()
    print("---")
    print("Rule-based agent demo")
    run_rule_based_demo()


if __name__ == "__main__":
    run_demo()
