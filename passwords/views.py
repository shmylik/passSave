

from django.http import JsonResponse

def get_passwords(request):
    return JsonResponse({"success" : True})