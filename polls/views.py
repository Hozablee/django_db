from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from polls.models import Member, Goods, Basket, Shipment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




def logout_view(request):
    logout(request)
    return home_page(request)

def register(request):
    return render(request, 'register.html')

# --------------------------------link----------------------------------------------

def create_register(request):
    if request.method == 'POST':
        member_register = Member()
        member_register.member_email = request.POST['email']
        member_register.member_pw = request.POST['pwd']
        member_register.member_fname = request.POST['fname']
        member_register.member_lname = request.POST['lname']
        member_register.member_address = request.POST['addr']
        member_register.member_tel = request.POST['tel']
        member_register.save()

        user = User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['pwd'])
        user.last_name = request.POST['lname']
        user.save()

    return login(request,user)

# --------------------------------back end------------------------------------------

def login(request,user):
    context = {'user':user}
    return render(request, 'main.html',context)

def main_page(request):
    return render(request, 'login.html')

# --------------------------------link----------------------------------------------

def check_login(request):
    email   = request.POST.get('email')
    pwd     = request.POST.get('pwd')
    user = authenticate(username=email, password=pwd)
    if user is not None:
    # the password verified for the user
        if user.is_active:
            print(user.is_authenticated())
            return login(request,user)
        else:
            return home_page(request)
    else:
        # the authentication system was unable to verify the username and password
        return home_page(request)

    # if Member.objects.filter(member_email = email,member_pw = pwd):

    #     return main_page(request)
    # else:
    #     return login(request)


# --------------------------------link----------------------------------------------

def home_page(request):
    return render(request,'home.html')

# --------------------------------link----------------------------------------------
# def buying(request):
#     good_detail = Goods.objects.get(goods_name=request.POST['buying'])
#     newBasket = Basket()
#     newBasket.basket_email = 
#     newBasket.basket_goods = good_detail
#     newBasket.basket_price =
#     newBasket.basket_num +=1
#     newBasket.save()
#     return render(request,'goods1.html',context)

def goods1(request,item):
    # print(request.user)
    # is_authenticate = request.user.is_authenticated()
    # print(is_authenticate)
    # if is_authenticate == True:
    username = request.user.username
    good_detail = Goods.objects.get(goods_name=item)
    context = {'good_detail':good_detail}
    return render(request,'goods1.html',context)
    # else:
    #     return home_page(request)


# --------------------------------link----------------------------------------------

# def choice_payment(request):
#     if request.method == 'POST':
#         if Goods.objects.filter(goods_name=name):
#             basket_choose = Basket()
#             basket_choose.basket_name = Goods.objects.get(goods_name=name)
#             basket_choose.basket_num = Goods.objects.get(goods_num=num)
#             basket_choose.basket_price = Goods.objects.get(goods_price=price)
#             basket_choose.save()

#     return show_payment(request)
    


# def show_payment(request,item1):
#         basket_detail = Basket.objects.get(basket_name=item1)
#         context1 = {'basket_detail':basket_detail}

#     return render(request, 'payment.html',context1)


# --------------------------------link----------------------------------------------

def create_shipment(request):
    if request.method == 'POST':
        shipment_data = Shipment()
        shipment_data.shipment_tax = request.POST['tax']

        shipment_data.shipment_date = request.POST['date']

        shipment_data.shipment_time = request.POST['time']

        shipment_data.shipment_sum = request.POST['sum']

        shipment_data.save()

    return show_shipment(request)

def show_shipment(request):
    return render(request, 'shipment.html')


# --------------------------------link----------------------------------------------



