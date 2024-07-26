class Question:
    question_text: str
    question_answer: bool

    def __init__(self, q_text: str, q_answer: bool):
        self.question_text = q_text
        self.question_answer = q_answer

    def __str__(self):
        return f"Question Text: {self.question_text}\nAnswer: {self.question_answer}\n"


if __name__ == "__main__":
    pass
