from django.conf import settings
from Product.models import Product
import os
import xlrd
def run():
    data_dir = os.path.join(settings.BASE_DIR, 'data\STock.xls') 
    book = xlrd.open_workbook(data_dir)
    sheet = book.sheet_by_index(0)
    data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(6, sheet.nrows)] 
    # print(data)
    for item in data:
        product = Product()
        product.code = item[0]
        product.name = item[1]
        product.unit = item[2]
        product.stock = item[3]
        product.cost_price = item[8]
        product.m_r_p = item[9]
        product.purchase_price = item[10]
        product.sales_price = item[11]
        product.company = item[12]
        product.save()
