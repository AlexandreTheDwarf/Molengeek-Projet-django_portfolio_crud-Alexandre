from portfolio_front.models import TestimonialSection, Testimonial
from django.core.files import File
import os
from datetime import date

def seed_testimonial_section():
    # Crée la section des témoignages
    section, _ = TestimonialSection.objects.get_or_create(
        under_title="Découvrez ce que nos clients disent de nous."
    )
    return section

def seed_testimonials(section):
    # Liste des témoignages à insérer
    testimonials = [
        ("Proin iaculis purus consequat sem cure digni ssim.", "testimonials-1.jpg", "Saul Goodman", "CEO & Founder"),
        ("Export tempor illum tamen malis malis.", "testimonials-2.jpg", "Sara Wilsson", "Designer"),
        ("Enim nisi quem export duis labore cillum.", "testimonials-3.jpg", "Jena Karlis", "Store Owner"),
        ("Fugiat enim eram quae cillum dolore dolor.", "testimonials-4.jpg", "Matt Brandon", "Freelancer"),
        ("Quis quorum aliqua sint quem legam.", "testimonials-5.jpg", "John Larson", "Entrepreneur")
    ]

    testimonial_items = []
    for quote, image_name, name, title in testimonials:
        testimonial = Testimonial.objects.create(
            quote=quote,
            image=None,  # L'image sera ajoutée dans la prochaine fonction
            name=name,
            title=title,
            section=section
        )
        testimonial_items.append((testimonial, image_name))

    return testimonial_items

def seed_testimonial_images(testimonial_items):
    for testimonial, image_name in testimonial_items:
        image_path = os.path.join('media_seed', image_name)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                testimonial.image = File(img_file, name=image_name)
                testimonial.save()
        else:
            print(f"⚠️ Image manquante : {image_path}")
