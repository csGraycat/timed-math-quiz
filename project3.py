#  timed math quiz
import random
from project1.utils import int_input
import time


def main():
    task_len = int_input("Number of questions: ")

    while True:
        difficulties = ['e', 'm', 'h']
        print("Select difficulty: [e]asy, [m]edium or [h]ard")
        difficulty = input()
        if difficulty in difficulties:
            break

    start_time = time.time()

    match difficulty:
        case 'e':
            operations = ['+', '-']
            nums_len = 2
            generate_quiz(task_len, nums_len, operations, 10, 99)

        case 'm':
            operations = ['+', '-', '*']
            nums_len = 3
            generate_quiz(task_len, nums_len, operations, 10, 99)

        case 'h':
            operations = ['+', '-', '*']
            nums_len = 3
            generate_quiz(task_len, nums_len, operations, 100, 999)

    end_time = time.time()
    time_lapsed = end_time - start_time
    print("Quiz completed in: ")
    print("%.2f" % time_lapsed + ' seconds')


def generate_quiz(task_len, nums_len, operations, rand_a, rand_b):
    for _ in range(task_len):
        task = ''
        for _ in range(nums_len):
            task += str(random.randint(rand_a, rand_b)) + ' ' + random.choice(operations) + ' '
        task = task[:-2]
        print(task)
        ans = int_input("Answer: ")
        while ans != eval(task):
            print('Incorrect')
            ans = int_input("Answer: ")
        print('Correct!')


main()