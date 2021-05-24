from django.contrib import admin
from .models import HeroText, ContactInformation, Partner, Project, Menu, AboutUsText, PartnerText, ProjectText, ProductText, ContactText, FooterText, Product
from django.contrib.auth.models import Group

admin.site.register(HeroText)
admin.site.register(ContactInformation)
admin.site.register(Partner)
admin.site.register(Project)
admin.site.register(Menu)
admin.site.register(AboutUsText)
admin.site.register(PartnerText)
admin.site.register(ProjectText)
admin.site.register(ProductText)
admin.site.register(ContactText)
admin.site.register(FooterText)
admin.site.register(Product)

admin.site.unregister(Group)