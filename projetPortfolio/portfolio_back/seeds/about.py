from portfolio_front.models import About
from django.core.files import File
import os
from datetime import date

def seed_about():
    image_path = os.path.join('media_seed', 'profile-img.jpg')
    with open(image_path, 'rb') as img_file:
        about = About.objects.create(
            under_title="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.",
            photo=File(img_file, name='profile-img.jpg'),
            job="UI/UX Designer & Web Developer",
            under_career_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            birthday=date(1995, 5, 1),
            website="www.example.com",
            phone="+123 456 7890",
            city="New York, USA",
            age=30,
            degree="Master",
            email="email@example.com",
            freelance=True,
            end_about_text="Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores."
        )
        print(f"About created: {about.id}")
