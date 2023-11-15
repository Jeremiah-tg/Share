from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, CreateSubscriptionPageView

urlpatterns = [
   # path("", views.home, name="home"),
path("", HomeView.as_view(), name="home"),
path("opportunity_details/<int:pk>", ArticleDetailView.as_view(), name="shared-opportunity"),
# path("links/<int:pk>", LinkViews.as_view(), name="links"),
#pk is a predefined key that is asigned to each post that is entered.
path("add_post/", AddPostView.as_view(), name="add_post"),
path("opportunity_details/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
path("opportunity_details/<int:pk>/remove", DeletePostView.as_view(), name="delete_post"),
path("like/<int:pk>", LikeView, name="like_post"),
path("subscription/", CreateSubscriptionPageView.as_view(), name="create_subscription_page"),

    
]
