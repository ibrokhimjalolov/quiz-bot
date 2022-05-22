import tempfile
import os
from bot.utils.db_api.django_db_api.core.models import (
    Question, Option, GeneratedTestQuestions, GeneratedTest
)

TEMPLATE = """
%(index)s. %(question)s
A) %(A)s
B) %(B)s
C) %(C)s
D) %(D)s
"""


class TestGenerator:

    def __init__(self, user_id):
        self.temp_file = tempfile.mktemp(suffix='.txt')
        self.temp_file_pdf = tempfile.mktemp(suffix='.pdf')
        self.answer = ''
        self.generated_test = GeneratedTest.objects.create(
            user_id=user_id
        )
        self.generate()
        self.convert2pdf()

    def get_generated_file_path(self):
        return self.temp_file_pdf

    @staticmethod
    def get_questions_number():
        return 30

    def generate(self):
        with open(self.temp_file, 'w') as f:
            f.write(
                f"Test kodi {self.generated_test.id}\n"
            )
            f.write(
                f"Natijangizni @test_master_english_bot bot orqali bilishingiz mumkin. Omad!\n\n"
            )
            questions = self.get_questions()
            for index, question in enumerate(questions):
                GeneratedTestQuestions.objects.create(
                    test=self.generated_test,
                    question=question,
                    order=index+1
                )
                f.write(
                    TEMPLATE % dict(**{'index': index + 1, 'question': question.content}, **question.options_asdict())
                )
                # f.write(
                #     ''
                # )

    def get_questions(self):
        return Question.objects.all().order_by('?')[:self.get_questions_number()]

    def convert2pdf(self):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=9)
        with open(self.temp_file, 'r') as f:
            for index, line in enumerate(f.readlines()):
                pdf.cell(200, 10, txt=line,
                         ln=index+1)
        pdf.output(self.temp_file_pdf)


class TestChecker:
    def __init__(self, txt, user_id):
        self.score = -1
        self.user_id = user_id
        a = txt.split()
        self.code = -1
        self.keys = ''
        if len(a) != 2 or not len(a[1]) != 30:
            return
        self.code = a[0]
        self.keys = a[1]

    def get_score(self):
        try:
            test = GeneratedTest.objects.filter(user_id=self.user_id, id=int(self.code)).first()
            if not test:
                return -1
            index = 1
            wrong = 0
            options = test.questions.all()
            for index, question in enumerate(options):
                if question.question.get_answer_label() != self.keys[index].upper():
                    wrong += 1
            return 30 - wrong
        except ValueError:
            return -1

