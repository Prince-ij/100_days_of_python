class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def start_quiz(self):
        for question in self.question_list:
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
            self.check_answer(answer, question.answer)
        print("You've completed the quiz !")
        print(f"Your final score is: {self.score}/{self.question_number}\n\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("Sorry, that was not correct !")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
