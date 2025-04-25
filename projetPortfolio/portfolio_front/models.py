from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=32)
    data_typed_items = models.CharField(max_length=128)

class About(models.Model):
    DEGREE_CHOICES = [
        ('None', 'Aucun diplôme'),
        ('HighSchool', 'Baccalauréat'),
        ('Bachelor', 'Licence'),
        ('Master', 'Master'),
        ('PhD', 'Doctorat'),
    ]

    under_title = models.TextField()
    photo = models.ImageField(upload_to='about_photos/')
    job = models.CharField(max_length=64)
    under_career_text = models.TextField()
    birthday = models.DateField()
    website = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    email = models.EmailField()
    freelance = models.BooleanField()
    end_about_text = models.TextField()

# Skills start

class SkillSection(models.Model):
    under_title = models.TextField()  # Texte sous le titre de la section

class Skill(models.Model):
    name = models.CharField(max_length=100)  # Nom de la compétence (ex: HTML, CSS)
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Pourcentage de maîtrise entre 0 et 100"
    )  # Pourcentage de maîtrise (ex: 100, 90)

# Skills End

# Portfolio start

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)  # Nom de la catégorie (ex: App, Card, Web)

    def __str__(self):
        return self.name[:50]

class PortfolioItem(models.Model):
    category = models.ForeignKey(PortfolioCategory, related_name='items', on_delete=models.CASCADE)  # Lien vers la catégorie
    title = models.CharField(max_length=100)  # Titre du projet
    client = models.CharField(max_length=100)  # Nom du client
    project_date = models.DateField()  # Date du projet
    project_url = models.URLField(blank=True, null=True)  # URL du projet
    description = models.TextField()  # Description détaillée du projet

    def __str__(self):
        return self.title[:50]

class PortfolioImage(models.Model):
    item = models.ForeignKey(PortfolioItem, related_name='images', on_delete=models.CASCADE)  # Lien vers le projet
    image = models.ImageField(upload_to='portfolio/')  # Image du projet

# Portfolio ending

# Services start

class ServiceSection(models.Model):
    under_title = models.TextField()  # Texte sous le titre de la section

    def __str__(self):
        return self.under_title[:50]

class ServiceCard(models.Model):
    ICON_CHOICES = [
        ('bi bi-briefcase', 'Briefcase'),
        ('bi bi-card-checklist', 'Card Checklist'),
        ('bi bi-bar-chart', 'Bar Chart'),
        ('bi bi-binoculars', 'Binoculars'),
        ('bi bi-brightness-high', 'Brightness High'),
        ('bi bi-calendar4-week', 'Calendar Week'),
        # Ajoutez d'autres icônes ici
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=64)
    description = models.TextField()

    # Ajout du champ section pour faire la relation avec ServiceSection
    section = models.ForeignKey(
    ServiceSection, 
    related_name='service_cards', 
    on_delete=models.CASCADE, 
    default=1  # ici 1 correspond à l'ID d'une `ServiceSection` existante
)

# Services end

# Testimonials debut

class TestimonialSection(models.Model):
    under_title = models.TextField()  # Texte sous le titre de la section

class Testimonial(models.Model):
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    section = models.ForeignKey(TestimonialSection, related_name='testimonials', on_delete=models.CASCADE, default=1)  # Utilise un ID de section par défaut ici

# Testimonials end 

# Contact Debut

class Contact(models.Model):
    under_title = models.TextField()  # Texte sous le titre de la section
    location = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    iframe_url = models.TextField(default='')  # L'URL de l'iframe Google Maps

# Contact end