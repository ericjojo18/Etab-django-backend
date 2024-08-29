from ..models import SiteLogo

def logo_context(request):
    logo = SiteLogo.objects.first()
    
    return  {'logo': logo}
    