def calculate_discount(total_price, cashback=0):
    if total_price > 500000:
        discount = 0.1
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05
    else:
        discount = 0

    discount_amount = total_price * discount
    discounted_price = total_price - discount_amount - cashback

    return discounted_price, discount_amount