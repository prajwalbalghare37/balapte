# Generated by Django 3.2.5 on 2021-07-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='बाळासाहेब आपटे', max_length=1000)),
                ('author', models.CharField(default='', max_length=37)),
                ('image', models.ImageField(upload_to='allImages')),
                ('Content', models.CharField(default='बाळासाहेब आपटे', max_length=10000)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]