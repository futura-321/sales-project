from django.urls import include, path

from main_app import views, admin_views, seller_views, customer_views

urlpatterns = [
   path("",views.main,name="home"),
   path("dash/",views.dash,name="dash"),
   path("login/",views.Login,name="Login"),
   path("admin_dash/",views.admin_dash,name='admin_dash'),
   path("customer_dash/",views.customer_dash,name='customer_dash'),
   path("seller_dash/",views.seller_dash,name='seller_dash'),
   path("customer_register/",views.customer_register,name="customer_register"),
   path("seller_register/",views.seller_register,name="seller_register"),
   path("customer_details/",admin_views.customer_details,name="customer_details"),
   path("seller_details/",admin_views.seller_details,name="seller_details"),
   path("customer_update/<int:id>/",admin_views.customer_update,name="customer_update"),
   path("customer_delete/<int:id>/",admin_views.customer_delete,name="customer_delete"),
   path("seller_update/<int:id>/",admin_views.seller_update,name="seller_update"),
   path("seller_delete/<int:id>/",admin_views.seller_delete,name="seller_delete"),
   path("add_product/",seller_views.create_product,name="create_product"),
   path("view_products/", seller_views.view_products, name="view_products"),
   path("product_delete/<int:id>/",seller_views.product_delete,name="product_delete"),
   path("update_product/<int:id>/",seller_views.product_update,name="product_update"),
   path("admin_product_view/", admin_views.admin_product_view,name="admin_product_view"),
   path("customer_product_view/", customer_views.customer_product_view, name="customer_product_view"),
   path("add_to_cart/<int:id>/",customer_views.add_to_cart, name="add_to_cart"),
   path("view_cart",customer_views.view_cart,name="view_cart"),
   path("delete_cart/<int:id>/",customer_views.delete_cart,name="delete_cart"),
   path("buy_now/<int:cart_id>/",customer_views.buy,name="buy_now"),
   path("payment/<int:buy_id>/",customer_views.payment,name="payment"),
   path("view_paid_cart/", seller_views.view_paidcart, name="view_paid_cart"),
   path("view_my_orders/", customer_views.my_orders, name="view_my_orders"),
   path("customer_feed_back/", customer_views.customer_feed_back, name="customer_feed_back"),
   path("view_customer_feed_back/", customer_views.customer_view_feedbacks, name="customer_view_feed_backs"),
   path("customer_feedback/",admin_views.admin_view_feedbacks,name="customers_feedback"),
   path("admin_view_orders", admin_views.admin_view_orders, name="admin_view_orders"),
   path("logout/",views.logout_view,name="logout"),
]
