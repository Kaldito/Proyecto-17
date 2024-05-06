# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# ------------ CREACION DEL QUESTION BANK ------------ #
question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']

    new_question = Question(text=q_text, answer=q_answer)

    question_bank.append(new_question)

# ------------ MAIN ------------ #
quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('Quiz terminado')
