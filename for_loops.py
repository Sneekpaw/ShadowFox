# Day 5 - For Loop Tasks
import random

# ------------------------------------------
# Task 1: Dice Rolling Simulator
# ------------------------------------------
def task_dice_rolls():
    print("\n=== Task 1: Dice Rolling Simulator ===")

    rolls = 20  # minimum 20
    dice_results = []

    count_six = 0
    count_one = 0
    count_two_six_in_row = 0

    previous_roll = None

    # Roll the dice 20 times
    for i in range(rolls):
        roll = random.randint(1, 6)
        dice_results.append(roll)
        print(f"Roll {i+1}: {roll}")

        # Count 6s
        if roll == 6:
            count_six += 1

        # Count 1s
        if roll == 1:
            count_one += 1

        # Count two consecutive 6s
        if roll == 6 and previous_roll == 6:
            count_two_six_in_row += 1

        previous_roll = roll

    print("\n--- Dice Results Summary ---")
    print("Total rolls:", rolls)
    print("Times rolled 6:", count_six)
    print("Times rolled 1:", count_one)
    print("Times two consecutive 6s:", count_two_six_in_row)
    print("All rolls:", dice_results)


# ------------------------------------------
# Task 2: Jumping Jacks Workout Program
# ------------------------------------------
def task_jumping_jacks():
    print("\n=== Task 2: Jumping Jacks Workout ===")

    total_jacks = 100
    set_size = 10
    completed = 0

    for i in range(1, (total_jacks // set_size) + 1):
        print(f"\nPerform set {i}: Do {set_size} jumping jacks.")

        completed += set_size

        # Ask the user
        tired = input("Are you tired? (yes/no): ").strip().lower()

        if tired in ["yes", "y"]:
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ["yes", "y"]:
                print(f"\nYou completed a total of {completed} jumping jacks.")
                return  # exit task
            else:
                remaining = total_jacks - completed
                print(f"{remaining} jumping jacks remaining. Continue!")
        else:
            remaining = total_jacks - completed
            print(f"{remaining} jumping jacks remaining.")

    # Completed all
    print("\n🎉 Congratulations! You completed the workout! 🎉")


# ------------------------------------------
# Main Menu
# ------------------------------------------
def main():
    print("Day 5 - For Loops\n")

    while True:
        print("\nChoose a task:")
        print("1 - Dice Rolling Simulator")
        print("2 - Jumping Jacks Workout Tracker")
        print("0 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_dice_rolls()
        elif choice == "2":
            task_jumping_jacks()
        elif choice == "0":
            print("Exiting Day 5 Tasks. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
