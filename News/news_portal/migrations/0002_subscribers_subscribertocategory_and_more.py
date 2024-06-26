# Generated by Django 5.0.6 on 2024-05-31 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberToCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_portal.category')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_portal.subscribers')),
            ],
        ),
        migrations.AddField(
            model_name='subscribers',
            name='category',
            field=models.ManyToManyField(through='news_portal.SubscriberToCategory', to='news_portal.category'),
        ),
    ]
