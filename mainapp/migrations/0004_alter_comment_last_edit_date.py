# Generated by Django 4.1.7 on 2023-12-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_article_last_edit_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="last_edit_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
