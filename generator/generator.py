import random

from data.data import Person
from faker import Faker

faker = Faker('en_US')

def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(10, 80),
        department= faker.job(),
        salary=random.randint(10000, 80000),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )