from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import HeroForm, AboutForm, SkillSectionForm, SkillForm, ServiceSectionForm, ServiceCardForm, TestimonialSectionForm, TestimonialForm, PortfolioCategoryForm, PortfolioItemForm
from portfolio_front.models import Hero, About, Skill, SkillSection, ServiceSection, ServiceCard, TestimonialSection, Testimonial, PortfolioItem, PortfolioCategory, PortfolioImage

def go_to_admin(request):
    return render(request, 'adminSide/admin.html')

def update_hero(request):
    hero = get_object_or_404(Hero, pk=1) 
    if request.method == 'POST':
        form = HeroForm(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HeroForm(instance=hero)
    return render(request, 'adminSide/update.html', {'form': form})

def update_about(request):
    about = get_object_or_404(About, pk=1)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AboutForm(instance=about)
    return render(request, 'adminSide/update.html', {'form': form})

# Skills section :

def get_skills(request):
    all_skillsection = SkillSection.objects.first()
    all_skills = Skill.objects.all()
    return render(request, "adminSide/datasheet/skill_sheet.html", {'all_skillsection': all_skillsection, 'all_skills': all_skills})

def update_skillsection(request, section_id):
    skillsection = get_object_or_404(SkillSection, id=section_id)
    if request.method == 'POST':
        form = SkillSectionForm(request.POST, instance=skillsection)
        if form.is_valid():
            form.save()
            return redirect('get_skills')
    else:
        form = SkillSectionForm(instance=skillsection)
    return render(request, 'adminSide/update.html', {'form': form})

def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_skills')
    else:
        form = SkillForm()
    return render(request, 'adminSide/create.html', {'form': form})

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('get_skills')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'adminSide/update.html', {'form': form})

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        skill.delete()
        return redirect('get_skills')
    return render(request, 'adminSide/delete.html', {'skill': skill})

# Services :

def get_services(request):
    all_servicesection = ServiceSection.objects.first()
    all_services = ServiceCard.objects.all()
    return render(request, "adminSide/datasheet/services_sheet.html", {'all_servicesection': all_servicesection, 'all_services': all_services})

def update_servicesection(request, section_id):
    servicesection = get_object_or_404(ServiceSection, id=section_id)
    if request.method == 'POST':
        form = ServiceSectionForm(request.POST, instance=servicesection)
        if form.is_valid():
            form.save()
            return redirect('get_services')
    else:
        form = ServiceSectionForm(instance=servicesection)
    return render(request, 'adminSide/update.html', {'form': form})

def create_service(request):
    if request.method == 'POST':
        form = ServiceCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_services')
    else:
        form = ServiceCardForm()
    return render(request, 'adminSide/create.html', {'form': form})

def update_service(request, service_id):
    service = get_object_or_404(ServiceCard, id=service_id)
    if request.method == 'POST':
        form = ServiceCardForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('get_services')
    else:
        form = ServiceCardForm(instance=service)
    return render(request, 'adminSide/update.html', {'form': form})

def delete_service(request, service_id):
    service = get_object_or_404(ServiceCard, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('get_services')
    return render(request, 'adminSide/delete.html', {'service': service})

# Testimonials :

def get_testimonials(request):
    all_testimonialsection = TestimonialSection.objects.first()
    all_testimonials = Testimonial.objects.all()
    return render(request, "adminSide/datasheet/testimonials_sheet.html", {'all_testimonialsection': all_testimonialsection, 'all_testimonials': all_testimonials})

def update_testimonialsection(request, section_id):
    testimonialsection = get_object_or_404(TestimonialSection, id=section_id)
    if request.method == 'POST':
        form = TestimonialSectionForm(request.POST, instance=testimonialsection)
        if form.is_valid():
            form.save()
            return redirect('get_testimonials')
    else:
        form = TestimonialSectionForm(instance=testimonialsection)
    return render(request, 'adminSide/update.html', {'form': form})

def create_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'adminSide/create.html', {'form': form})

def update_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('get_testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'adminSide/update.html', {'form': form})

def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('get_testimonials')
    return render(request, 'adminSide/delete.html', {'testimonial': testimonial})

# Portfolio :

def get_portfolio(request):
    all_categories = PortfolioCategory.objects.all()
    all_items = PortfolioItem.objects.all()
    return render(request, "adminSide/datasheet/portfolios_sheet.html", {'all_categories': all_categories, 'all_items': all_items})

def portfolio_item_detail(request, item_id):
    item = get_object_or_404(PortfolioItem, id=item_id)
    all_about = About.objects.first()
    return render(request, 'portfolio_details.html', {'item': item, 'all_about' : all_about, 'MEDIA_URL': settings.MEDIA_URL,})


def create_portfolio_category(request):
    if request.method == 'POST':
        form = PortfolioCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_portfolio')
    else:
        form = PortfolioCategoryForm()
    return render(request, 'adminSide/create.html', {'form': form})

def update_portfolio_category(request, category_id):
    category = get_object_or_404(PortfolioCategory, id=category_id)
    if request.method == 'POST':
        form = PortfolioCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('get_portfolio')
    else:
        form = PortfolioCategoryForm(instance=category)
    return render(request, 'adminSide/update.html', {'form': form})

def delete_portfolio_category(request, category_id):
    category = get_object_or_404(PortfolioCategory, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('get_portfolio')
    return render(request, 'adminSide/delete.html', {'category': category})

def create_portfolio_item(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            if 'image' in request.FILES:
                image = request.FILES['image']
                PortfolioImage.objects.create(item=item, image=image)
            return redirect('get_portfolio')
    else:
        form = PortfolioItemForm()
    return render(request, 'adminSide/create.html', {'form': form})

def update_portfolio_item(request, item_id):
    item = get_object_or_404(PortfolioItem, id=item_id)
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            if 'image' in request.FILES:
                image = request.FILES['image']
                if item.images.exists():
                    item.images.first().image = image
                    item.images.first().save()
                else:
                    PortfolioImage.objects.create(item=item, image=image)
            return redirect('get_portfolio')
    else:
        form = PortfolioItemForm(instance=item)
    return render(request, 'adminSide/update.html', {'form': form})

def delete_portfolio_item(request, item_id):
    item = get_object_or_404(PortfolioItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('get_portfolio')
    return render(request, 'adminSide/delete.html', {'item': item})
