import random

if __name__ == "__main__":
    quiz_file = open("Test.txt", 'w')

    operators = ["+", "-", "*", "/"]
    quiz_file.write("If the answer is infinite, your answer should retain two decimal places\n")
    for question_list in range(5):
        int_list = []
        for i in range(3):
            random_int = random.randint(0, 100)
            int_list.append(random_int)

        fraction_list = []
        for i in range(3):
            fraction_first_number = random.randint(1, 9)
            fraction_second_number = random.randint(2, 9)
            while fraction_first_number % fraction_second_number == 0:
                fraction_first_number = random.randint(1, 9)
                fraction_second_number = random.randint(2, 9)
            random_fraction = "(" + str(fraction_first_number) + "/" + str(fraction_second_number) + ")"
            fraction_list.append(random_fraction)

        decimal_list = []
        for i in range(3):
            random_decimal = round(random.random() * 10, 1)
            decimal_list.append(random_decimal)

        number_list = []
        for i in range(3):
            number = random.choice([int_list[i], fraction_list[i], decimal_list[i]])
            number_list.append(number)

        problem1 = str(number_list[0]) + " " + operators[random.randint(0, 3)] + " " + str(number_list[1])
        problem2 = (str(number_list[0]) + " " + operators[random.randint(0, 3)] + " " + str(number_list[1]) + " "
                    + operators[random.randint(0, 3)] + " " + str(number_list[2]))
        problem = random.choice([problem1, problem2])
        quiz_file.write("Question " + str(question_list + 1) + ": " + problem + " = \n")

    quiz_file.close()