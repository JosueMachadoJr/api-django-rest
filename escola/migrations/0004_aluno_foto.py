# Generated by Django 5.0.6 on 2024-06-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_aluno_id_alter_curso_id_alter_matricula_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
