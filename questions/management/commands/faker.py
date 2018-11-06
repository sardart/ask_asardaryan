import random
from questions.models import Question, Tag, User
from faker import Faker
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    users_count = 100
    questions_count = 200
    tags_count = 10
    faker = Faker()

    def handle(self, *args, **options):
        self.tags = self.generate_tags()
        self.users = self.generate_users()
        self.questions = self.generate_questions()

        message = "Successfully generated %s questions, %s users, %s tags" % (len(self.questions), len(self.users), len(self.tags))
        self.stdout.write(self.style.SUCCESS(message))

    def generate_users(self):
        users = []
        for _ in range(self.users_count):
            user = User.objects.create(username=self.faker.name())
            user.save()
            users.append(user)

        return users

    def generate_tags(self):
        tags = []
        for i in range(self.tags_count):
            tag = Tag.objects.create(title=self.faker.word())
            tag.save()
            tags.append(tag)

        return tags

    def generate_questions(self):
        questions = []
        for i in range(self.questions_count):
            question = Question.objects.create(title=self.faker.sentence(),
                                text=self.faker.text(),
                                author=random.choice(self.users),
                                rating=random.randint(-50, 50),
                                answers_count=random.randint(0, 30))

            tags = set()
            for _ in range(random.randint(1, 3)):
                tags.add(random.choice(self.tags))

            question.tags.add(*tags)

            question.save()
            questions.append(question)

        return questions


