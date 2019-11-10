from django.contrib import admin
from .models import QCollection, Question, Answer

admin.site.register(QCollection)
admin.site.register(Question)
admin.site.register(Answer)
