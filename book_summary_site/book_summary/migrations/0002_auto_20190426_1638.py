# Generated by Django 2.0.13 on 2019-04-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
