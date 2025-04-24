from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from portfolio_front.models import Hero, About, SkillSection, Skill, PortfolioCategory, PortfolioItem, PortfolioImage, ServiceSection, ServiceCard, TestimonialSection, Testimonial, Contact

def get_all_data(request):
    all_hero = Hero.objects.first()
    all_about = About.objects.first()
    all_skillsection = SkillSection.objects.first()
    all_skills = Skill.objects.all()
    all_portfoliocategories = PortfolioCategory.objects.all()
    all_portfolioitems = PortfolioItem.objects.all()
    all_portfolioimages = PortfolioImage.objects.all()
    all_servicesection = ServiceSection.objects.first()
    all_servicecards = ServiceCard.objects.all()
    all_testimonialsection = TestimonialSection.objects.first()
    all_testimonials = Testimonial.objects.all()
    all_contact = Contact.objects.first()
    return render(request, "index.html", 
                  {'all_hero' : all_hero,
                   'all_about' : all_about,
                   'all_skillsection': all_skillsection,
                    'all_skills': all_skills,
                    'all_portfoliocategories': all_portfoliocategories,
                    'all_portfolioitems': all_portfolioitems,
                    'all_portfolioimages': all_portfolioimages,
                    'all_servicesection': all_servicesection,
                    'all_servicecards': all_servicecards,
                    'all_testimonialsection': all_testimonialsection,
                    'all_testimonials': all_testimonials,
                    'all_contact': all_contact,
                    'MEDIA_URL': settings.MEDIA_URL,
                   })
