"""
URL configuration for projetPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio_front import views as front_views
from portfolio_back import views as back_views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin Django
    path('', front_views.get_all_data, name='index'),
    path('adminPanel/', back_views.go_to_admin, name='adminPanel'),
    path('adminPanel/update-hero/', back_views.update_hero, name='update_hero'),
    path('adminPanel/update-about/', back_views.update_about, name='update_about'),
    # Skills :
    path('adminPanel/skills/', back_views.get_skills, name='get_skills'),
    path('update-skillsection/<int:section_id>/', back_views.update_skillsection, name='update_skillsection'),
    path('create-skill/', back_views.create_skill, name='create_skill'),
    path('update-skill/<int:skill_id>/', back_views.update_skill, name='update_skill'),
    path('delete-skill/<int:skill_id>/', back_views.delete_skill, name='delete_skill'),
    # Services :
    path('adminPanel/services/', back_views.get_services, name='get_services'),
    path('update-servicesection/<int:section_id>/', back_views.update_servicesection, name='update_servicesection'),
    path('create-service/', back_views.create_service, name='create_service'),  
    path('update-service/<int:service_id>/', back_views.update_service, name='update_service'),
    path('delete-service/<int:service_id>/', back_views.delete_service, name='delete_service'),
    # Testimonials
    path('adminPanel/testimonials/', back_views.get_testimonials, name='get_testimonials'),
    path('update-testimonialsection/<int:section_id>/', back_views.update_servicesection, name='update_testimonialsection'),
    path('create-testimonial/', back_views.create_testimonial, name='create_testimonial'),  
    path('update-testimonial/<int:testimonial_id>/', back_views.update_testimonial, name='update_testimonial'),
    path('delete-testimonial/<int:testimonial_id>/', back_views.delete_testimonial, name='delete_testimonial'),
  # Portfolio :
    path('adminPanel/portfolio/', back_views.get_portfolio, name='get_portfolio'),
    path('portfolio/<int:item_id>/', back_views.portfolio_item_detail, name='portfolio_item_detail'),
    path('create-portfolio-category/', back_views.create_portfolio_category, name='create_portfolio_category'),
    path('update-portfolio-category/<int:category_id>/', back_views.update_portfolio_category, name='update_portfolio_category'),
    path('delete-portfolio-category/<int:category_id>/', back_views.delete_portfolio_category, name='delete_portfolio_category'),
    path('create-portfolio-item/', back_views.create_portfolio_item, name='create_portfolio_item'),
    path('update-portfolio-item/<int:item_id>/', back_views.update_portfolio_item, name='update_portfolio_item'),
    path('delete-portfolio-item/<int:item_id>/', back_views.delete_portfolio_item, name='delete_portfolio_item'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
