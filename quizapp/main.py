from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = Question(i["text"], i["answer"])
    question_bank.append(question_text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"quiz completed! your final score was {quiz.score}/{len(question_bank)}")

