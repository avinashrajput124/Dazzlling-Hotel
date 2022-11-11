from django.urls import path
from ello import views,ApiViews
from ello.ApiViews import hotelListView
from rest_framework.authtoken.views import obtain_auth_token
 

urlpatterns = [
    path("", views.home, name="home.html"),
    path("home", views.home, name="home.html"),
    path("login", views.login_user, name="loginuser"),
    path("users_list/", views.users_list, name="users-list.html"),
    path("user_search", views.user_search, name="user_search.html"),
    path("search", views.search, name='search.html'),
  


    path("edit_hotal/<int:id>", views.edit_hotal, name='edit_hotal'),
    path("update_hotal/<int:id>", views.update_hotal, name='update_hotal'),
    path("delete_hotal/<int:id>", views.delete_hotal, name='delete_hotal'),


    path('hotal_view/<int:id>', views.hotal_view, name="hotal_view"),
    path('list_offers/',views.list_offers, name="list_offers"),
    path('offer_for_you_save',views.offer_for_you_save, name="offer_for_you_save"),
    path('view_offers_new/<int:id>',views.view_offers_new, name="view_offers_new"),
    path('edit_offer/<int:id>/',views.edit_offer, name="edit_offer"),
    path('update_offers',views.update_offers, name="update_offers"),
    path('distroy_view_offers_new/<int:id>',views.distroy_view_offers_new, name="distroy_view_offers_new"),
    path('youtube_video_save',views.youtube_video_save, name="youtube_video_save"),
    path('promotions_save',views.promotions_save, name="promotions_save"),
    path('promotion_list',views.promotion_list, name="promotion_list"),
    path('view_promotion/<int:id>',views.view_promotion, name="view_promotion"),
    path('edit_promotion/<int:id>',views.edit_promotion, name="edit_promotion"),
    path('update_promotion',views.update_promotion, name="update_promotion"),
    path('distroy_whats_new/<int:id>',views.distroy_whats_new, name="distroy_whats_new"),
    path('distroy/<int:id>',views.distroy, name="distroy"),
    path('exclusive_partners_save',views.exclusive_partners_save, name="exclusive_partners_save"),
    path('exclusive_partners_list',views.exclusive_partners_list, name="exclusive_partners_list"),
    path('distroy_exclusive_list/<int:id>',views.distroy_exclusive_list, name="distroy_exclusive_list"),
    path('view_exclusive/<int:id>',views.view_exclusive, name="view_exclusive"),
    path('edit_exclusive/<int:id>',views.edit_exclusive, name="edit_exclusive"),
    path('update_exclusive',views.update_exclusive, name="update_exclusive"),
    path('holiday_packages_save',views.holiday_packages_save, name="holiday_packages_save"),
    path('list_holiday_packages',views.list_holiday_packages, name="list_holiday_packages"),
    path('view_holiday_packages/<int:id>',views.view_holiday_packages, name="view_holiday_packages"),
    path('edit_holiday_packages/<int:id>',views.edit_holiday_packages, name="edit_holiday_packages"),
    path('distroy_holiday_packages/<int:id>',views.distroy_holiday_packages, name="distroy_holiday_packages"),
    path('update_holiday_packages',views.update_holiday_packages, name="update_holiday_packages"),
    path('whats_new_save',views.whats_new_save, name="whats_new_save"),
    path('list_whats_new',views.list_whats_new, name="list_whats_new"),
    path('view_whats_new/<int:id>',views.view_whats_new, name="view_whats_new"),
    path('edit_whats_new/<int:id>',views.edit_whats_new, name="edit_whats_new"),
    path('update_whats_new',views.update_whats_new, name="update_whats_new"),


    path('logout', views.logoutuser, name="handleLogout"),
    path("add_hotel", views.add_hotel, name='add-hotel'),
    path("hotel_list/", views.hotel_list, name='hotel_list'),
    path("hotel_list_filter/", views.hotel_list_filter, name='hotel_list_filter'),
    path("forgot-password", views.forgot_password, name='forgot-password.html'),





#  ---------------------------------login Flow api --------------------------------

    path('register/', ApiViews.registeruser,name="register"),
    path('profile/', ApiViews.profile,name="profile"),
    path('login/', obtain_auth_token,name="login"),
    path('User_logout/', ApiViews.User_logout,name="User_logout"),

    # -------------------------------- hotal api--------------------------------

    path("hotel/",ApiViews.hotel,name='hotel'),
    path("all_promotions/",ApiViews.all_promotions,name='all_promotions'),
    path("all_exclusive_partners/",ApiViews.all_exclusive_partners,name='all_exclusive_partners'),
    path("all_offer_for_you/",ApiViews.all_offer_for_you,name='all_offer_for_you'),
    path("all_holidays_packages/",ApiViews.all_holidays_packages,name='all_holidays_packages'),
    path("all_youtube_video/",ApiViews.all_youtube_video,name='all_youtube_video'),
    path("all_whats_new/",ApiViews.all_whats_new,name='all_whats_new'),
    # path("filter_hotel/",ApiViews.filter_hotel,name='filter_hotel'),

    path("hotelListView/",hotelListView.as_view()),



]