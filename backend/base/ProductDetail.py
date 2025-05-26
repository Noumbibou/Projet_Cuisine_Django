from . import views
from django.shortcuts import render
from .models import Cuisines
from django.views import View 


class ProductDetail(View):
    def get(self,request,idprod):
        cuisine = Cuisines.objects.get(id=idprod)
        return render(request,'productDetail.html',{'element_cuisine':cuisine})

            