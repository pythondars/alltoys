from django.db import transaction

from toys.models import Toy, User


def create_toy():
    with transaction.atomic():
        user = User.objects.create(first_name="test user")
        try:
            with transaction.atomic():
                toy = Toy.objects.create(name="Test toy")
                raise Exception("Uzr!")
        except Exception as e:
            print(e)

    print(user.first_name)
