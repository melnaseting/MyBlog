# Generated by Django 5.1.3 on 2024-12-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_coment_post_coment_author_post_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
