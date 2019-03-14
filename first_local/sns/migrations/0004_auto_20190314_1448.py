# Generated by Django 2.1.7 on 2019-03-14 14:48

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='postings/resize/%Y%m%d'),
        ),
    ]
