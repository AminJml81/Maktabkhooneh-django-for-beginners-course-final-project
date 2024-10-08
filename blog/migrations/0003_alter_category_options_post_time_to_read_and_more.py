# Generated by Django 4.2.13 on 2024-07-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_category_post_image_alter_post_published_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.AddField(
            model_name="post",
            name="time_to_read",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(default="blog/default.jpg", upload_to="blog/"),
        ),
    ]
