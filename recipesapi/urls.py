#this whole file is for mapping views, so we can call them later on
from django.urls import include, path
from rest_framework import routers #router classs is wiring up resources into views and urls automatically
from . import views
# Creation of a router and registering my viewsets with it.
router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'allItems', views.AllItemsViewSet)

#function dataInput is not mapped anymore because it was inserting data all the time website was up and we didn't want that
urlpatterns = [
    path('', include(router.urls)), #wiring up our API using automatic URL routing.

]