# Generated by Django 3.0.7 on 2020-06-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=10)),
                ('DateOfBirth', models.DateField()),
                ('About_me', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
