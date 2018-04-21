#! Python3
# math_problem_solver.py - Solve the problems in Test.txt and output the answers

if __name__ == "__main__":
    quiz_file = open('Test.txt')
    answer_file = open('Answer.txt', 'w')

    # read the questions from the Test.txt
    question_list = quiz_file.readlines()

    answer_file.write("Here are the answers : \n")

    for index in range(len(question_list)):
        question = question_list[index]
        answer = 0
        if question[0:8] == "Question":
            exec("answer = " + question[12:-3])  # directly solve the problem use Python's function exec
            Question = question[12:-3].rstrip()
            answer_file.write("Question " + str(index) + " : " + Question + " = " + str(round(answer, 2)) + '\n')

    quiz_file.close()
    answer_file.close()
