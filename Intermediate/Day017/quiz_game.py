import os
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from functools import cache
import atexit

# TODO: Enhance to pull questions from OpenTriviaDatabase - This is a RESTful API that returns JSON
# https://opentdb.com/api_config.php

@atexit.register
def exit_handler() -> None:
    # clean up any resources before exiting
    print("Thank you for playing!")


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


@cache
def init_question_bank() -> list:
    bank: list[Question] = []
    for q in question_data:
        question: Question = Question(q["text"], q["answer"])
        bank.append(question)
    return bank


def main() -> None:
    still_playing: bool = True
    question_bank: list[Question] = init_question_bank()
    # print(init_question_bank.cache_info())
    quiz_brain: QuizBrain = QuizBrain(question_bank)
    cls()

    while still_playing:
        quiz_brain.next_question()
        still_playing = quiz_brain.still_has_questions() and not quiz_brain.guess.upper() == 'QUIT'
        print()
    print(f"Your final score was {quiz_brain.score}/{quiz_brain.questions_asked_count}")


if __name__ == '__main__':
    main()
