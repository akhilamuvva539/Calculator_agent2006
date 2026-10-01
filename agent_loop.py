# Observe -> Decide -> Act Agent Loop

for iteration in range(1, 4):
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

print("\nAgent loop completed after 3 iterations.")
