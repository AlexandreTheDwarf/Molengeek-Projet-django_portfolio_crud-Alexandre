from django import forms
from portfolio_front.models import Hero, About, SkillSection, Skill, PortfolioCategory, PortfolioItem, PortfolioImage, ServiceSection, ServiceCard, TestimonialSection, Testimonial

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
    image = forms.ImageField(required=False)  # Champ hors modèle

    class Meta:
        model = PortfolioItem
        fields = ['category', 'title', 'client', 'project_date', 'project_url', 'description']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['image'].required = False

class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image']

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