from pywebio.input import *
from pywebio.output import *
from datetime import datetime, timedelta
from flask import Flask
# from timer import start_min_timer
import time

# from timer import start_timer,countdown_timer

# def countdown_timer(duration):
#     start_time = time.time()
#     end_time = start_time + duration

#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes, seconds = divmod(remaining_time, 60)
#         time_str = f"Time Left: {minutes:02d}:{seconds:02d}"
#         clear()  # Clear previous output
#         put_text(time_str)
#         time.sleep(1)
    
#     clear()
#     put_text("Time's up!")

# def start_timer():
#     countdown_duration = 180  # 3 minutes in seconds
#     countdown_timer(countdown_duration)

# if __name__ == '__main__':
#     start_timer()









app = Flask(__name__)
    


def exam(questions,exam_duration):
    c = 0
    name = input("Enter your name to start the Exam: ", type="text")
    end_time = time.time() + exam_duration * 60
    remaining_time = int(end_time - time.time())
    minutes, seconds = divmod(remaining_time, 60)
    time_str = f"Time Duration: {minutes:02d}:{seconds:02d}"
    put_text(time_str)
    
    for i, question in enumerate(questions, start=1):
        if(time.time() > end_time):
            put_text('Time up!')
            break
        q = radio(f"Question {i}: {question['question']}", question['choices'])
        if q == question['correct_choice']:
            c += 1    

    put_text(f"{name}, your score is {c}")
    if c > len(questions) / 2:

        put_text("Result: Passed")
    else:
        put_text("Result: Failed")

    put_text("Thanks for Participating!")

def take_exam():
        import json
        print("nn mnvbjkfvekldvsdv")
        with open('exam_data.json') as file:
            exam_data = json.load(file)
            questions = exam_data.get('questions', [])
            exam_duration = exam_data.get('duration', 60) 

        exam(questions, exam_duration)
if __name__ == '__main__':
    take_exam()
    # start_timer()
