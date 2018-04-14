if __name__ == "__main__":
    score = 0
    quiz_file = open('Test.txt')
    report_file = open("Report.txt", 'w')

    question_list = quiz_file.readlines()

    report_file.write("Here is your score : \n")

    for index in range(len(question_list)):
        question = question_list[index]
        if question[0:8] == "Question":
            equal_sign = question.find("=")
            user_answer = 0
            try:
                user_answer = float(question[equal_sign+1:].strip())
                answer = 0
                exec("answer = " + question[12:equal_sign-1].rstrip())
                if round(answer, 2) == user_answer:
                    report_file.write("Problem " + str(index) + ": CORRECT\n")
                    score = score + 1
                else:
                    report_file.write("Problem " + str(index) + ": WRONG\n")
            except ValueError:
                report_file.write("Problem " + str(index) + ": Please enter your answer!\n")
    report_file.write("Your score is : " + str(score))

    quiz_file.close()
    report_file.close()
