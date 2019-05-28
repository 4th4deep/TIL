class Fourth:
    late = '09:10'
    finish = '18:00'
    lunch = '12:10'
    title = 'Deep learning ...'


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

p1 = Person('dd')
p2 = Person('zz')

print(Person.population, p1.population)
p1.population = 100
print(Person.population, p1.population)