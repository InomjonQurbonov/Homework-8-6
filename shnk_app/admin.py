from django.contrib import admin
from shnk_app.models import Podsystem, Groups, Document, Document_files, Document_types

admin.site.register(Podsystem)
admin.site.register(Groups)
admin.site.register(Document)
admin.site.register(Document_files)
admin.site.register(Document_types)
