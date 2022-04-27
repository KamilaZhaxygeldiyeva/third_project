# Generated by Django 4.0.3 on 2022-03-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('text', models.TextField(verbose_name='text')),
                ('date_at', models.DateTimeField(verbose_name='publication date')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'New',
            },
        ),
    ]