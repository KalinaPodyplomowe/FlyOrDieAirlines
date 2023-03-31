# Generated by Django 4.1.7 on 2023-03-31 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_number', models.CharField(max_length=10)),
                ('date_reserved', models.DateField()),
                ('checked_in', models.BooleanField(default=False)),
                ('baggage_count', models.IntegerField()),
                ('baggage_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
                ('street_address', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_travel', models.DateField()),
                ('flight_number', models.CharField(max_length=10)),
                ('reservation_date', models.DateField()),
                ('arrival_airport_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport_history', to='flights.airport')),
                ('departure_airport_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport_history', to='flights.airport')),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.reservation')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.user')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.user'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='worker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.worker'),
        ),
    ]
