# Generated by Django 5.0 on 2024-01-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='332831731345', max_length=50, null=True, verbose_name='проверочный код'),
        ),
    ]
