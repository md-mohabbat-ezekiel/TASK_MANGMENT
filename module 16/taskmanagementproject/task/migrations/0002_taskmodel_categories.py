# Generated by Django 5.0 on 2023-12-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='category.taskcategory'),
        ),
    ]
