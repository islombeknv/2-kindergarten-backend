# Generated by Django 3.2 on 2021-04-27 04:19

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannermodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='gallerymodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='gallerymodel',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
