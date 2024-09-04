# from .students_urls import urlpatterns as student_patterns
# from .absence_urls import  urlpatterns as absence_patterns
# from .student_card_urls import urlpatterns as cards_patterns

# urlpatterns = student_patterns + absence_patterns + cards_patterns

from . import absence_urls
from . import student_card_urls 
from . import students_urls

