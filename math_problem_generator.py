#! Python3
# math_problem_generator.py - Randomly generate elementary math problem
import random

if __name__ == "__main__":
    quiz_file = open("Test.txt", 'w')

    # put the operators into a list so that can choose one randomly
    operators = ["+", "-", "*", "/"]
    quiz_file.write("If the answer is infinite, your answer should retain two decimal places\n")

    # Randomly generate 5 questions
    for question_list in range(5):
        int_list = []
        fraction_list = []
        decimal_list = []

        # randomly generate 3 integers for the arithmetic
        for i in range(3):
            random_int = random.randint(0, 100)
            int_list.append(random_int)

        # randomly generate 3 fraction numbers for the arithmetic
        for i in range(3):
            fraction_first_number = random.randint(1, 9)
            fraction_second_number = random.randint(2, 9)
            while fraction_first_number % fraction_second_number == 0 or \
                    fraction_second_number % fraction_first_number == 0:
                fraction_first_number = random.randint(1, 9)
                fraction_second_number = random.randint(2, 9)
            random_fraction = "(" + str(fraction_first_number) + "/" + str(fraction_second_number) + ")"
            fraction_list.append(random_fraction)

        # randomly generate 3 decimal numbers for the arithmetic
        for i in range(3):
            random_decimal = round(random.random() * 10, 1)
            decimal_list.append(random_decimal)

        # randomly choose numbers from integer, fraction, decimal
        number_list = []
        for i in range(3):
            number = random.choice([int_list[i], fraction_list[i], decimal_list[i]])
            number_list.append(number)

        # define two types of the questions
        problem1 = str(number_list[0]) + " " + operators[random.randint(0, 3)] + " " + str(number_list[1])
        problem2 = (str(number_list[0]) + " " + operators[random.randint(0, 3)] + " " + str(number_list[1]) + " "
                    + operators[random.randint(0, 3)] + " " + str(number_list[2]))
        problem = random.choice([problem1, problem2])  # randomly choose one type of the questions
        quiz_file.write("Question " + str(question_list + 1) + ": " + problem + " = \n")

    quiz_file.close()
