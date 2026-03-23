import random

def snake_water_gun():
    print('Welcome to game')
    choices = ['snake','water','gun']

    user_score = 0
    comp_score = 0

    rounds = int(input("Enter the number of rounds you want to play: "))

    for i in range(1, rounds + 1):
        print(f"\nRound {i}:")
        user_choice = input("Choose Snake, Water, or Gun: ").lower()
        if user_choice not in  choices:
            print("Invalid choice! Please select from 'snake', 'water', or 'gun'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")


        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "snake" and computer_choice == "water") or \
             (user_choice == "water" and computer_choice == "gun") or \
             (user_choice == "gun" and computer_choice == "snake"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1 


    print("\nGame Over!")
    print(f"Final Score: You - {user_score} | Computer - {comp_score}")
    if user_score > comp_score:
        print("Congratulations! You win the game! 🎉")
    elif user_score < comp_score:
        print("Sorry, Computer wins the game! 🤖")
    else:
        print("It's a draw! Well played!")

snake_water_gun()