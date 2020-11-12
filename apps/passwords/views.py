from django.http import JsonResponse, HttpResponse

def get_passwords(request):
    fruit = request.GET.get('fruit')
    obj = {}

    if fruit == 'orange':
        obj = {
            'answer':'tnx'
            }
            
    else:
        obj = {
             'answer':'where is orange?'
           }    

    return JsonResponse(obj)