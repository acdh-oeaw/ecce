from django.contrib import admin
from .models import *

admin.site.register(Date)
admin.site.register(Corpus)
admin.site.register(Text)
admin.site.register(Consonant)
admin.site.register(Cluster)
admin.site.register(TokenLabel)
admin.site.register(SchwaPresent)
admin.site.register(OnSet)
admin.site.register(Token)
admin.site.register(Lemma)

# Register your models here.
