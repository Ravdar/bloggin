# Generated by Django 4.1.7 on 2023-12-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_article_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="last_edit_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]