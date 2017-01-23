from django.contrib import admin

# Register your models here.

from .models import Post, Respuesta, Usuario

class RespuestaInLine(admin.StackedInline):
	model = Respuesta
	extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Post_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [RespuestaInLine]
admin.site.register(Post, PostAdmin)
admin.site.register(Respuesta)
admin.site.register(Usuario)


