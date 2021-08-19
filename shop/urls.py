from django.urls import path


from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('cart/>', views.cart, name='cart'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    
]