

from django.shortcuts import render, redirect
from django.db import connection
from .models import hotels


# Create your views here.
def offers(request):
    return render(request, "offers.html")


def Aurora(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Aurora Borealis"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Aurora Borealis"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Aurora Borealis"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Aurora Borealis"''')

    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()
    return render(request, "scotland_info.html", {'fool': fool, 'fool1': fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Disney(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Disney Land, Hongkong"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Disney Land, Hongkong"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Disney Land,
     Hongkong"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Disney Land, Hongkong"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()
    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Maldiv(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Maldives"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Maldives"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Maldives"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Maldives"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()

    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Prague(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Prague"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Prague"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Prague"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Prague"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()

    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Santor(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Santorini"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Santorini"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Santorini"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Santorini"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()

    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Scotla(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Scotland"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Scotland"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Scotland"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Scotland"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()

    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


def Venice(request):
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor.execute('''SELECT * FROM hotels_hotels where name="Venice"''')
    cursor1.execute('''SELECT * FROM hotels_things where name="Venice"''')
    cursor2.execute('''SELECT * FROM hotels_restaurants where name="Venice"''')
    cursor3.execute('''SELECT * FROM hotels_flights where name="Venice"''')
    fool = cursor.fetchall()
    fool1 = cursor1.fetchall()
    fool2 = cursor2.fetchall()
    fool3 = cursor3.fetchall()

    return render(request, "scotland_info.html", {'fool': fool,'fool1':fool1,
                                                  'fool2':fool2,'fool3':fool3})


