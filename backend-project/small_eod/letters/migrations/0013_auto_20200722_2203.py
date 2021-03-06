# Generated by Django 3.0.8 on 2020-07-22 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0012_auto_20200626_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date of sending or receiving.', verbose_name='Date'),
        ),
    ]
