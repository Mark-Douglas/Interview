from django.db import models

# Create your models here.

class Goblincakesales(models.Model):
    """
    The database object model for Goblin' Cakes

    Built automatically through inspectdb and then amended to suit
    """

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', blank=True, null=True, max_length=150)  # Field name made lowercase.
    product_type = models.CharField(db_column='Product_Type', blank=True, null=True, max_length=150)  # Field name made lowercase.
    price_per = models.IntegerField(db_column='Price_Per', blank=True, null=True)  # Field name made lowercase.
    units_sold = models.IntegerField(db_column='Units_Sold', blank=True, null=True)  # Field name made lowercase.
    quarter = models.IntegerField(db_column='Quarter', blank=True, null=True)  # Field name made lowercase.

    headers = ["Product", "Product Type", "Price Per", "Units Sold", "Total Sales Value"]

    product_types = ["Cake", "Canned Drink", "Cookie", "Hot Drink"]

    class Meta:
        managed = False
        db_table = 'GoblinCakeSales'

    def str(self):
        return f"{self.product} - {self.product_type} :" \
        " {self.price_per} sold in quarter {self.quarter}"

    @property
    def total_sales_value(self):
        """
        Return total sales value as unit price times units sold
        """
        return self.price_per * self.units_sold