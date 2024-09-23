from django.contrib import admin
from conferenceApp.models import  Conference,Speaker,Attendee,Review,Session
# Register your models here.

admin.site.register(Conference)
admin.site.register(Speaker)
admin.site.register(Attendee)
admin.site.register(Session)
admin.site.register(Review)
