cst_name = input("Enter customer name: ")

prd1_name = input("Enter Product 1 name: ")
prd1_price = float(input("Enter Product 1 price: "))

prd2_name = input("Enter Product 2 name: ")
prd2_price = float(input("Enter Product 2 price: "))

prd3_name = input("Enter Product 3 name: ")
prd3_price = float(input("Enter Product 3 price: "))

ttl_amount = prd1_price + prd2_price + prd3_price

if ttl_amount > 3000:
    discount = ttl_amount * 10 / 100
else:
    discount = 0

final_amount = ttl_amount - discount

print(f"Customer Name : {cst_name}")

print("\nProduct Details:")
print(f"1. {prd1_name} - {prd1_price:.2f}")
print(f"2. {prd2_name} - {prd2_price:.2f}")
print(f"3. {prd3_name} - {prd3_price:.2f}")

print(f"Total Amount  : {ttl_amount:.2f}")
print(f"Discount      : {discount:.2f}")
print(f"Final Amount  : {final_amount:.2f}")
