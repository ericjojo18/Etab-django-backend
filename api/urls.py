from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from api.viewset.student_api_views import StudentViewSet
from api.viewset.user_api_views import UserViewSet
from api.viewset.teacher_api_views import TeacherViewSet
from api.viewset.role_viewset import RoleViewSet
from api.viewset.app_setting_viewset import AppSettingViewSet
from api.viewset.school_viewset import SchoolViewSet
from api.viewset.student_absence_viewset import StudentAbsenceViewSet
from api.viewset.student_card_viewset import StudentCardViewSet
from api.viewset.address_viewset import AddressViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
    TokenVerifyView,
)
from api.viewset.customer_token_view import CustomerTokenObtainPairView
# from api.viewset.student_api_views import student_api, student_api_view_detail, 


# from .viewset.teacher_api_views import teacher_api, teacher_api_view_detail
# from .viewset.user_api_views import user_api, user_api_view_detail


router = routers.DefaultRouter()
router.register(r'appsetting', AppSettingViewSet, basename="appsetting")
router.register(r'school', SchoolViewSet, basename="school")
router.register(r'students', StudentViewSet, basename="students")
router.register(r'users', UserViewSet, basename="users")
router.register(r'teachers', TeacherViewSet, basename="teachers")
router.register(r'role', RoleViewSet, basename="role")
router.register(r'studentabsence', StudentAbsenceViewSet, basename="studentabsence")
router.register(r'studentcard', StudentCardViewSet, basename="studentcard")
router.register(r'address', AddressViewSet, basename="address")

app_name = "api"
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('students', student_api),
    # path('teachers', teacher_api),
    # path('users', user_api),
    
    # # path('student', student_api_view_detail),
    # path('student/<int:pk>', student_api_view_detail),
    # path('teacher/<int:pk>', teacher_api_view_detail),
    # path('user/<int:pk>', user_api_view_detail),
    
    path('', include(router.urls)),
    #path('api/token/', CustomerTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
   path('api/token/sliding/', TokenObtainSlidingView.as_view(), name='token_obtain_sliding'),
   path('api/token-sliding/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh_sliding'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]