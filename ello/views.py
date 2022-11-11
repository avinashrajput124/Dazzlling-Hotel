from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from ello.models import Add_Hotal,promotions,exclusive_partners,Holiday_packages, whats_new,offer_for_you, youtube_video
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ello.models import User
from django.contrib.auth import get_user_model
import math
from django.core.paginator  import Paginator
import math
from ello.decorator import admin_required

User = get_user_model()



@admin_required()
def home(request):
       hotal = Add_Hotal.objects.all().order_by('-Hotal_Name')[:6]
       perm = {'hotal':hotal}

       return render(request, "home.html", perm)

@admin_required()
def users_list(request):
       
       no_of_posts = 7
       print(request.GET)
       page = request.GET.get('page')
       if page is None:
           page = 1
       else:
           page = int(page)
      


       '''This function is used to access the data from the database and sending it to the frontend.'''
       user_all = User.objects.all()
       
       length = len(user_all)
       user_all = user_all[(page-1)*no_of_posts: page*no_of_posts]
        
       if page>1:
           prev = page-1
       else:
           prev = None
       
       if page<math.ceil(length/no_of_posts):
           nxt = page + 1
       else:
           nxt = None


       params = {'user_all' : user_all,'prev' : prev, 'nxt' : nxt}

       return render(request, "users-list.html", params)



# def user_filter(request):
#        # hotal = Add_Hotal.objects.all()
#        # user_all = User.objects.all()
#        query = request.GET['query']
#        user_all = User.objects.filter(username__icontains=query)

#        context = {'user_all' : user_all}
#        return render(request, 'user_search.html', context)

       

@admin_required()
def forgot_password(request):
       return render(request, "forgot-password.html")



def login_user(request):
       print('xxxxxxxxxxxxxxx')
       print(request.POST)
       if request.method=="GET":
              print('helo')
           
        # Get the post parameters
              username = request.GET.get('username')
              password = request.GET.get('password')
              print(username)
              print(password)
              # check for errorneous input
              user = authenticate(username = username, password = password)
              print(user)
              if user is not None:
                     login(request, user)
                     return redirect('/home')
       return render(request, "login.html")


@admin_required()
def search(request):
       x = Add_Hotal.objects.all()
       tottal_hotal = len(x)
       # hotal = Add_Hotal.objects.all()
       query = request.GET['query']
       hotal = Add_Hotal.objects.filter(Hotal_Name__icontains=query)

       context = {'hotal' : hotal, 'tottal_hotal':tottal_hotal}
       return render(request, 'search.html', context)

@admin_required()
def user_search(request):
       # hotal = Add_Hotal.objects.all()
       # user_all = User.objects.all()
       query = request.GET['query']
       user_all = User.objects.filter(username__icontains=query)

       context = {'user_all' : user_all}
       return render(request, 'user_search.html', context)




@admin_required()
def hotal_view(request, id):
      
       if request.method=="POST":
              hotal = Add_Hotal.objects.all()
              Hotal_id = Add_Hotal.objects.get(pk=id)

              
              cotext = {'Hotal_id':Hotal_id, 'hotal':hotal}

              return render(request, 'shop-description.html', cotext)
       return render(request, "shop-description.html")

