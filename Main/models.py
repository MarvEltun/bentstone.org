from django.db import models

class HeroText(models.Model):
	text_1		= models.CharField(max_length=250)
	text_2		= models.CharField(max_length=250)
	text_3		= models.CharField(max_length=250)
	button_1	= models.CharField(max_length=250, default="Our products")
	button_2	= models.CharField(max_length=250, default="Get in touch")
	lang		= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Hero Section"

class Menu(models.Model):
	open_button		= models.CharField(max_length=50)
	close_button	= models.CharField(max_length=50)
	home_button		= models.CharField(max_length=50)
	products_button	= models.CharField(max_length=50)
	projects_button	= models.CharField(max_length=50)
	about_us_button	= models.CharField(max_length=50)
	contact_button	= models.CharField(max_length=50)
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Menu"

class ContactInformation(models.Model):
	email	= models.EmailField()
	phone	= models.CharField(max_length=20)
	def __str__(self):
		return "Contact Informations"

class Partner(models.Model):
	name	= models.CharField(max_length=200)
	logo	= models.ImageField(upload_to="partners/")

	def __str__(self):
		return f"{self.name}"

class Project(models.Model):
	name			= models.CharField(max_length=200)
	category		= models.CharField(max_length=200)
	description		= models.TextField()

	name_az			= models.CharField(max_length=200)
	category_az		= models.CharField(max_length=200)
	description_az	= models.TextField()

	name_ru			= models.CharField(max_length=200)
	category_ru		= models.CharField(max_length=200)
	description_ru	= models.TextField()

	name_tr			= models.CharField(max_length=200)
	category_tr		= models.CharField(max_length=200)
	description_tr	= models.TextField()
	image			= models.ImageField(upload_to="projects/")

	def __str__(self):
		return f"{self.name}"

class AboutUsText(models.Model):
	title			= models.CharField(max_length=50)
	subtitle		= models.CharField(max_length=250)
	content			= models.TextField()
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] About Us Section"

class PartnerText(models.Model):
	title			= models.CharField(max_length=50)
	subtitle		= models.CharField(max_length=250)
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Partners Section"

class ProjectText(models.Model):
	title			= models.CharField(max_length=50)
	subtitle		= models.CharField(max_length=250)
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Project Section"

class ProductText(models.Model):
	title			= models.CharField(max_length=50)
	subtitle		= models.CharField(max_length=250)
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Product Section"

class ContactText(models.Model):
	title			= models.CharField(max_length=50)
	subtitle		= models.CharField(max_length=250)
	name_field		= models.CharField(max_length=50)
	email_field		= models.CharField(max_length=50)
	message_field	= models.CharField(max_length=50)
	lang			= models.CharField(max_length=2, default="EN")

	def __str__(self):
		return f"[{self.lang}] Contact Section"

class FooterText(models.Model):
	title			= models.CharField(max_length=250)
	copyright		= models.CharField(max_length=250)
	description		= models.TextField()
	lang			= models.CharField(max_length=2, default="EN")
	def __str__(self):
		return f"[{self.lang}] Footer Section"

class Product(models.Model):
	name			= models.CharField(max_length=200)
	category		= models.CharField(max_length=200)
	description		= models.TextField()
	price			= models.CharField(max_length=30)

	name_az			= models.CharField(max_length=200)
	category_az		= models.CharField(max_length=200)
	description_az	= models.TextField()
	price_az		= models.CharField(max_length=30)

	name_ru			= models.CharField(max_length=200)
	category_ru		= models.CharField(max_length=200)
	description_ru	= models.TextField()
	price_ru		= models.CharField(max_length=30)

	name_tr			= models.CharField(max_length=200)
	category_tr		= models.CharField(max_length=200)
	description_tr	= models.TextField()
	price_tr		= models.CharField(max_length=30)
	image			= models.ImageField(upload_to="products/")

	def __str__(self):
		return f"{self.name}"