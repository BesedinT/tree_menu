from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True, related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
