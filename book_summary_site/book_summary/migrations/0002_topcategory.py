# Generated by Django 2.2.1 on 2019-06-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_summary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='トップカテゴリ名')),
            ],
        ),
    ]
