from django.urls import path
from . import views
#URL konfiguracija

urlpatterns = [
    path('', views.pocetna, name='pocetna'),
    path('nastambe/', views.nastamba_list, name='nastamba_list'),  # Prikaz svih nastambi
    path('nastambe/<int:id>/', views.nastamba_detail, name='nastamba_detail'),  # Detaljan prikaz nastambe
    path('nastambe/dodaj/', views.nastamba_create, name='nastamba_create'),  # Kreiranje nove nastambe
    path('nastambe/<int:id>/uredi/', views.nastamba_update, name='nastamba_update'),  # Uređivanje nastambe
    path('nastambe/<int:id>/arhiviraj/', views.nastamba_archive, name='nastamba_archive'),  # Arhiviranje nastambe (soft delete)
    path('nastambe/<int:id>/delete/', views.nastamba_delete, name='nastamba_delete'),

    path('zivotinje/', views.zivotinja_list, name='zivotinja_list'),
    path('zivotinje/<int:id>/', views.zivotinja_detail, name='zivotinja_detail'),
    path('zivotinje/dodaj/', views.zivotinja_create, name='zivotinja_create'),
    path('zivotinje/<int:id>/arhiviraj/', views.zivotinja_archive, name='zivotinja_archive'),
    path('zivotinje/<int:id>/uredi/', views.zivotinja_update, name='zivotinja_update'),  # URL za uređivanje životinja
    path('zivotinje/arhivirane',views.arhivirane_zivotinje,name='arhivirane_zivotinje'),
    path('zivotinje/<int:id>/delete/', views.zivotinja_delete, name='zivotinja_delete'),

    path('radnici/', views.radnik_list, name='radnik_list'),
    path('radnici/<int:id>', views.radnik_detail, name='radnik_detail'),
    path('radnici/dodaj/', views.radnik_create, name='radnik_create'),
    path('radnici/<int:id>/delete', views.radnik_delete, name='radnik_delete'),

    path('obaveze/', views.obaveza_list, name='obaveza_list'),
    path('obaveze/dodaj/', views.obaveza_create, name='obaveza_create'),
    path('obaveze/<int:id>/zavrsi/', views.obaveza_complete, name='obaveza_complete'),
    path('obaveza/<int:id>/delete/', views.obaveza_delete, name='obaveza_delete'),

    path('report/zivotinje',views.report_zivotinje,name='report_zivotinje'), # Izvjestaj troskova zivotinja
    path('izvjesca/',views.izvjesca,name='izvjesca'),
    path('izvjesca/nezgoda',views.nezgoda_list,name='nezgoda_list'),
    path('izvjesca/nezgoda/dodaj',views.nezgoda_create,name='nezgoda_create'),
    path('izvjesca/trosak/dodaj',views.trosak_create,name='trosak_create'),

]
