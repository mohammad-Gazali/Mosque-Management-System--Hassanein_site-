# Generated by Django 4.1.1 on 2023-01-09 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_moneydeleting_remove_student_school_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointsadding',
            name='master_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.master', verbose_name='اسم الأستاذ'),
        ),
        migrations.AddField(
            model_name='pointsdeletings',
            name='master_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.master', verbose_name='اسم الأستاذ'),
        ),
        migrations.AlterField(
            model_name='coming',
            name='master_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.master', verbose_name='اسم الأستاذ'),
        ),
        migrations.AlterField(
            model_name='memorizemessage',
            name='master_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.master', verbose_name='اسم الأستاذ'),
        ),
        migrations.AlterField(
            model_name='memorizenotes',
            name='master_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.master', verbose_name='اسم الأستاذ'),
        ),
    ]