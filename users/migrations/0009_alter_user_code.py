# Generated by Django 5.0 on 2024-01-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default='170371755210', max_length=50, null=True, verbose_name='проверочный код'),
        ),
    ]
