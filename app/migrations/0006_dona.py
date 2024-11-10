# Generated by Django 5.1.3 on 2024-11-10 03:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_adopta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=200)),
                ('VALOR', models.IntegerField()),
                ('EMAIL', models.EmailField(max_length=254)),
                ('FECHA_DONACION', models.DateTimeField(auto_now_add=True)),
                ('METODO_PAGO', models.CharField(max_length=50)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
                ('DIRECCION', models.CharField(blank=True, max_length=255, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]