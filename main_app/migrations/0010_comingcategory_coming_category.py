# Generated by Django 4.1.1 on 2022-10-25 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_coming_coming_type_remove_coming_is_late_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الفئة')),
            ],
            options={
                'verbose_name': 'فئة الحضور',
                'verbose_name_plural': 'فئات الحضور',
            },
        ),
        migrations.AddField(
            model_name='coming',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.comingcategory', verbose_name='نوع الحضور'),
        ),
    ]