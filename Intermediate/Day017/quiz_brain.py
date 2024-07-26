from question_model import Question
import random


class QuizBrain:
    """
    Specs for this had the program just going through the questions in the list from start to finish. I added a random
    element, and ensuring the question had not been asked before.
    """
    questions_list: list[Question] = []
    question_number: int = 0
    question_id: int = 0
    questions_asked: list[int] = []
    questions_asked_count: int = 0
    guess: str = ""
    score: int = 0

    def __init__(self, question_list: list[Question]):
        self.questions_list = question_list
        self.question_number = 0

    def ask_question(self, question: Question) -> None:
        print("Asking question")
        self.guess = input(f"Q-{self.question_number}: {question.question_text} (True/False): ").title()

    def next_question(self) -> None:
        question_id = random.randint(0, len(self.questions_list) - 1)
        already_asked: bool = (question_id in self.questions_asked)

        while already_asked:
            question_id = random.randint(0, len(self.questions_list) - 1)
            if question_id in self.questions_asked:
                already_asked = True
            else:
                already_asked = False

        self.questions_asked.append(question_id)
        self.question_number += 1
        self.questions_asked_count += 1
        question: Question = self.questions_list[question_id]

        self.ask_question(question)
        self.check_answer(question)
        print(f"Your current score: {self.score}/{len(self.questions_asked)}")

    def still_has_questions(self) -> bool:
        return len(self.questions_list) != len(self.questions_asked)

    def check_answer(self, question: Question) -> None:
        # question: Question = self.questions_list[self.question_id]
        if self.guess == question.question_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")