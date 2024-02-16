def bill_amount_after_discount(bill_amount, discount_percentage):
    discount_amount = bill_amount * (discount_percentage / 100)
    final_bill_amount = bill_amount - discount_amount

    return final_bill_amount


bill_amount = int(input("enter bill amount:"))
discount_percentage = int(input("enter discount percentag:"))
final_bill_amount = bill_amount_after_discount(bill_amount, discount_percentage)
print(final_bill_amount)
