import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.utils.db_api.django_db_api.config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from bot.utils.db_api.django_db_api.core.models import Question, Option
import json


def make_save(txt):
    return ' '.join(txt.split())


c = 1

with open('./database1.json', 'r') as f:
    data = json.load(f)
    for d in data:
        question = Question.objects.create(
            content=make_save(d['fields']['question'])
        )
        options = {
            'A': make_save(d['fields']['A']),
            'B': make_save(d['fields']['B']),
            'C': make_save(d['fields']['C']),
            'D': make_save(d['fields']['D']),
        }
        for option in options:
            op = Option.objects.create(
                question=question,
                content=options[option],
                label=option,
                is_correct=bool(option == make_save(d['fields']['answer']))
            )
        print("Done", c)
        c += 1
