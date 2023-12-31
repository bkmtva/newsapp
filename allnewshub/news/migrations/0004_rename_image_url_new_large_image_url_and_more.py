# Generated by Django 4.2.4 on 2023-08-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='image_url',
            new_name='large_image_url',
        ),
        migrations.AddField(
            model_name='new',
            name='small_image_url',
            field=models.URLField(null=True),
        ),
    ]
