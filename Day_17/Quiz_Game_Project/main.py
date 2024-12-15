from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    currrent_question = Question(question['text'], question['answer'])
    question_bank.append(currrent_question)

quiz = QuizBrain(question_bank)

quiz.start_quiz()
