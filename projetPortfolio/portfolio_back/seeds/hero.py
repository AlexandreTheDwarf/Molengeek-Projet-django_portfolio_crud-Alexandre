from portfolio_front.models import Hero

def seed_hero(seeder):
    seeder.add_entity(Hero, 1, {
        'name': lambda x: "Alex Smith",
        'data_typed_items': lambda x: "Designer, Developer, Freelancer, Photographer"
    })
