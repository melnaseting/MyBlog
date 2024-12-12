# Generated by Django 5.1.3 on 2024-12-11 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_coment_post_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coment',
        ),
        migrations.AddField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
