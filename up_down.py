import random


def replay():
    while True:
        reply = input("Do you want to REPLAY? (y/n): ").lower()
        if reply == "y" or reply == "n":
            return reply


def up_down():
    best_attempts = 0
    while True:
        print(f"Your Best Attempts: {best_attempts}")
        random_number = random.randint(1, 100)
        attempts = 0
        while True:
            while True:
                user_number = input('Enter number: ')
                if user_number.isdecimal():
                    user_number = int(user_number)
                    if 1 <= user_number <= 100:
                        break
                print("Please enter an integer between 1 and 100.")
            attempts += 1

            if random_number > user_number:
                print("Up!")
            elif random_number < user_number:
                print("Down!")
            else:
                print("Bingo!")
                print(f"Your attempts: {attempts}")
                if best_attempts < attempts:
                    best_attempts = attempts

                reply = replay()
                if reply == "y":
                    break  # 함수 재실행
                elif reply == "n":
                    return  # 함수 종료


up_down()
