from dapur import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
#views adalah file /class
#home adalah function/method
#'' =root directory


    path('', views.masuk, name='masuk'),
    path('regist', views.regist, name="regist"),
    path('masuk', views.masuk, name="masuk"),
    path('keluar', views.keluar, name="keluar"),
    path('homeuser2', views.homeuser2, name="homeuser2"),
    path('homeuser1', views.homeuser1, name="homeuser1"),
    path('homeuser1_a', views.homeuser1_a, name="homeuser1_a"),
    path('homeuser1_b', views.homeuser1_b, name="homeuser1_b"),
# bagian surat masuk
    path('tmbhsurat', views.tmbhsurat, name="tmbhsurat"),
    path('shkotakmasuk', views.shkotakmasuk, name="shkotakmasuk"),
    path('kotakmasuk22', views.kotakmasuk22, name="kotakmasuk22"),
    path('shkotakmasuk/<int:pk>/', views.updatekotakmasuk, name="updatekotakmasuk"),
    path('delete/<int:nsurat>', views.Dkotakmasuk),
# bagian disposisi
    path('disposisi', views.dis1, name="dis1"),
    path('dis/<int:pk>/', views.dis, name="dis"),
    path('shdis/<int:pk>/', views.shdis, name="shdis"),
    path('shdis2/<int:pk>/', views.shdis2, name="shdis2"),
    path('canceldis/<int:pk>/', views.canceldis, name="canceldis"),

    path('sharsip', views.sharsip, name="sharsip"),
    path('k_sharsip', views.k_sharsip, name="k_sharsip"),
    path('arsipkan/<int:pk>/', views.arsipkan, name="arsipkan"),
    path('k_arsipkan/<int:pk>/', views.k_arsipkan, name="k_arsipkan"),
    path('noarsipkan/<int:pk>/', views.noarsipkan, name="noarsipkan"),
    path('k_noarsipkan/<int:pk>/', views.k_noarsipkan, name="k_noarsipkan"),
    # path('dis/<int:nsurat>/disposisi22/', views.disposisi22, name="disposisi22"),
# bagian surat KELUAR 
    path('shkotakkeluar', views.shkotakkeluar, name="shkotakkeluar"),
    path('tmbhsuratkeluar', views.tmbhsuratkeluar, name="tmbhsuratkeluar"),
    path('svkotakkeluar', views.svkotakkeluar, name="svkotakkeluar"),
    path('shkotakkeluar/<int:nsurat>/', views.updatekotakkeluar, name="updatekotakkeluar"),
    path('k_delete/<int:nsurat>', views.Dkotakeluar),
# bagian dashboard halaman utama
    path('a',views.a, name="a"),

    # path('shkotakmasukarsip', views.shkotakmasukarsip, name="shkotakmasukarsip"),

]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

