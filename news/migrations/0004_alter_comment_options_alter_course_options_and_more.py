# Generated by Django 4.0.3 on 2022-04-07 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_at', 'username'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарийлер'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курстар'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['date_at', 'name'], 'verbose_name': 'Жаңалық', 'verbose_name_plural': 'Жаңалықтар'},
        ),
    ]
