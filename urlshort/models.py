from django.db import models


class ShortUrl(models.Model):
    url = models.URLField(unique=True)
    urlhash = models.CharField(max_length=40, unique=True)
    shortlink = models.CharField(max_length=400)

    clicks = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url}:\n' \
            f'shortlink: {self.shortlink}\n' \
            f'urlhash: {self.urlhash}\n'
