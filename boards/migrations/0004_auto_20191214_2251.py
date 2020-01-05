# Generated by Django 2.2.8 on 2019-12-14 22:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20191214_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardfeed',
            name='index',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='name',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='boardfeed',
            name='created_at',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='boardfeed',
            name='refreshed_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='BoardBlock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512, null=True)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('index', models.PositiveIntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='boards.Board')),
            ],
            options={
                'db_table': 'board_blocks',
                'ordering': ['index'],
            },
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='block',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='boards.BoardBlock'),
            preserve_default=False,
        ),
    ]
