# Generated by Django 5.0 on 2024-01-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_code_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='911366661832', max_length=50, null=True, verbose_name='проверочный код'),
        ),
    ]
