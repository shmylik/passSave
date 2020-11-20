def get_goods() -> list:
    return [
        {
            'name': 'boots', 
            'price': 100,
            'amount':25
         },
         {
            'name': 'socks', 
            'price': 10,
            'amount':15
         },
          {
            'name': 't-shirt', 
            'price': 50,
            'amount':5
         },
        ]
    
def calculate_price(request_item: str, amount: int, goods: list) -> int:
    price = 0
    
    for item in goods:
        if request_item == item['name']:
            if amount:
                if amount > 0 and amount <= item['amount']:
                    price = item['price'] * amount
            else:
                price = item['price']
    
    return price



