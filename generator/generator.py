from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
faker_ua = Faker('uk_UA')
"""'uk_UA' українська, 'ru_RU' мова вбивць, 'en_US' за замоченням, ['it_IT', 'en_US', 'ja_JP'] для перебору"""
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name() + " " + faker_en.first_name(),
        email=faker_en.email(),
        location=faker_en.address(),
        company=faker_en.address(),
        massage=faker_en.text(),
    )


def generated_person_ua():
    yield Person(
        full_name=faker_ua.first_name() + " " + faker_ua.last_name() + " " + faker_ua.first_name(),
        email=faker_ua.email(),
        location=faker_ua.address(),
        company=faker_ua.address(),
        massage=faker_ua.text(),
    )
