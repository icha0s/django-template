from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(title="{{cookiecutter.project_name}} API", default_version="v1", description="Routes of {{cookiecutter.project_name}} project"),
    public=False,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("swagger(<str:format>.json|.yaml)/", schema_view.without_ui(), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    path("docs/", schema_view.with_ui("redoc"), name="schema-redoc"),
    path("", include((router.urls, "api-root")), name="api-root"),
]

app_name = "api_v1"

urlpatterns += router.urls
