def greetings(bot_name, birth_year):  # prints greetings with preloaded name and bot's birth year
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')
    remind_name()


def remind_name():  # prints username
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')
    guess_age()


def guess_age():  # guesses age by remainders
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder_3 = int(input())
    remainder_5 = int(input())
    remainder_7 = int(input())
    age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")
    count()


def count():  # counts to number from the input
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1
    test()


def test():  # prints a test to solve
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
        1. To repeat a statement multiple times.
        2. To decompose a program into several small subroutines.
        3. To determine the execution time of a program.
        4. To interrupt the execution of a program.""")
    while True:
        if int(input()) == 2:
            print('Completed, have a nice day!')
            break
        else:
            print("Try again")
    end()


def end():  # ends the program
    print('Congratulations, have a nice day!')


greetings('Aid', '2020')
