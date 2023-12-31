# Generated by Django 5.0 on 2023-12-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_about_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='cv',
        ),
        migrations.AddField(
            model_name='about',
            name='pdf_file',
            field=models.FileField(default='default_cv.pdf', upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
