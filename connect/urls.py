from django.urls import path
from connect import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add_admin/',views.add_admin,name="add_admin"),
    path('save_admin/', views.save_admin, name="save_admin"),
    path('view_admin/', views.display_admins, name="view_admin"),
    path('edt_adm/<int:dataid>/', views.edt_adm, name="edt_adm"),
    path('update_admin/<int:dataid>/', views.update_admin, name="update_admin"),
    path('delete_admin/<int:dataid>/', views.delete_admin, name="delete_admin"),
    path('add_catg/', views.add_catg, name="add_catg"),
    path('save_categ/', views.save_categ, name="save_categ"),
    path('display_categ/', views.display_categ, name="display_categ"),
    path('edit_categ/<int:dataid>/', views.edit_categ, name="edit_categ"),
    path('update_categ/<int:dataid>/', views.update_categ, name="update_categ"),
    path('delete_categ/<int:dataid>/', views.delete_categ, name="delete_categ"),
    path('add_prod/', views.add_prod, name="add_prod"),
    path('save_prod/', views.save_prod, name="save_prod"),
    path('display_prod/', views.display_prod, name="display_prod"),
    path('edit_prod/<int:dataid>/', views.edit_prod, name="edit_prod"),
    path('update_prod/<int:dataid>/', views.update_prod, name="update_prod"),
    path('delete_prod/<int:dataid>/', views.delete_prod, name="delete_prod"),
    path('show/', views.show, name="show"),
    path('log/', views.log, name="log"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('display_contacts/', views.display_contacts, name="display_contacts"),
    path('llogout/', views.llogout, name="llogout"),





]