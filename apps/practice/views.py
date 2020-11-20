from django.http import HttpResponse, JsonResponse
from .services import goods as goodsService

goodMail = 'спасибо, всё прост супер'
badMail = 'ошибка, переделывай'

fruits = ('apple', 'watermelon', 'banana', 'orange')

def test(request):
    request_fruit = request.GET.get('fruit')
    
    for fruit in fruits:
        if request_fruit == fruit:
            answer = goodMail
            break

        else:
            answer = badMail
        
    return HttpResponse(answer)

# /ex1/?order=boots&amount=3
def calculate_goods_price(request):
    """Считает сумму по имени товара и его количеству """
    request_order = request.GET.get('order')
    request_amount = request.GET.get('amount')
    
    goods = goodsService.get_goods()
    price = goodsService.calculate_price(request_order, int(request_amount), goods)
    

    return JsonResponse({'result': price})

    