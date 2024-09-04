from .app_setting_urls import urlpatterns as app_patterns
from .school_urls import urlpatterns as  school_patterns

urlpatterns = app_patterns + school_patterns
