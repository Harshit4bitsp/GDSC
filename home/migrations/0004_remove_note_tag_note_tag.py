# Generated by Django 4.0.5 on 2022-06-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_note_tag_note_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='tag',
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
    ]
