from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question ["correct_answer"]
    question_entry = Question(question_text, question_answer)
    question_bank.append(question_entry)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() is True:
    quiz.next_question()

print("You've completed the Quiz!")
print (f"Your final score is {quiz.score}/{quiz.question_number}")