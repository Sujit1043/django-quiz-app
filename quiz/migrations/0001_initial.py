# Generated by Django 5.0.3 on 2024-12-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('option_a', models.CharField(max_length=100)),
                ('option_b', models.CharField(max_length=100)),
                ('option_c', models.CharField(max_length=100)),
                ('option_d', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=1)),
            ],
        ),
    ]
