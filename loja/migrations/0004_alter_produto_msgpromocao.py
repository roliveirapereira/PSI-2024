# Generated by Django 4.2.7 on 2024-08-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_image_alter_produto_msgpromocao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='msgPromocao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
