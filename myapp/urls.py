from django.urls import path
from .views import (
    CustomLoginView,
    workList,
    workDetail,
    workCreate,
    workUpdate,
    workDelete,
    RegisterPage,
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", workList.as_view(), name="tasks"),
    path("task/<int:pk>/", workDetail.as_view(), name="task"),
    path("work-create/", workCreate.as_view(), name="work-create"),
    path("work-update/<int:pk>/", workUpdate.as_view(), name="work-update"),
    path("work-delete/<int:pk>/", workDelete.as_view(), name="work-delete"),
]
