# Generated by Django 2.2.3 on 2019-07-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='締め切り'),
        ),
    ]