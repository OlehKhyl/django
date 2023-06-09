# Generated by Django 4.2 on 2023-04-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('anouns', models.CharField(max_length=250, verbose_name='Anouns')),
                ('full_text', models.TextField(verbose_name='News text')),
                ('date', models.DateTimeField(verbose_name='Publish date')),
            ],
        ),
    ]
