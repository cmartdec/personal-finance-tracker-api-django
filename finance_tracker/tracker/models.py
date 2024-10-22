from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transacion_type}: {self.amount} on {self.date}"




