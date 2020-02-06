# Artist Name
Artist = "Abel Tesfaye or The Weeknd"

# Music Type
Genere = "Hip hop"

# Duration
DurationInsecond = 204

# TimeRelease
TimeRelease = "December,2019"

# Music about
MusicAbout = "Love"

# Song
Song = "Blinding Lights"
print(Artist)
print(Genere)
print(DurationInsecond)
print(TimeRelease)
print(MusicAbout)
print(Song)


# Class in Python

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
point.draw()
print(point.default_color)
print(Point.default_color)
another = Point(3, 4)
print(another.default_color)

another.draw()


# Class and instance method
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point.zero()
point.draw()


# Magic Method

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
print(str(point))


# compare objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point < other)


# Performing Artimetic operation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x and self.y + other.y


point = Point(10, 20)
other = Point(1, 2)
print(point + other)


# creating custome container

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

# Private member


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)


# properties
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value


product = Product(-50)
