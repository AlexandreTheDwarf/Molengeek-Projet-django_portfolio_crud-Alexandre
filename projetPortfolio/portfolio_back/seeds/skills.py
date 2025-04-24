from portfolio_front.models import SkillSection, Skill
import random

def seed_skill_section(seeder):
    seeder.add_entity(SkillSection, 1, {
        'under_title': lambda x: "Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas."
    })

def seed_skills(seeder):
    seeder.add_entity(Skill, 6, {
        'name': lambda x: random.choice(["HTML", "CSS", "JavaScript", "PHP", "WordPress/CMS", "Photoshop"]),
        'percentage': lambda x: random.choice([100, 90, 75, 80, 90, 55])
    })
