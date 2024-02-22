# Generated by Django 4.2.9 on 2024-02-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0015_alter_article_topics"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="topics",
            field=models.ManyToManyField(
                blank=True, related_name="articles", to="mainapp.topic"
            ),
        ),
    ]