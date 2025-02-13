from faker import Faker


def generate_random_name() -> str:
    """Generate random name"""

    fake = Faker('ru_RU')
    random_name = fake.name()
    return random_name
