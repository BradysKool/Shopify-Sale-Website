from django.core.management.base import BaseCommand, CommandParser
import csv,sys,os
from SaleApp.models import Products

class Command(BaseCommand):
    help = 'csv to database'

    def add_arguments(self, parser):
        pass
    
    def handle(self, *args, **options):
        Products.objects.all().delete()
        with open('C:\\Users\\brady\\OneDrive\\Desktop\\Shopify sale website 2.0\\SaleWebsite\\SaleApp\\management\\commands\\Products.csv') as file:
            render_file = csv.reader(file)
            next(render_file)
            for file in render_file:
                product = Products(
                    brand = file[1],
                    name = file[2],
                    url = file[3],
                    handle = file[4],
                    msrp = file[5],
                    salePrice = file[6],
                    percentOnSale = file[7]
                )
                product.save()