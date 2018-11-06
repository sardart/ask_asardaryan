import random
from questions.models import Question, Tag, User, Comment
from faker import Faker
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    users_count = 100
    questions_count = 100
    tags_count = 10
    comments_count = 200
    questions_likes_count = int(users_count * questions_count / 4)
    comments_likes_count = int(users_count * comments_count / 8)

    faker = Faker()

    def handle(self, *args, **options):
        self.tags = self.generate_tags()
        self.users = self.generate_users()
        self.questions = self.generate_questions()
        self.comments = self.generate_comments()
        self.generate_likes()

        message = "Successfully generated %s questions, %s users, %s tags" % (len(self.questions), len(self.users), len(self.tags))
        self.stdout.write(self.style.SUCCESS(message))

    def generate_users(self):
        users = []

        for _ in range(self.users_count):
            username = self.faker.name() + " " + self.faker.word()
            user = User.objects.create(username=username)
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
                                rating=random.randint(-50, 50))
            tags = set()
            for _ in range(random.randint(1, 3)):
                tags.add(random.choice(self.tags))

            question.tags.add(*tags)

            question.save()
            questions.append(question)

        return questions

    def generate_comments(self):
        comments = []

        for _ in range(self.comments_count):
            question = random.choice(self.questions)
            user = random.choice(self.users)
            comment = Comment.objects.create(question=question,
                                             author=user,
                                             text=self.faker.sentence())
            comment.save()
            comments.append(comment)

        return comments

    def generate_likes(self):
        for _ in range(self.questions_likes_count):
            question = random.choice(self.questions)
            user = random.choice(self.users)
            is_liked = random.choice([True, False])
            question.like(is_liked=is_liked, user=user)

        for _ in range(self.comments_likes_count):
            comment = random.choice(self.comments)
            user = random.choice(self.users)
            is_liked = random.choice([True, False])
            comment.like(is_liked=is_liked, user=user)




