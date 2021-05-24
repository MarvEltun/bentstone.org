from django.shortcuts import render, redirect
from .models import HeroText, ContactInformation, Partner, Project, Menu, AboutUsText, PartnerText, ProjectText, ProductText, ContactText, FooterText, Product

from django.core.mail import send_mail as mail

def getAllInfo(lang):
	hero		= HeroText.objects.filter(lang=lang).first()
	contact		= ContactInformation.objects.all().first()
	partners	= Partner.objects.all()
	projects	= Project.objects.all()
	menu		= Menu.objects.filter(lang=lang).first()
	about		= AboutUsText.objects.filter(lang=lang).first()
	partner_txt	= PartnerText.objects.filter(lang=lang).first()
	projectTxt	= ProjectText.objects.filter(lang=lang).first()
	productTxt	= ProductText.objects.filter(lang=lang).first()
	contactTxt	= ContactText.objects.filter(lang=lang).first()
	footerTxt	= FooterText.objects.filter(lang=lang).first()
	products	= Product.objects.all()
	data		= {
		"lang": lang,
		"hero": hero,
		"contact": contact,
		"partners": partners,
		"projects": projects,
		"menu": menu,
		"about": about,
		"partner_txt": partner_txt,
		"projectTxt": projectTxt,
		"productTxt": productTxt,
		"contactTxt": contactTxt,
		"footerTxt": footerTxt,
		"products": products
	}
	return data

def home(request):
	data	= getAllInfo("EN")
	return render(request, "main/main.html", data)

def home_az(request):
	data	= getAllInfo("AZ")
	return render(request, "main/main.html", data)

def home_ru(request):
	data	= getAllInfo("RU")
	return render(request, "main/main.html", data)

def home_tr(request):
	data	= getAllInfo("TR")
	return render(request, "main/main.html", data)

def send_mail(request):
	if request.method == "POST":
		name	= request.POST.get("name")
		subject = f"Message from {name}"
		content	= request.POST.get("message")
		email	= request.POST.get("email")
		content += f"\n Client email: {email}"
		mail(
			subject,
			content,
			email,
			["oceanwinckler.rem@gmail.com"]
		)

	return redirect("home")

def project(request, pid):
	data	= getAllInfo("EN")
	project	= Project.objects.filter(id=pid).first()
	if project == None:
		return redirect("home")
	data.update({"project": project})
	return render(request, "main/project.html", data)

def project_az(request, pid):
	data	= getAllInfo("AZ")
	project	= Project.objects.filter(id=pid).first()
	if project == None:
		return redirect("home_az")
	data.update({"project": project})
	return render(request, "main/project.html", data)

def project_ru(request, pid):
	data	= getAllInfo("RU")
	project	= Project.objects.filter(id=pid).first()
	if project == None:
		return redirect("home_ru")
	data.update({"project": project})
	return render(request, "main/project.html", data)

def project_tr(request, pid):
	data	= getAllInfo("TR")
	project	= Project.objects.filter(id=pid).first()
	if project == None:
		return redirect("home_tr")
	data.update({"project": project})
	return render(request, "main/project.html", data)

def product(request, pid):
	data	= getAllInfo("EN")
	product	= Product.objects.filter(id=pid).first()
	data.update({"product": product})
	return render(request, "main/product.html", data)

def product_az(request, pid):
	data	= getAllInfo("AZ")
	product	= Product.objects.filter(id=pid).first()
	data.update({"product": product})
	return render(request, "main/product.html", data)

def product_ru(request, pid):
	data	= getAllInfo("RU")
	product	= Product.objects.filter(id=pid).first()
	data.update({"product": product})
	return render(request, "main/product.html", data)

def product_tr(request, pid):
	data	= getAllInfo("TR")
	product	= Product.objects.filter(id=pid).first()
	data.update({"product": product})
	return render(request, "main/product.html", data)