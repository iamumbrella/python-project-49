import random
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def your_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even_number(num):
    return num % 2 == 0


def your_answer(answer, num):
    if is_even_number(num) is True and answer == "yes":
        return True
    elif is_even_number(num) is False and answer == "no":
        return True


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        is_even = is_even_number(num)
        if (is_even and answer == "yes") or (not is_even and answer == "no"):
            print('Correct!')
        else:
            correct_answer = "yes" if is_even else "no"
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            return f"Let's try again, {name}!"  # Передаем name в строке возврата
    return f"Congratulations, {name}!"


def main():
    welcome()
    print(game(your_name()))


if __name__ == '__main__':
    main()

