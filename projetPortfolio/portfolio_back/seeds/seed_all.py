from django_seed import Seed

from .hero import seed_hero
from .skills import seed_skill_section, seed_skills
from .portfolio import seed_categories, seed_portfolio_items, seed_portfolio_images
from .about import seed_about
from .services import seed_service_section
from .testimonials import seed_testimonial_section, seed_testimonials, seed_testimonial_images
from .contact import seed_contact

def run():
    seeder = Seed.seeder()

    seed_hero(seeder)
    seed_skill_section(seeder)
    seed_skills(seeder)

    categories = seed_categories()
    image_items = seed_portfolio_items(categories)
    seed_portfolio_images(image_items)

    seed_about()

    seed_service_section()

    testimonial_section = seed_testimonial_section()  
    testimonial_items = seed_testimonials(testimonial_section)  
    seed_testimonial_images(testimonial_items)  

    seed_contact()

    pks = seeder.execute()
    print(pks)