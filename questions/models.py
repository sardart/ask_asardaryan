from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from questions.managers import QuestionManager


class User(AbstractUser):
    upload = models.ImageField(upload_to='upload/%Y/%m/%d')


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")
    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    tags = models.ManyToManyField(Tag, blank=True, related_name="questions")
    rating = models.IntegerField(default=0)
    # comments_count = models.IntegerField(default=0)
    objects = QuestionManager()

    def comments_count(self):
       return self.comment_set.count()

    def __str__(self):
        return self.title

    def like(self, user, is_liked):
        try:
            like = self.questionlike_set.get(author=user)
            if like.is_liked is not is_liked:
                like.is_liked = is_liked
        except QuestionLike.DoesNotExist:
            like = QuestionLike.objects.create(author=user, is_liked=is_liked, question=self)

        if like.is_liked:
            self.rating += 1
        else:
            self.rating -= 1

        like.save()
        self.save()

    class Meta:
        ordering = ['-create_date']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_data = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания комментария")
    text = models.TextField(blank=True, verbose_name=u"Комментарий")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def like(self,  user, is_liked):
        try:
            like = self.commentlike_set.get(author=user)
            if like.is_liked is not is_liked:
                like.is_liked = is_liked
        except CommentLike.DoesNotExist:
            like = CommentLike.objects.create(author=user, is_liked=is_liked, comment=self)

        if like.is_liked:
            self.rating += 1
        else:
            self.rating -= 1

        like.save()
        self.save()


class CommentLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class QuestionLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

