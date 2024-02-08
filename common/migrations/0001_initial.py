# Generated by Django 5.0.1 on 2024-01-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banner/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.TextField(blank=True)),
                ('degree', models.CharField(choices=[('BACHELOR', 'Bachelor'), ('master', 'Master')], default='BACHELOR', max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='result/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('characterization', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='review/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('social_name', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('student_count', models.PositiveBigIntegerField(default=0)),
                ('universities_count', models.PositiveBigIntegerField(default=21)),
                ('years_of_experienced', models.IntegerField()),
                ('countries_count', models.PositiveBigIntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
