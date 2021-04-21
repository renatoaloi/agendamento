from django.http import JsonResponse

# Create your views here.
def health_check_view(request):
    return JsonResponse(data={})