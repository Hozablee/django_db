from django.contrib import admin

from .models import Question

admin.site.register(Question)

from .models import Member

admin.site.register(Member)

from .models import Goods

admin.site.register(Goods)

from .models import Basket

admin.site.register(Basket)

from .models import Shipment

admin.site.register(Shipment)



# ------------------------user in to database-----------------------------