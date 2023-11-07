# Generated by Django 4.2.6 on 2023-11-06 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_book_seat_no"),
    ]

    operations = [
        migrations.CreateModel(
            name="seat_book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "seat_no1",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no2",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no3",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no4",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no5",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no6",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no7",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no8",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no9",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no10",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no11",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no12",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no13",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no14",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no15",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no16",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no17",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no18",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no19",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no20",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no21",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no22",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no23",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no24",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no25",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no26",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no27",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no28",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no29",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no30",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no31",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no32",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no33",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no34",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no35",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no36",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no37",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no38",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no39",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
                (
                    "seat_no40",
                    models.CharField(
                        choices=[("B", "Booked"), ("E", "empty")],
                        default="E",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="ticketbooking", name="seat",),
        migrations.RemoveField(model_name="ticketbooking", name="user",),
        migrations.RemoveField(model_name="book", name="seat_no",),
        migrations.DeleteModel(name="BusSeat",),
        migrations.DeleteModel(name="TicketBooking",),
        migrations.AddField(
            model_name="seat_book",
            name="bus_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.book"
            ),
        ),
    ]
