# Generated by Django 5.0.3 on 2024-03-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(max_length=100, null=True)),
                ('email', models.TextField(max_length=100, null=True)),
                ('password', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
