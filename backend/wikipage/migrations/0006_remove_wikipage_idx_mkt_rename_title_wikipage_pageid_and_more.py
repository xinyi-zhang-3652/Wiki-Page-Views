# Generated by Django 4.2.7 on 2023-11-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipage', '0005_remove_wikipage_idx_date_title_remove_wikipage_date_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='wikipage',
            name='idx_MKT',
        ),
        migrations.RenameField(
            model_name='wikipage',
            old_name='title',
            new_name='pageid',
        ),
        migrations.AddIndex(
            model_name='wikipage',
            index=models.Index(fields=['month', 'keyword', 'pageid'], name='idx_MKT'),
        ),
    ]