# Generated by Django 2.2 on 2019-05-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descriprion',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]