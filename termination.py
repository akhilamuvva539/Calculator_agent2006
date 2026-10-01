def get_result(done):
    if done:
        return "success"
    return "failure"


def main():
    while True:
        answer = input("Is the task complete? (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            done = True
            break
        if answer in {"no", "n"}:
            done = False
            break
        print("Please enter yes or no.")

    print("Result:", get_result(done))


if __name__ == "__main__":
    main()
