from django.db import models

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=50, verbose_name='название')
    descrition = models.TextField(verbose_name='описпние')
    image = models.ImageField(upload_to='img/post/', verbose_name='фото', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'дата')
    category = models.ForeignKey('post.Category', on_delete = models.SET_NULL, verbose_name = 'катагория', null=True)
    count_like = models.PositiveIntegerField(verbose_name = 'лайки', default=0)
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self) -> str:
        return f'Название пота {self.title}, Опублековано {self.created.date()}'


class Category(models.Model):
    """Model definition for Category."""
    title = models.CharField(max_length = 25, verbose_name='название')
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.title}'