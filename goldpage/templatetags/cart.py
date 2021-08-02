from django import template

register=template.Library()


#decorator
@register.filter(name='cart_has_it')
def cart_has_it(product,cart):
    print(product,cart)
    proidsincart=cart.keys()
    for id in proidsincart:
        if int(id)==product.proid:
            return cart[id]

    return False
