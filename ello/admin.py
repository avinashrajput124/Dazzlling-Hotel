from django.contrib import admin

from ello.models import Add_Hotal, User,promotions,exclusive_partners,offer_for_you,Holiday_packages,youtube_video,whats_new

# Register your models here.
 
 # mts lactures
admin.site.register(Add_Hotal)
admin.site.register(promotions)
admin.site.register(User)
admin.site.register(exclusive_partners)
admin.site.register(offer_for_you)
admin.site.register(Holiday_packages)
admin.site.register(youtube_video)
admin.site.register(whats_new)
