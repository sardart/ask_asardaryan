from django.db.models import Manager


class QuestionManager(Manager):

    def hot(self):
        return self.filter(is_active=True).order_by('-rating').prefetch_related()

    def by_tag(self, tag):
        return self.filter(is_active=True).filter(tags__title=tag).prefetch_related()
