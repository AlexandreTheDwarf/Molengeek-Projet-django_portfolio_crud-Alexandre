from django import forms
from portfolio_front.models import Hero, About, SkillSection, Skill, PortfolioCategory, PortfolioItem, PortfolioImage, ServiceSection, ServiceCard, TestimonialSection, Testimonial
from django.forms import inlineformset_factory

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class SkillSectionForm(forms.ModelForm):
    class Meta:
        model = SkillSection
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class PortfolioCategoryForm(forms.ModelForm):
    class Meta:
        model = PortfolioCategory
        fields = '__all__'

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['category', 'title', 'client', 'project_date', 'project_url', 'description']

class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image']

PortfolioImageFormSet = inlineformset_factory(PortfolioItem, PortfolioImage, form=PortfolioImageForm, extra=1, can_delete=True)

class ServiceSectionForm(forms.ModelForm):
    class Meta:
        model = ServiceSection
        fields = '__all__'

class ServiceCardForm(forms.ModelForm):
    class Meta:
        model = ServiceCard
        fields = ['icon', 'title', 'description']

class TestimonialSectionForm(forms.ModelForm):
    class Meta:
        model = TestimonialSection
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['quote', 'image', 'name', 'title']