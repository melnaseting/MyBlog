# Generated by Django 5.1.3 on 2024-12-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_coment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coment',
        ),
        migrations.AddField(
            model_name='post',
            name='coment',
            field=models.ManyToManyField(blank=True, null=True, to='blog.coment'),
        ),
    ]
