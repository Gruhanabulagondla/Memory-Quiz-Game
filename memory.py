import random
import time


def play_game():
    items = [
        "Python",
        "Java",
        "SQL",
        "AI",
        "Cloud"
    ]

    random.shuffle(items)

    print("\nRemember these items:")
    print("--------------------")

    print(" | ".join(items))

    time.sleep(5)

    print("\n" * 30)

    print("========== MEMORY QUIZ ==========")
    print("Enter the items in the same order.")
    print("Separate them using commas.")

    answer = input("\nYour answer: ")

    user_items = [item.strip() for item in answer.split(",")]

    score = 0

    for i in range(min(len(items), len(user_items))):
        if user_items[i].lower() == items[i].lower():
            score += 1

    print("\n========== RESULT ==========")
    print("Correct sequence:")
    print(" -> ".join(items))

    print("\nYour sequence:")
    print(" -> ".join(user_items))

    print(f"\nScore: {score}/{len(items)}")

    if score == len(items):
        print("Excellent memory!")
    elif score >= 3:
        print("Good memory!")
    else:
        print("Keep practicing!")


def main():
    print("========== MEMORY QUIZ GAME ==========")

    while True:
        print("\n1. Start Game")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            print("\nThank you for playing!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()