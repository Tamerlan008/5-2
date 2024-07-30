from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    content = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    image = models.ImageField(upload_to='news', verbose_name='Фото')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'