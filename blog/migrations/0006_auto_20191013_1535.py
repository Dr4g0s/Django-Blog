# Generated by Django 2.2.4 on 2019-10-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]