def artist():
    name = "Abel Tesfsy(The Weeknd)"
    print(name)


artist()


def genere():
    music_type = "Hip Hop"
    print(music_type)


genere()


def year():
    published_time = 2020
    print(published_time)


year()


facebook = "Facebook\'s rating is"
fb_rating = 3.5
fb_rating_str = str(3.5)
fb = facebook + " " + fb_rating_str
print(fb)

motto = 'Facebook\'s new motto is "move fast weith stable infra."'
print(motto)

# String

app_name = "Pandora - Music & Radio"
average_rating = float("4.0")
total_ratings = int("1724546")
price = "free"
print(app_name)

# Index

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[4]
rating_2 = row_2[4]
rating_3 = row_3[4]
total = rating_1 + rating_2 + rating_3
average = total/3
print(average)

rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]
total = rating_1 + rating_2 + rating_3
average = total/3
print(average)

# Retrieving Multiple list element
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0], row_1[-1]]
print(fb_rating_data)
insta_rating_data = [row_2[0], row_2[-1]]
Pandora_rating_data = [row_5[0], row_5[-1]]

avg_rating = (fb_rating_data[-1] +
              insta_rating_data[-1] + Pandora_rating_data[-1])/3
print(avg_rating)

fb_first_4 = row_1[0:4]
print(fb_first_4)

last_3_fb = row_1[-3:-1]
print(last_3_fb)

# Tuples
fruits = ("banana", "orange", "grape")
for x in fruits:
    print(x)
print(type(fruits))

# Python Dictionary
mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}
print(mycar)

mygreens = dict(fruit = "green apples", vegetable = "kale")
print(mygreens)