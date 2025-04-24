import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetPortfolio.settings')
django.setup()

from portfolio_back.seeds.seed_all import run

if __name__ == '__main__':
    run()