from django.db import models


class BalanceSheetModel(models.Model):

    year = models.DateField(db_column='year')
    stock_name = models.CharField(db_column="stock_name", max_length=255, blank=False, null=False)
    share_capital = models.DecimalField(db_column='share_capital', blank=False, null=False, max_digits=20, decimal_places=2)
    reserve_surplus = models.DecimalField(db_column='reserve_surplus', blank=False, null=False, max_digits=20, decimal_places=2)
    net_worth = models.DecimalField(db_column='net_worth', blank=False, null=False, max_digits=20, decimal_places=2)
    secured_loan = models.DecimalField(db_column='secured_loan', blank=False, null=False, max_digits=20, decimal_places=2)
    unsecured_loan = models.DecimalField(db_column='unsecured_loan', blank=False, null=False, max_digits=20, decimal_places=2)
    gross_block = models.DecimalField(db_column='gross_block', blank=False, null=False, max_digits=20, decimal_places=2)
    depreciation = models.DecimalField(db_column='depreciation', blank=False, null=False, max_digits=20, decimal_places=2)
    net_block = models.DecimalField(db_column='net_block', blank=False, null=False, max_digits=20, decimal_places=2)
    capital_wip = models.DecimalField(db_column='capital_wip', blank=False, null=False, max_digits=20, decimal_places=2)
    investments = models.DecimalField(db_column='investments', blank=False, null=False, max_digits=20, decimal_places=2)
    inventories = models.DecimalField(db_column='inventories', blank=False, null=False, max_digits=20, decimal_places=2)
    sundry_debtors = models.DecimalField(db_column='sundry_debtors', blank=False, null=False, max_digits=20, decimal_places=2)
    cash_and_bank = models.DecimalField(db_column='cash_and_bank', blank=False, null=False, max_digits=20, decimal_places=2)
    loan_and_advances = models.DecimalField(db_column='loan_and_advances', blank=False, null=False, max_digits=20, decimal_places=2)
    total_current_assests = models.DecimalField(db_column='total_current_assests', blank=False, null=False, max_digits=20, decimal_places=2)
    current_liabilities = models.DecimalField(db_column='current_liabilities', blank=False, null=False, max_digits=20, decimal_places=2)
    provisions = models.DecimalField(db_column='provisions', blank=False, null=False, max_digits=20, decimal_places=2)
    total_current_liabilites = models.DecimalField(db_column='total_current_liabilites', blank=False, null=False, max_digits=20, decimal_places=2)
    net_current_assets = models.DecimalField(db_column='net_current_assets', blank=False, null=False, max_digits=20, decimal_places=2)
    misc_expenses = models.DecimalField(db_column='misc_expenses', blank=False, null=False, max_digits=20, decimal_places=2)

    class Meta :
        managed = True
        db_table = 'balance_sheet'
        ordering = ['year']

class ShortBalanceSheetModel(models.Model):
    year = models.DateField(db_column='year')
    stock_name = models.CharField(db_column="stock_name", max_length=255, blank=False, null=False)
    net_worth = models.DecimalField(db_column='net_worth', blank=False, null=False, max_digits=20, decimal_places=2)
    total_liabilities = models.DecimalField(db_column='total_liabilities', blank=False, null=False, max_digits=20, decimal_places=2)
    total_current_assests = models.DecimalField(db_column='total_current_assests', blank=False, null=False,
                                                max_digits=20, decimal_places=2)
    net_current_assets = models.DecimalField(db_column='net_current_assets', blank=False, null=False, max_digits=20,
                                             decimal_places=2)
    total_assets = models.DecimalField(db_column='total_assets', blank=False, null=False, max_digits=20,
                                             decimal_places=2)

    class Meta :
        managed = True
        db_table = 'short_balance_sheet'

