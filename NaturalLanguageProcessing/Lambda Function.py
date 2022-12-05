def get_total(comida, cantidad, bebida, postre):
    precios = {
        'alambre vegetariano' : 115,
        'alambre de pechuga' : 120,
        'alambre de bistec' : 120,
        'alambre de chuleta' : 120,
        'alambre de costilla' : 130,
        'alambre de arrachera' : 145,
        'costra de pastor' : 30,
        'costra de pechuga' : 35,
        'costra de bistec' : 35,
        'volcan de pastor' : 22,
        'volcan de pechuga' : 22,
        'volcan de bistec' : 28,
        'torta de pastor' : 50,
        'torta de maciza' : 50,
        'torta de suadero' : 50,
        'torta de longaniza' : 50,
        'torta de pechuga' : 50,
        'torta de bistec' : 65,
        'torta de chuleta' : 65,
        'refresco' : 23,
        'agua natural' : 20,
        'agua de jamaica' : 24,
        'agua de horchata' : 24,
        'cerveza en botella' : 33,
        'cerveza de barril' : 33,
        'litro de cerveza' : 80,
        'michelada' : 90,
        'michelato' : 90,
        'arroz con leche' : 30,
        'pastel de chocolate' : 35,
        'fresas con crema' : 35,
        'gelatina' : 20,
        'flan' : 30,
        'nada' : 0,
        'no' : 0
    }
    total = int(precios[comida]) * int(cantidad)
    total += int(precios[bebida])
    total += int(precios[postre])

    return total


""" --- Main handler --- """
def lambda_handler(event, context):
    intent_name = event['interpretations'][0]['intent']['name']
    slots = event['interpretations'][0]['intent']['slots']
    comida = slots['comida']['value']['interpretedValue']
    cantidad = slots['cantidad']['value']['interpretedValue']
    bebida = slots['bebida']['value']['interpretedValue']
    postre = slots['postre']['value']['interpretedValue']
    
    total = get_total(comida, cantidad, bebida, postre)
    message = "El total de su orden sería $" + str(total) + ", ¿podemos proceder con su pago?"
    response = {
       'sessionState' : {
            'dialogAction' : {
                'type' : 'Close'
            },
            'intent' : {
                'name' : intent_name,
                'state' : 'Fulfilled'
            }
       },
        'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
    }
    
    return response