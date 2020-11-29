from django.contrib import admin

from toys.models import Toy, Tag, User

admin.site.register(Toy)
admin.site.register(Tag)
admin.site.register(User)
