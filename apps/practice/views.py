from django.http import HttpResponse

goodMail = ('спасибо, всё прост супер')
badMail = ('ошибка, переделывай')

def test(request):
    request_check = request.GET.get('check')
    
    checks = ['goodCheck', 'badCheck']
    
    
    for check in checks:
        print(checks[0])
        # if 'goodCheck':
        #     print(goodMail)
        #     continue
        
        # elif 'badCheck':
        #     print(badMail)
        #     continue

        
    return HttpResponse(check)
    