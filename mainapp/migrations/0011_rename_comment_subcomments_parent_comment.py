# Generated by Django 4.2.9 on 2024-02-20 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0010_article_downvotes_article_total_votes_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subcomments", old_name="comment", new_name="parent_comment",
        ),
    ]