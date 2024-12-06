# Generated by Django 5.1.3 on 2024-12-06 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content_alter_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
