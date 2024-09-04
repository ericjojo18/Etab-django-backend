from .role_user_urls import urlpatterns as role_patterns
from .user_urls import urlpatterns as user_patterns

urlpatters = role_patterns + user_patterns