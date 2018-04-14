import random


if __name__ == "__main__":
    quiz_file = open("Test.txt", 'w')

    operators = ["+", "-", "*", "/"]
    quiz_file.write("If the answer is infinite, your answer should retain two decimal places\n")
    for question_list in range(5):
        int_1 = random.randint(0, 100)
        int_2 = random.randint(0, 100)
        int_3 = random.randint(0, 100)

        fraction_first_number = random.randint(1, 9)
        fraction_second_number = random.randint(2, 9)
        while fraction_first_number % fraction_second_number == 0:
            fraction_first_number = random.randint(1, 9)
            fraction_second_number = random.randint(2, 9)
        fraction_1 = "(" + str(fraction_first_number) + "/" + str(fraction_second_number) + ")"

        fraction_first_number = random.randint(1, 9)
        fraction_second_number = random.randint(2, 9)
        while fraction_first_number % fraction_second_number == 0:
            fraction_first_number = random.randint(1, 9)
            fraction_second_number = random.randint(2, 9)
        fraction_2 = "(" + str(fraction_first_number) + "/" + str(fraction_second_number) + ")"

        fraction_first_number = random.randint(1, 9)
        fraction_second_number = random.randint(2, 9)
        while fraction_first_number % fraction_second_number == 0:
            fraction_first_number = random.randint(1, 9)
            fraction_second_number = random.randint(2, 9)
        fraction_3 = "(" + str(fraction_first_number) + "/" + str(fraction_second_number) + ")"

        fix_point_1 = round(random.random() * 10, 1)
        fix_point_2 = round(random.random() * 10, 1)
        fix_point_3 = round(random.random() * 10, 1)

        number_1 = random.choice([fraction_1, int_1, fix_point_1])
        number_2 = random.choice([fraction_2, int_2, fix_point_2])
        number_3 = random.choice([fraction_3, int_3, fix_point_3])

        problem1 = str(number_1) + " " + operators[random.randint(0, 3)] + " " + str(number_2)
        problem2 = (str(number_1) + " " + operators[random.randint(0, 3)] + " " + str(number_2) + " "
                    + operators[random.randint(0, 3)] + " " + str(number_3))
        problem = random.choice([problem1, problem2])
        quiz_file.write("Question " + str(question_list + 1) + ": " + problem + " = \n")

    quiz_file.close()
