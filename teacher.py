# from pywebio.input import *
# from pywebio.output import *

# def teacher():
#     put_text("Add Exam Here Q/A")

#     ques = input("Add Question herre")
#     ans = input("Add answer here")



# teacher()

from pywebio.input import *
from pywebio.output import *
import json

def create_exam():
    exam_data = {}

    exam_name = input("Enter Exam Name:", type="text")
    exam_data['exam_name'] = exam_name

    questions = []
    while len(questions) < 10:
        question_text = input("Enter Question:", type="text")
        question_type = select("Select Question Type:", ['Multiple Choice', 'Text'])

        if question_type == "Multiple Choice" or question_type == "Single Choice":
            choices = []
            choice_count = input("Enter the number of choices:", type="number", value=4)
            for _ in range(choice_count):
                choice = input(f"Enter Choice {_ + 1}:", type="text")
                choices.append(choice)
            correct_choice = select("Select Correct Choice:", choices)
            questions.append({
                "type": question_type,
                "question": question_text,
                "choices": choices,
                "correct_choice": correct_choice
            })
        else:
            questions.append({
                "type": question_type,
                "question": question_text
            })

            more_questions = checkbox("Add another question?", options=['No']) 
            if not more_questions:
                break

    exam_data['questions'] = questions

    duration = input("Add Duration in min.:", type="number")
    exam_data['duration'] = duration
    with open('exam_data.json', 'w') as file:
        json.dump(exam_data, file, indent=4)

    put_text("Exam created successfully!")

if __name__ == '__main__':
    create_exam()
