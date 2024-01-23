# Generated by Django 3.2.4 on 2021-06-30 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category_name', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Food categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(default='', max_length=50)),
                ('image', models.CharField(default='', max_length=2000)),
                ('prep_time', models.CharField(default='', max_length=40)),
                ('cook_time', models.CharField(default='', max_length=40)),
                ('servings', models.CharField(default='', max_length=3)),
                ('recipe_description', models.CharField(blank=True, default='', max_length=500)),
                ('ingredients_text', models.TextField(default='')),
                ('recipe_steps', models.TextField(default='')),
                ('recipe_notes', models.TextField(blank=True, default='')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(default='', max_length=150, unique=True)),
                ('approval', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.course')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.cuisine')),
                ('food_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.food_category')),
            ],
            options={
                'verbose_name_plural': 'Recipes',
            },
        ),
    ]
