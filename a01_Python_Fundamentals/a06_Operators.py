"""Determines if shopping list item is eligible for free shipping"""

def main():
    """Assignment operators"""
    # Set item_name, item_price, quantity, discount_rate, and eligible_items
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1 
    eligible_items = "Orange banana carrot"
    item_price = 2 #USD

    """Arithmetic operators""" 
    # Calculate subtotal as item_price * quantity
    subtotal = item_price * quantity

    # print item_name, subtotal
    print(f"item_name: {item_name}, subtotal: {subtotal}")

    # initialize discount to 0
    discount = 0

    """Membership operators"""
    # check if item_name is in eligible_items string
    # (used to check if an item is eligible for a discount)
    if item_name in eligible_items:
        discount = subtotal * discount_rate
        print(f"{item_name} is in eligible items. {item_name} is eligible for a discount ")

    # print discount
    print(f"discount: {discount}.")

    """Comparison operators"""
    # check if discount is applied (discount > 0)
    was_discount_applied = discount > 0
    print(f"Was the discount applied: {was_discount_applied}")

    """Logical operators"""
    # check if free shipping should be applied (quantity > 5 AND item_name = 'banana')
    does_free_shipping_apply = quantity > 5 and item_name == 'banana'
    print(f"Is this item eligible for free shipping? {does_free_shipping_apply}")

if __name__ == '__main__':
    main()