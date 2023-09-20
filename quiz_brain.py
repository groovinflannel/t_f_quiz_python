import data


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        input(f"{self.question_number}: {current_q.text} Type True or False and press Enter. ")

    def still_has_questions(self):
        num_of_questions = len(data.question_data)
        return self.question_number == num_of_questions