@admin_required()
def hotel_list(request):
       x = Add_Hotal.objects.all().order_by('-Hotal_Name')
       paginator=Paginator(x,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       tottal_hotal = len(x)     
       no_of_posts = 3
       page = request.GET.get('page')
       if page is None:
           page = 1
       else:
           page = int(page)
      


       # '''This function is used to access the data from the database and sending it to the frontend.'''
       hotal = Add_Hotal.objects.all()
       
       length = len(hotal)
       hotal = hotal[(page-1)*no_of_posts: page*no_of_posts]
       
       if page>1:
           prev = page-1
       else:
           prev = None
       
       if page<math.ceil(length/no_of_posts):
           nxt = page + 1
       else:
           nxt = None



       params = {'hotal' : hotal,'datafinal':datafinal,'page_number':page_number,'tottal_hotal':tottal_hotal}
       return render(request, "hotel-list.html", params)


@admin_required()
def hotel_list_filter(request):
       
       x = Add_Hotal.objects.all()
       tottal_hotal = len(x)

       print(request.GET)
       hello = request.GET.get('resently_added')
       if request.method=="GET":
              if hello is None:
                     hello = Add_Hotal.objects.all()
              else:
                     hello = str(hello)
              if hello == 'newfirst':
                     hotal = Add_Hotal.objects.all().order_by("-Hotal_id")
              if hello == 'oldfirst':
                     hotal = Add_Hotal.objects.all().order_by("Hotal_id")
              elif hello == 'a_to_z':
                     hotal = Add_Hotal.objects.all().order_by('Hotal_Name')
              elif hello == 'z_to_a':
                     hotal = Add_Hotal.objects.all().order_by('-Hotal_Name')
              elif hello == 'price_low_to_hight':
                     hotal = Add_Hotal.objects.all().order_by('hotal_new_price')
              elif hello == 'price_high_to_low':
                     hotal = Add_Hotal.objects.all().order_by('-hotal_new_price')
              elif hello == '5-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=5)
              elif hello == '4-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=4)
              elif hello == '3-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=3)
              elif hello == '2-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=2)
              elif hello == '1-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=1)
              elif hello == '0-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=0)
              else:
                     hotal = Add_Hotal.objects.all()
                     
       

       params = {'hotal' : hotal,'tottal_hotal':tottal_hotal}
       return render(request, "hotel_list_filter.html", params)

@admin_required()
def add_hotel(request):
       if request.method == "POST":
              # Hotal_id = request.POST.get('Hotal_id')
              Hotal_Name = request.POST.get('hotalname')
              hotal_new_price = request.POST.get('newprice')
              hotal_new_price_premium = request.POST.get('hotal_new_price_premium')
              hotal_discreption = request.POST.get('dec')
              Hotal_Location = request.POST.get('loc')
              Hotal_Latitude = request.POST.get('lat')
              Hotal_Longitude = request.POST.get('long')
              Hotal_images1 = request.FILES.get('Hotal_images1')
              # recettion images
              reception_images1 = request.FILES.get('reception_images1')
              reception_images2 = request.FILES.get('reception_images2')
              reception_images3 = request.FILES.get('reception_images3')
              reception_images4= request.FILES.get('reception_images4')
              reception_images5 = request.FILES.get('reception_images5')
              # bedroom images
              bedroom_images1 = request.FILES.get('bedroom_images1')
              bedroom_images2 = request.FILES.get('bedroom_images2')
              bedroom_images3 = request.FILES.get('bedroom_images3')
              bedroom_images4= request.FILES.get('bedroom_images4')
              bedroom_images5 = request.FILES.get('bedroom_images5')
              # washroom images
              washroom_images1 = request.FILES.get('washroom_images1')
              washroom_images2 = request.FILES.get('washroom_images2')
              washroom_images3 = request.FILES.get('washroom_images3')
              washroom_images4= request.FILES.get('washroom_images4')
              washroom_images5 = request.FILES.get('washroom_images5')
              # exterior images
              Exterior_images1 = request.FILES.get('Exterior_images1')
              Exterior_images2 = request.FILES.get('Exterior_images2')
              Exterior_images3 = request.FILES.get('Exterior_images3')
              Exterior_images4= request.FILES.get('Exterior_images4')
              Exterior_images5 = request.FILES.get('Exterior_images5')
              # garden images
              garden_images1 = request.FILES.get('garden_images1')
              garden_images2 = request.FILES.get('garden_images2')
              garden_images3 = request.FILES.get('garden_images3')
              garden_images4= request.FILES.get('garden_images4')
              garden_images5 = request.FILES.get('garden_images5')
              date = request.POST.get('datetime.today()')

              data = Add_Hotal(Hotal_Name=Hotal_Name, hotal_new_price=hotal_new_price,hotal_new_price_premium=hotal_new_price_premium,
              hotal_discreption = hotal_discreption, Hotal_Location=Hotal_Location, Hotal_Latitude=Hotal_Latitude, Hotal_Longitude=Hotal_Longitude, Hotal_images1=Hotal_images1,
               date=date,
              reception_images1=reception_images1,reception_images2=reception_images2,reception_images3=reception_images3,reception_images4=reception_images4,reception_images5=reception_images5,
              bedroom_images1=bedroom_images1,bedroom_images2=bedroom_images2,bedroom_images3=bedroom_images3,bedroom_images4=bedroom_images4,bedroom_images5=bedroom_images5,
              washroom_images1=washroom_images1,washroom_images2=washroom_images2,washroom_images3=washroom_images3,washroom_images4=washroom_images4,washroom_images5=washroom_images5,
              Exterior_images1=Exterior_images1,Exterior_images2=Exterior_images2,Exterior_images3=Exterior_images3,Exterior_images4=Exterior_images4,Exterior_images5=Exterior_images5,
              garden_images1=garden_images1,garden_images2=garden_images2,garden_images3=garden_images3,garden_images4=garden_images4,garden_images5=garden_images5, 
              )
       
              data.save()
              messages.success(request,'Hotel Added Sucessfully')
              return redirect('hotel_list')
       return render(request, "add-hotel.html")



@admin_required()
def logoutuser(request):
       logout(request)
       return redirect('login')



@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('hotel-list')

@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('search')

@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('hotel_list_filter')


@admin_required()
def update_hotal(request, id):
       if request.method=="POST":
              update = Add_Hotal.objects.all()
              Hotal_id = Add_Hotal.objects.get(pk=id)
              cotext = {'Hotal_id':Hotal_id, 'update':update}
              return render(request, 'update_hotal.html', cotext)
@admin_required()
def edit_hotal(request, id):
       update=Add_Hotal.objects.get(Hotal_id=id)
       if request.method == "POST":
              if request.POST.get('hotalname') is not None:
                     update.Hotal_Name = request.POST.get('hotalname')
                     
              else:
                     update.Hotal_Name = update.Hotal_Name
              if request.POST.get('newprice') is not None:
                     update.hotal_new_price = request.POST.get('newprice')
                     
              else:
                     update.hotal_new_price = update.hotal_new_price
              if request.POST.get('hotal_new_price_premium') is not None:
                     update.hotal_new_price_premium = request.POST.get('hotal_new_price_premium')
                     
              else:
                     update.hotal_new_price_premium = update.hotal_new_price_premium
              if request.POST.get('dec') is not None:
                     update.hotal_discreption = request.POST.get('dec')
                     
              else:
                     update.hotal_discreption = update.hotal_discreption
              if request.POST.get('loc') is not None:
                     update.Hotal_Location = request.POST.get('loc')
                     
              else:
                     update.Hotal_Location = update.Hotal_Location
              if request.POST.get('lat') is not None:
                     update.Hotal_Latitude = request.POST.get('lat')
                     
              else:
                     update.Hotal_Latitude = update.Hotal_Latitude
              if request.POST.get('long') is not None:
                     update.Hotal_Longitude = request.POST.get('long')
                     
              else:
                     update.Hotal_Longitude = update.Hotal_Longitude

              #  banner images
              if request.FILES.get('Hotal_images1') is not None:
                     update.Hotal_images1 = request.FILES.get('Hotal_images1')
                     
              else:
                     update.Hotal_images1 = update.Hotal_images1
              
              # reception images

              if request.FILES.get('reception_images1') is not None:
                     update.reception_images1 = request.FILES.get('reception_images1')
                     
              else:
                     update.reception_images1 = update.reception_images1

              if request.FILES.get('reception_images2') is not None:
                     update.reception_images2 = request.FILES.get('reception_images2')
                     
              else:
                     update.reception_images2 = update.reception_images2
              if request.FILES.get('reception_images3') is not None:
                     update.reception_images3 = request.FILES.get('reception_images3')
                     
              else:
                     update.reception_images3 = update.reception_images3

              if request.FILES.get('reception_images4') is not None:
                     update.reception_images4 = request.FILES.get('reception_images4')
                     
              else:
                     update.reception_images4 = update.reception_images4
              if request.FILES.get('reception_images5') is not None:
                     update.reception_images5 = request.FILES.get('reception_images5')
                     
              else:
                     update.reception_images5 = update.reception_images5

              # bedroom images
              if request.FILES.get('bedroom_images1') is not None:
                     update.bedroom_images1 = request.FILES.get('bedroom_images1')
                     
              else:
                     update.bedroom_images1 = update.bedroom_images1
              if request.FILES.get('bedroom_images2') is not None:
                     update.bedroom_images2 = request.FILES.get('bedroom_images2')
                     
              else:
                     update.bedroom_images2 = update.bedroom_images2
              if request.FILES.get('bedroom_images3') is not None:
                     update.bedroom_images3 = request.FILES.get('bedroom_images3')
                     
              else:
                     update.bedroom_images3 = update.bedroom_images3
              if request.FILES.get('bedroom_images4') is not None:
                     update.bedroom_images4 = request.FILES.get('bedroom_images4')
                     
              else:
                     update.bedroom_images4 = update.bedroom_images4
              if request.FILES.get('bedroom_images5') is not None:
                     update.bedroom_images5 = request.FILES.get('bedroom_images5')
                     
              else:
                     update.bedroom_images5 = update.bedroom_images5

              # washroom images

              if request.FILES.get('washroom_images1') is not None:
                     update.washroom_images1 = request.FILES.get('washroom_images1')
                     
              else:
                     update.washroom_images1 = update.washroom_images1
              if request.FILES.get('washroom_images2') is not None:
                     update.washroom_images2 = request.FILES.get('washroom_images2')
                     
              else:
                     update.washroom_images2 = update.washroom_images2

              if request.FILES.get('washroom_images3') is not None:
                     update.washroom_images3 = request.FILES.get('washroom_images3')
                     
              else:
                     update.washroom_images3 = update.washroom_images3
              if request.FILES.get('washroom_images4') is not None:
                     update.washroom_images4 = request.FILES.get('washroom_images4')
                     
              else:
                     update.washroom_images4 = update.washroom_images4
              if request.FILES.get('washroom_images5') is not None:
                     update.washroom_images5 = request.FILES.get('washroom_images5')
                     
              else:
                     update.washroom_images5 = update.washroom_images5


              # exterior images


              if request.FILES.get('Exterior_images1') is not None:
                     update.Exterior_images1 = request.FILES.get('Exterior_images1')
                     
              else:
                     update.Exterior_images1 = update.Exterior_images1

              if request.FILES.get('Exterior_images2') is not None:
                     update.Exterior_images2 = request.FILES.get('Exterior_images2')
                     
              else:
                     update.Exterior_images2 = update.Exterior_images2
              if request.FILES.get('Exterior_images3') is not None:
                     update.Exterior_images3 = request.FILES.get('Exterior_images3')
                     
              else:
                     update.Exterior_images3 = update.Exterior_images3
                     
              if request.FILES.get('Exterior_images4') is not None:
                     update.Exterior_images4 = request.FILES.get('Exterior_images4')
                     
              else:
                     update.Exterior_images4 = update.Exterior_images4

              if request.FILES.get('Exterior_images5') is not None:
                     update.Exterior_images5 = request.FILES.get('Exterior_images5')
                     
              else:
                     update.Exterior_images5 = update.Exterior_images5

              # garden images
              
              if request.FILES.get('garden_images1') is not None:
                     update.garden_images1 = request.FILES.get('garden_images1')
                     
              else:
                     update.garden_images1 = update.garden_images1

              if request.FILES.get('garden_images2') is not None:
                     update.garden_images2 = request.FILES.get('garden_images2')
                     
              else:
                     update.garden_images2 = update.garden_images2

              if request.FILES.get('garden_images3') is not None:
                     update.garden_images3 = request.FILES.get('garden_images3')
                     
              else:
                     update.garden_images3 = update.garden_images3
              if request.FILES.get('garden_images4') is not None:
                     update.garden_images4 = request.FILES.get('garden_images4')
                     
              else:
                     update.garden_images4 = update.garden_images4
              if request.FILES.get('garden_images5') is not None:
                     update.garden_images5 = request.FILES.get('garden_images5')
                     
              else:
                     update.garden_images5 = update.garden_images5
              if request.POST.get('datetime.today()') is not None:
                     update.date = request.POST.get('datetime.today()')
                     
              else:
                     update.date = update.date
              update.save()
              messages.success(request,'Data Updated Sucessfully')
              return redirect('hotel_list')
       return render(request, 'update_hotal.html') 




#---------------------------------------------Start Promotions---------------------------------------------------
@admin_required()
def promotions_save(request):
       if request.method=="POST":
              hotel_name=request.POST.get('hotel_name')
              promotions_Details=request.POST.get('promotions_Details')
              promotions_images1=request.FILES.get('promotions_images1')
              promotions_images2=request.FILES.get('promotions_images2')
              promotions_images3=request.FILES.get('promotions_images3')
              promotions_images4=request.FILES.get('promotions_images4')
              date = request.POST.get('datetime.today()')
              data=promotions(promotions_Details=promotions_Details,hotel_name=hotel_name,promotions_images1=promotions_images1,promotions_images2=promotions_images2,promotions_images3=promotions_images3,promotions_images4=promotions_images4,date=date)
              data.save()
              messages.success(request,'Promotion save sucessfully')
              return redirect('promotions_save')
       return render(request,'promotions.html')

@admin_required()
def promotion_list(request):
       data=promotions.objects.all().order_by('-id')
       paginator=Paginator(data,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       return render(request,'promotion_list.html',{'data':data,'datafinal':datafinal,'page_number':page_number})

@admin_required()
def view_promotion(request,id):
       Hotal_id=promotions.objects.get(pk=id)
       return render(request,'view_promotions.html',{'Hotal_id':Hotal_id})

@admin_required()
def edit_promotion(request,id):
       data=promotions.objects.get(pk=id)
       return render(request,'edit_promotion.html',{'data':data})

@admin_required()
def update_promotion(request):
       if request.method=="POST":
              id=request.POST.get('id')
              hotel_name=request.POST.get('hotel_name')
              promotions_Details=request.POST.get('promotions_Details')
              update=promotions.objects.get(id=id)
              if request.FILES.get('promotions_images1') is not None:
                     update.promotions_images1 = request.FILES.get('promotions_images1')
              else:
                     update.promotions_images1 = update.promotions_images1
              if request.FILES.get('promotions_images2') is not None:
                     update.promotions_images2 = request.FILES.get('promotions_images2')
              else:
                     update.promotions_images2 = update.promotions_images2
              if request.FILES.get('promotions_images3') is not None:
                     update.promotions_images3 = request.FILES.get('promotions_images3')
              else:
                     update.promotions_images3 = update.promotions_images3
              if request.FILES.get('promotions_images4') is not None:
                     update.promotions_images4 = request.FILES.get('promotions_images4')
              else:
                     update.promotions_images4 = update.promotions_images4
              date = request.POST.get('datetime.today()')
              data=promotions(id=id,hotel_name=hotel_name,promotions_Details=promotions_Details,date=date)
              data.save()
              messages.success(request,'Promotion save sucessfully')
              update.save()
              return redirect('promotion_list')
       return render(request,'edit_promotion.html')

@admin_required()
def distroy(request,id):
       data=promotions.objects.get(pk=id)
       data.delete()
       messages.success(request,'Promotion Delete Sucessfully')
       return redirect('promotion_list')
#  -----------------------------------------End Promotion-------------------------------------------------------------------

# -----------------------------------------Start Exclusive Partners-------------------------------------------------------

@admin_required()
def exclusive_partners_save(request):
       if request.method=="POST":
              exclusive_partners_images1=request.FILES.get('exclusive_partners_images1')
              exclusive_partners_images2=request.FILES.get('exclusive_partners_images2')
              exclusive_partners_images3=request.FILES.get('exclusive_partners_images3')
              exclusive_partners_images4=request.FILES.get('exclusive_partners_images4')
              exclusive_partners_Details=request.POST.get('exclusive_partners_Details')
              date = request.POST.get('datetime.today()')
              data=exclusive_partners(exclusive_partners_Details=exclusive_partners_Details,exclusive_partners_images1=exclusive_partners_images1,exclusive_partners_images2=exclusive_partners_images2,exclusive_partners_images3=exclusive_partners_images3,exclusive_partners_images4=exclusive_partners_images4,date=date)
              data.save()
              messages.success(request,'Exclusive Partners Save Sucessfully')
              return redirect('exclusive_partners_save')
       return render(request,'exclusive_partners.html')

@admin_required()
def exclusive_partners_list(request):
       data=exclusive_partners.objects.all().order_by('-id')
       paginator=Paginator(data,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       return render(request,'list_exclusive_partners.html',{'data':data,'datafinal':datafinal,'page_number':page_number})


@admin_required()
def view_exclusive(request,id):
       Hotal_id=exclusive_partners.objects.get(pk=id)
       return render(request,'view_exclusives.html',{'Hotal_id':Hotal_id})

@admin_required()
def edit_exclusive(request,id):
       data=exclusive_partners.objects.get(pk=id)
       return render(request,'edit_exclusive_partners.html',{'data':data})

@admin_required()
def distroy_exclusive_list(request,id):
       data=exclusive_partners.objects.get(pk=id)
       data.delete()
       messages.success(request,'Exclusive Partners Deleted Sucessfully')
       return redirect('exclusive_partners_list')

@admin_required()
def update_exclusive(request):
       if request.method=="POST":
              id=request.POST.get('id')
              update=exclusive_partners.objects.get(id=id)
              if request.FILES.get('exclusive_partners_images1') is not None:
                     update.exclusive_partners_images1 = request.FILES.get('exclusive_partners_images1')
              else:
                     update.exclusive_partners_images1 = update.exclusive_partners_images1
              if request.FILES.get('exclusive_partners_images2') is not None:
                     update.exclusive_partners_images2 = request.FILES.get('exclusive_partners_images2')
              else:
                     update.exclusive_partners_images2 = update.exclusive_partners_images2
              if request.FILES.get('exclusive_partners_images3') is not None:
                     update.exclusive_partners_images3 = request.FILES.get('exclusive_partners_images3')
              else:
                     update.exclusive_partners_images3 = update.exclusive_partners_images3
              if request.FILES.get('exclusive_partners_images4') is not None:
                     update.exclusive_partners_images4 = request.FILES.get('exclusive_partners_images4')
              else:
                     update.exclusive_partners_images4 = update.exclusive_partners_images4
              exclusive_partners_Details=request.POST.get('exclusive_partners_Details')
              date = request.POST.get('datetime.today()')
              data=exclusive_partners(id=id,exclusive_partners_Details=exclusive_partners_Details,date=date)
              data.save()
              messages.success(request,'Exclusive Partners Update Sucessfully')
              update.save()
              return redirect('exclusive_partners_list')
       return render(request,'edit_exclusive_partners.html')

#-------------------------------------------End Exclusive Partners------------------------------------------------------

# ----------------------------------------------Start Holiday Packages------------------------------
@admin_required()
def holiday_packages_save(request):
       if request.method=="POST":
              Holiday_packages_images1=request.FILES.get('Holiday_packages_images1')
              Holiday_packages_images2=request.FILES.get('Holiday_packages_images2')
              Holiday_packages_images3=request.FILES.get('Holiday_packages_images3')
              Holiday_packages_images4=request.FILES.get('Holiday_packages_images4')
              Holiday_packages_Details=request.POST.get('Holiday_packages_Details')
              date = request.POST.get('datetime.today()')
              data=Holiday_packages(Holiday_packages_Details=Holiday_packages_Details,Holiday_packages_images1=Holiday_packages_images1,Holiday_packages_images2=Holiday_packages_images2,Holiday_packages_images3=Holiday_packages_images3,Holiday_packages_images4=Holiday_packages_images4,date=date)
              data.save()
              messages.success(request,'Holidays Package Uploaded Sucessfully')
              return render(request,'holiday_packages.html')
       return render(request,'holiday_packages.html')


@admin_required()
def list_holiday_packages(request):
       data=Holiday_packages.objects.all().order_by('-id')
       paginator=Paginator(data,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       return render(request,'list_holiday_packages.html',{'data':data,'datafinal':datafinal,'page_number':page_number})


@admin_required()
def view_holiday_packages(request,id):
       Hotal_id=Holiday_packages.objects.get(pk=id)
       return render(request,'view_holday_packages.html',{'Hotal_id':Hotal_id})


@admin_required()
def edit_holiday_packages(request,id):
       data=Holiday_packages.objects.get(pk=id)
       return render(request,'edit_holiday_packages.html',{'data':data})


@admin_required()
def distroy_holiday_packages(request,id):
       data=Holiday_packages.objects.get(pk=id)
       data.delete()
       messages.success(request,'Holidays Package Deleted Sucessfully')
       return redirect('list_holiday_packages')

@admin_required()
def update_holiday_packages(request):
       if request.method=="POST":
              id=request.POST.get('id')
              update=Holiday_packages.objects.get(id=id)
              if request.FILES.get('Holiday_packages_images1') is not None:
                     update.Holiday_packages_images1 = request.FILES.get('Holiday_packages_images1')
              else:
                     update.Holiday_packages_images1 = update.Holiday_packages_images1
              if request.FILES.get('Holiday_packages_images2') is not None:
                     update.Holiday_packages_images2 = request.FILES.get('Holiday_packages_images2')
              else:
                     update.Holiday_packages_images2 = update.Holiday_packages_images2
              if request.FILES.get('Holiday_packages_images3') is not None:
                     update.Holiday_packages_images3 = request.FILES.get('Holiday_packages_images3')
              else:
                     update.Holiday_packages_images3 = update.Holiday_packages_images3
              if request.FILES.get('Holiday_packages_images4') is not None:
                     update.Holiday_packages_images4 = request.FILES.get('Holiday_packages_images4')
              else:
                     update.Holiday_packages_images4 = update.Holiday_packages_images4
              Holiday_packages_Details=request.POST.get('Holiday_packages_Details')
              date = request.POST.get('datetime.today()')
              data=Holiday_packages(id=id,Holiday_packages_Details=Holiday_packages_Details,date=date)
              data.save()
              messages.success(request,'Holidays Package Updated Sucessfully')
              update.save()
              return redirect('list_holiday_packages')
       return redirect('edit_holiday_packages')

# -----------------------------------------------End Holidays Packages----------------------------------------------------------


#  -------------------------------------------- Start whats new----------------------------------------------------------------
@admin_required()
def whats_new_save(request):
       if request.method=="POST":
              whats_new_images1=request.FILES.get('whats_new_images1')
              whats_new_images2=request.FILES.get('whats_new_images2')
              whats_new_images3=request.FILES.get('whats_new_images3')
              whats_new_images4=request.FILES.get('whats_new_images4')
              whats_new_details=request.POST.get('whats_new_details')
              date = request.POST.get('datetime.today()')
              data=whats_new(whats_new_images1=whats_new_images1,whats_new_images2=whats_new_images2,whats_new_images3=whats_new_images3,whats_new_images4=whats_new_images4,whats_new_details=whats_new_details,date=date)
              data.save()
              messages.success(request,'Whats New Added Sucessfully')
              return render(request,'whats_new_save.html')
       return render(request,'whats_new_save.html')

       
@admin_required()
def list_whats_new(request):
       data=whats_new.objects.all().order_by('-id')
       paginator=Paginator(data,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       return render(request,'list_whats_new.html',{'data':data,'datafinal':datafinal,'page_number':page_number})

@admin_required()
def view_whats_new(request,id):
       Hotal_id=whats_new.objects.get(pk=id)
       return render(request,'view_whats_new.html',{'Hotal_id':Hotal_id})

@admin_required()
def edit_whats_new(request,id):
       data=whats_new.objects.get(pk=id)
       return render(request,'edit_whats_new.html',{'data':data})

@admin_required()
def distroy_whats_new(request,id):
       data=whats_new.objects.get(pk=id)
       data.delete()
       messages.success(request,'Whats New Deleted Sucessfully')
       return redirect('list_whats_new')

@admin_required()
def update_whats_new(request):
       if request.method=="POST":
              id=request.POST.get('id')
              update=whats_new.objects.get(id=id)
              if request.FILES.get('whats_new_images1') is not None:
                     update.whats_new_images1 = request.FILES.get('whats_new_images1')
              else:
                     update.whats_new_images1 = update.whats_new_images1
              if request.FILES.get('whats_new_images2') is not None:
                     update.whats_new_images2 = request.FILES.get('whats_new_images2')
              else:
                     update.whats_new_images2 = update.whats_new_images2
              if request.FILES.get('whats_new_images3') is not None:
                     update.whats_new_images3 = request.FILES.get('whats_new_images3')
              else:
                     update.whats_new_images3 = update.whats_new_images3
              if request.FILES.get('whats_new_images4') is not None:
                     update.whats_new_images4 = request.FILES.get('whats_new_images4')
              else:
                     update.whats_new_images4 = update.whats_new_images4
              whats_new_details=request.POST.get('whats_new_details')
              date = request.POST.get('datetime.today()')
              data=whats_new(id=id,whats_new_details=whats_new_details,date=date)
              data.save()
              messages.success(request,'Whats New Updated Sucessfully')
              update.save()
              return redirect('list_whats_new')
       return redirect('edit_holiday_packages')


# ---------------------------------------------End Whats New-------------------------------------------------------------------

# ----------------------------------------------Start Offer For You--------------------------------------------------------------
@admin_required()
def offer_for_you_save(request):
       if request.method == "POST":
              offer_for_you_pic = request.FILES.get('offer_for_you_pic')
              print(offer_for_you_pic)
              first_time_book = request.POST.get('first_time_book')
              coupon_code = request.POST.get('coupon_code')
              offer_Details = request.POST.get('offer_Details')
              date = request.POST.get('datetime.today()')
              data=offer_for_you(date=date,offer_for_you_pic=offer_for_you_pic,first_time_book=first_time_book,coupon_code=coupon_code,offer_Details=offer_Details)
              data.save()
              messages.success(request,'Offer Upload Sucessfully')
              return redirect('offer_for_you_save')
       return render(request,'offers_for_you.html')


@admin_required()
def list_offers(request):
       data=offer_for_you.objects.all().order_by('-id')
       paginator=Paginator(data,6)
       page_number=request.GET.get('page')
       datafinal=paginator.get_page(page_number)
       return render(request,'list_offer_for_you.html',{'datafinal':datafinal,'data':data,'page_number':page_number})

@admin_required()
def view_offers_new(request,id):
       Hotal_id=offer_for_you.objects.get(pk=id)
       return render(request,'blog.html',{'Hotal_id':Hotal_id})

@admin_required()       
def edit_offer(request,id):
       data=offer_for_you.objects.get(pk=id)
       return render(request,'edit_offers.html',{'data':data})

@admin_required()
def update_offers(request):
       if request.method=="POST":
              id=request.POST.get('id')
              update=offer_for_you.objects.get(id=id)
              if request.FILES.get('offer_for_you_pic') is not None:
                     update.offer_for_you_pic = request.FILES.get('offer_for_you_pic')
              else:
                     update.offer_for_you_pic = update.offer_for_you_pic
              first_time_book = request.POST.get('first_time_book')
              coupon_code = request.POST.get('coupon_code')
              offer_Details = request.POST.get('offer_Details')
              date = request.POST.get('datetime.today()')
              data=offer_for_you(id=id,first_time_book=first_time_book,coupon_code=coupon_code,offer_Details=offer_Details,date=date)
              data.save()
              messages.success(request,'Offer Update Sucessfully')
              update.save()
              return redirect('list_offers')
       return redirect('edit_offer')


@admin_required()
def distroy_view_offers_new(request,id):
       data=offer_for_you.objects.get(pk=id)
       data.delete()
       messages.success(request,'Offer Deleted Sucessfully')
       return redirect('list_offers')


# ---------------------------------------------End Offer For You-----------------------------------------------------------------------

# ---------------------------------------------Start Yotube Video-------------------------------------------------------------------

@admin_required()
def youtube_video_save(request):
       if request.method=="POST":
              hotel_name=request.POST.get('hotel_name')
              location=request.POST.get('location')
              link=request.POST.get('link')
              youtube_video_Details=request.POST.get('youtube_video_Details')
              date = request.POST.get('datetime.today()')
              data=youtube_video(hotel_name=hotel_name,location=location,link=link,youtube_video_Details=youtube_video_Details,date=date)
              data.save()
              messages.success(request,'Youtube Video Save Sucessfullly')
              return redirect('youtube_video_save')
       return render (request,'youtubevideo_save.html')
# --------------------------------------------End Youtube Video----------------------