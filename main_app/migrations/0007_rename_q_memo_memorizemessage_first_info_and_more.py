# Generated by Django 4.1.1 on 2022-10-16 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_memorizemessage_message_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memorizemessage',
            old_name='q_memo',
            new_name='first_info',
        ),
        migrations.RenameField(
            model_name='memorizemessage',
            old_name='q_memo_before_edit',
            new_name='second_info',
        ),
    ]