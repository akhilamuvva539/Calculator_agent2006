def run_agent_steps(steps):
    state = {"done": False, "steps": []}

    for step in steps:
        state["steps"].append(step)
        print("Step:", step)

    state["done"] = True
    return state


if __name__ == "__main__":
    agent_state = run_agent_steps(["Observe", "Decide", "Act"])
    print("State:", agent_state)
