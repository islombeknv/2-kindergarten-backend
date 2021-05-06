from django.urls import path

from main.views import NewsListView, NewsDetailView, \
    StaffListView, GalleryListView, ContactCreateView, \
    IndexTemplateView

urlpatterns = [
    path('yangiliklar/', NewsListView.as_view(), name='yangiliklar'),
    path('yangiliklar/<int:pk>/', NewsDetailView.as_view(), name='yangiliklar-r'),
    path('xodimlar/', StaffListView.as_view(), name='xodimlar'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', IndexTemplateView.as_view(), name='index'),
]
