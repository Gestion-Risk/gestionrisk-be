# Generated by Django 3.2.8 on 2021-10-16 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCapacitacion',
            fields=[
                ('idAreaCap', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=45, verbose_name='area')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('idCapacitacion', models.AutoField(primary_key=True, serialize=False)),
                ('curso', models.CharField(max_length=45, verbose_name='curso')),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
                ('idAreaCapacitacionFk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='capacitacionAreaFk', to='AuthAppEmpleados.areacapacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('idCargo', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=45, verbose_name='cargo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('cedula', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('cargoIdFk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cargoIdFk', to='AuthAppEmpleados.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idRegistro', models.AutoField(primary_key=True, serialize=False)),
                ('cedulaTrabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cedulaTrabajadorFk', to='AuthAppEmpleados.trabajadores')),
                ('idCapacitacionFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idCapacitacionFk', to='AuthAppEmpleados.capacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='CargosCapacitacion',
            fields=[
                ('idCarCap', models.AutoField(primary_key=True, serialize=False, verbose_name='id_car_cap')),
                ('idAreaCapFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_area_fk', to='AuthAppEmpleados.areacapacitacion')),
                ('idcarFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_cargo_fk', to='AuthAppEmpleados.cargos')),
            ],
        ),
    ]