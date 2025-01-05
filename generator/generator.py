from data.data import Person
from faker import Faker

faker = Faker('en_US')

def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )