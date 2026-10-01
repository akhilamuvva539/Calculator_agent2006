# Observe -> Decide -> Act Agent Loop

def run_agent_loop(max_iters=10):
    for iteration in range(1, max_iters + 1):
        print(f"\n--- Iteration {iteration} ---")

        # 1. OBSERVE
        observation = input("Observe: Enter current situation: ")

        # 2. DECIDE
        if "rain" in observation.lower():
            decision = "Carry an umbrella"
        elif "hot" in observation.lower():
            decision = "Drink water"
        else:
            decision = "Continue normally"

        print("Decide:", decision)

        # 3. ACT
        print("Act:", decision)

    return "failure"


if __name__ == "__main__":
    result = run_agent_loop()
    print("\nAgent loop result:", result)
