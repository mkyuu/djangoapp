# Generated by Django 2.2.1 on 2019-06-08 03:10

import book_summary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='著者名')),
            ],
        ),
        migrations.CreateModel(
            name='BigCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('summary', models.TextField(verbose_name='要約')),
                ('img', models.URLField(blank=True, verbose_name='画像url')),
                ('link', models.URLField(blank=True, verbose_name='Amazonリンク')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='公開日')),
                ('author', models.ForeignKey(blank=True, default=book_summary.models.set_default_author, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.Author')),
                ('bigcategory', models.ForeignKey(blank=True, default=book_summary.models.set_default_bigcategory, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.BigCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='出版社名')),
                ('author', models.ForeignKey(default=book_summary.models.set_default_author, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_summary.Book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='名無しさん', max_length=200, verbose_name='投稿者')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='公開日')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_summary.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ジャンル名')),
                ('bigcategory', models.ForeignKey(default=book_summary.models.set_default_bigcategory, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.BigCategory', verbose_name='カテゴリ名')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, default=book_summary.models.set_default_category, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.Category', verbose_name='ジャンル'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default=book_summary.models.set_default_publisher, on_delete=django.db.models.deletion.SET_DEFAULT, to='book_summary.Publisher', verbose_name='出版社'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
