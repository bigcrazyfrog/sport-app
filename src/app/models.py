from app.internal.db.models.admin_user import AdminUser
from app.internal.db.models.allergens import Allergen
from app.internal.db.models.products import Product
from app.internal.db.models.menu import Menu, Recommendation

# for menu in Menu.objects.all():
#     for i in range(14):
#         Recommendation.objects.create(menu=menu, day=i+1,
#                                       breakfast=Product.objects.order_by('?').first(),
#                                       lunch=Product.objects.order_by('?').first(),
#                                       dinner=Product.objects.order_by('?').first(),
#                                       )
