from django.db import models
from django.urls import reverse

class Film(models.Model):
    filmName = models.CharField(max_length= 255,verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    duration = models.CharField(max_length=20,verbose_name='Продолжительность фильма')
    prewiew = models.ImageField(upload_to='imggg',blank=True)
    created_at = models.IntegerField(verbose_name='Год выпуска')
    country = models.CharField(max_length=100,verbose_name='Страна')
    rating = models.IntegerField(default=0,verbose_name='Рейтинг')
    file = models.FileField(upload_to='videos', blank=True, null=True)
    is_for_subscriber = models.BooleanField(default=False,verbose_name='По подписке')
    category = models.ManyToManyField('Category',verbose_name='Категория',null=True,)

    def get_absolute_url(self):
        return reverse('watch', kwargs={'film_id': self.pk})

    def get_categories(self):
        return  " %s" % (", ".join([cat.title for cat in self.category.all()]))
    get_categories.short_description = 'Жанр'

    def __str__(self):
        return self.filmName

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'