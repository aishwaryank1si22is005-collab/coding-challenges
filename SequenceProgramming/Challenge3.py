total_amount = float(input("Enter total amount: "))
discount_percentage = float(input("Enter discount percentage: "))

discount = (total_amount * discount_percentage) / 100
final_amount = total_amount - discount

print("Discount =", discount)
print("Amount to Pay =", final_amount)
