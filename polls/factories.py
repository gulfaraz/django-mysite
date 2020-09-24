import factory

from .models import Question, Choice


class QuestionFactory(factory.django.DjangoModelFactory):
    question_text = factory.Faker("sentence")
    pub_date = factory.Faker("date_time")

    class Meta:
        model = Question


class ChoiceFactory(factory.django.DjangoModelFactory):
    question = factory.SubFactory(QuestionFactory)
    choice_text = factory.Faker("sentence")
    votes = factory.Faker("pyint")

    class Meta:
        model = Choice
