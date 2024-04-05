from django.contrib import admin
# from .models import TodoItem
from .models import Aula, Disciplina, GradeCurricular, Turma

# Register your models here.
# admin.site.register(TodoItem)
admin.site.register(Aula)
admin.site.register( Disciplina)
admin.site.register( GradeCurricular)
admin.site.register( Turma)