from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(site, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == site.id:
            return True
    return False



@register.filter(name = 'cart_quantity')
def cart_quantity(site, cart):
    dic =[]
    for key in cart:
        for items in cart[key]:
            dic.append(items)
    keys = cart.keys()
    for id in keys:
        if int(id) == site.id:
            return dic[0]
    return 0



@register.filter(name = 'price_total')
def price_total(site, cart):
    # print(cart)
    return site.Price * cart_quantity(site, cart)


@register.filter(name = 'total_cart_price')
def total_cart_price(sites, cart):
    sum = 0
    for data in sites:
        sum += price_total(data, cart)

    return sum

@register.filter(name = 'currency')
def currency(number):
    return "$"+str(number)






