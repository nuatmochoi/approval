from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tag, document,tag_str,approved_doc,denied_doc,chat_record,TagModel



admin.site.register(Tag)


admin.site.register(document)

admin.site.register(tag_str)

admin.site.register(approved_doc)

admin.site.register(denied_doc)

admin.site.register(chat_record)

admin.site.register(TagModel)