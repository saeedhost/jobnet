# Generated by Django 4.1.1 on 2023-03-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostJobData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=255)),
                ('job_location', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('job_des', models.TextField()),
                ('job_image', models.ImageField(upload_to='user_uploaded_imgs')),
            ],
        ),
    ]