from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import QuizzUI

question_bank = []
for question in get_questions():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

ui = QuizzUI(quiz)

