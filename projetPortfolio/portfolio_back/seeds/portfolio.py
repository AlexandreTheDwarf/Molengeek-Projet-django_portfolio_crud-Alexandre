from portfolio_front.models import PortfolioCategory, PortfolioItem, PortfolioImage
from django.core.files import File
import os
from datetime import date

def seed_categories():
    categories = {}
    for name in ["App", "Card", "Web"]:
        obj, _ = PortfolioCategory.objects.get_or_create(name=name)
        categories[name] = obj
    return categories

def seed_portfolio_items(categories):
    # Liste des projets et images à insérer
    projects = [
        ("App", "App Project One", "Client A", "Description de l'App One", "portfolio-1.jpg", date(2023, 6, 15)),
        ("Web", "Web Project One", "Client B", "Description du Web One", "portfolio-2.jpg", date(2022, 11, 5)),
        ("App", "App Project Two", "Client C", "Description de l'App Two", "portfolio-3.jpg", date(2023, 7, 10)),
        ("Card", "Card Project One", "Client D", "Description du Card One", "portfolio-4.jpg", date(2023, 5, 25)),
        ("Web", "Web Project Two", "Client E", "Description du Web Two", "portfolio-5.jpg", date(2022, 12, 1)),
        ("App", "App Project Three", "Client F", "Description de l'App Three", "portfolio-6.jpg", date(2023, 8, 3)),
        ("Card", "Card Project Two", "Client G", "Description du Card Two", "portfolio-7.jpg", date(2023, 4, 18)),
        ("Card", "Card Project Three", "Client H", "Description du Card Three", "portfolio-8.jpg", date(2023, 9, 12)),
        ("Web", "Web Project Three", "Client I", "Description du Web Three", "portfolio-9.jpg", date(2023, 10, 25)),
    ]

    portfolio_items = []
    for category_name, title, client, description, image_name, project_date in projects:
        item = PortfolioItem.objects.create(
            category=categories[category_name],
            title=title,
            client=client,
            project_date=project_date,
            project_url=f"https://example.com/{title.replace(' ', '').lower()}",
            description=description
        )
        portfolio_items.append((item, image_name))

    return portfolio_items

def seed_portfolio_images(image_items):
    for item, image_name in image_items:
        image_path = os.path.join('media_seed', image_name)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                PortfolioImage.objects.create(item=item, image=File(img_file, name=image_name))
        else:
            print(f"⚠️ Image manquante : {image_path}")
