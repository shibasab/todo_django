# Generated by Django 2.2.3 on 2019-07-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20190720_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='achivement',
            field=models.IntegerField(blank=True, null=True, verbose_name='達成度'),
        ),
    ]