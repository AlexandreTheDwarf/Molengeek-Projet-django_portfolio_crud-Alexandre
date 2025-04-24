from portfolio_front.models import ServiceSection, ServiceCard

def seed_service_section():
    # Création de la section Services
    section = ServiceSection.objects.create(
        under_title="Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas."
    )

    # Création des cartes de service
    services = [
        ('bi bi-briefcase', 'Lorem Ipsum', 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident'),
        ('bi bi-card-checklist', 'Dolor Sitema', 'Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata'),
        ('bi bi-bar-chart', 'Sed ut perspiciatis', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'),
        ('bi bi-binoculars', 'Magni Dolores', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'),
        ('bi bi-brightness-high', 'Nemo Enim', 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque'),
        ('bi bi-calendar4-week', 'Eiusmod Tempor', 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi')
    ]

    # Ajout des cartes à la section
    for icon, title, description in services:
        ServiceCard.objects.create(
            section=section,  # Associer à la section Services
            icon=icon,
            title=title,
            description=description
        )

    print("Seed completé pour la section Services et ses cartes.")

