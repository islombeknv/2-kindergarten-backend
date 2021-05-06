from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from image_cropping import ImageRatioField

from main.validators import staff_picture, clean_picture, news_picture


class StaffModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff', validators=[staff_picture])
    cropping = ImageRatioField('image', '720x480', free_crop=True)
    position = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery', validators=[clean_picture])
    cropping = ImageRatioField('image', '720x480', free_crop=True)
    text = models.CharField(max_length=50,)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'


class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news', validators=[news_picture])
    cropping = ImageRatioField('image', '720x480', free_crop=True)
    description = models.TextField(max_length=250, null=True)
    content = RichTextUploadingField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners')
    text = models.CharField(max_length=512, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
