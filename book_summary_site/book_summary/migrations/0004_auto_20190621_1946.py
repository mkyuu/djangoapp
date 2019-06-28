# Generated by Django 2.1.7 on 2019-06-21 10:46

import book_summary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_summary', '0003_bigcategory_topcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bigcategory',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, default=book_summary.models.set_default_category, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.Category', verbose_name='ジャンル'),
        ),
    ]