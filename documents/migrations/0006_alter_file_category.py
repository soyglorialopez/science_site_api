# Generated by Django 4.1.3 on 2022-11-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_alter_file_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='files', to='documents.category'),
        ),
    ]
