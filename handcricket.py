import random

print("\n------------ HANDCRICKET ------------\n")

def get_input(msg):
    while True:
        try:
            value = int(input(msg))
            if value in range(1,11):
                return value
            else:
                print("ERROR | Please enter a valid number between 1 and 10!")
        except ValueError:
            print("ERROR | Please enter a valid number")

# TOSS
print("--- TOSS ---")
while True:
    usr_choice = input("Choose ODD or EVEN: ").lower()
    if usr_choice == "odd":
        usr_choice = 1
        break
    elif usr_choice == "even":
        usr_choice == 2
        break
    else:
        print("ERROR | Please enter a valid choice - Odd or Even")

comp_num = random.randint(1,10)
usr_num = get_input("Enter your choice (1 to 10): ")
print(f"Computer choice: {comp_num}\n")
summ = comp_num + usr_num

if (usr_choice == 1 and summ % 2 != 0) or (usr_choice == 2 and summ % 2 == 0):
    toss = True
    print("You won the toss!")
else:
    toss = False
    print("You lost the toss!")

# Thanks ChatGPT
if toss:
    while True:
        choice = input("\nChoose batting or bowling (bat or bowl): ").lower()
        if choice in ('bat', 'bowl'):
            usr_bat = (choice == "bat")
            break
        else:
            print("ERROR | Invalid choice. Please choose bat or bowl!")
else:
    usr_bat = random.choice([True, False])
    print(f"Computer chose to {'bat' if usr_bat else 'bowl'} first!")

# Gameplay
usr_score = 0
comp_score = 0
innings = 0

print("\n--- GAME ---")

while innings < 2:
    print(f"\n{"You are" if usr_bat else "Computer is"} batting")
    while True:
        comp_run = random.randint(1,10)
        usr_run = get_input("\nEnter your run (1 to 10): ")
        print(f"Computer chose: {comp_run}")

        if usr_run == comp_run:
            print("\nOUT!")
            break
        elif usr_bat:
            usr_score += usr_run
            print(f"RUNS: {usr_score}")
        else:
            comp_score += comp_run
            print(f"RUNS: {comp_score}")
    
    if innings == 0:
        print(f"\nEnd of first innings | {"Your" if usr_bat else "Computer's"} runs: {usr_score if usr_bat else comp_score}")
        usr_bat = not usr_bat # Switch roles
        print("\n--- SECOND INNINGS ---")
    
    innings += 1

# Decide Winner
print(f"\n--- FINAL RUNS ---\nYour runs: {usr_score}\nComputer's runs: {comp_score}")
if usr_score > comp_score:
    print("\nRESULT: YOU WIN")
elif usr_score < comp_score:
    print("\nRESULT: YOU LOSE")
else:
    print("\nRESULT: IT'S A TIE")
