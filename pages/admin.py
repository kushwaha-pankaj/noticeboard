from django.contrib import admin
from pages.models import Slider, About, Notice, Review, Contributor, Courses

admin.site.site_header = "NBPI-Quick NoticeBoard"

admin.site.site_title = "NBPI-Quick NoticeBoard"

admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Notice)
admin.site.register(Review)
admin.site.register(Contributor)
admin.site.register(Courses)