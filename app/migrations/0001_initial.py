# Generated by Django 3.1.6 on 2021-02-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Image name')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image file')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
