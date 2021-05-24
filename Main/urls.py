from django.urls import path

from . import views

urlpatterns = [
	# Home
	path("en/", views.home, name="home"),
	path("", views.home_az, name="home-az"),
	path("ru/", views.home_ru, name="home-ru"),
	path("tr/", views.home_tr, name="home-tr"),
	path("contact/", views.send_mail, name="email"),

	# Projects
	path("en/project/<str:pid>", views.project, name="project"),
	path("project/<str:pid>", views.project_az, name="project-az"),
	path("ru/project/<str:pid>", views.project_ru, name="project-ru"),
	path("tr/project/<str:pid>", views.project_tr, name="project-tr"),

	# Products
	path("en/product/<str:pid>", views.product, name="product"),
	path("product/<str:pid>", views.product_az, name="product-az"),
	path("ru/product/<str:pid>", views.product_ru, name="product-ru"),
	path("tr/product/<str:pid>", views.product_tr, name="product-tr"),
]