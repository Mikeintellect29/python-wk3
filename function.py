def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or higher.
    
    :param price: Original price of the item (float)
    :param discount_percent: Discount percentage to apply (float)
    :return: Final price after applying the discount or the original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if final_price == original_price:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric inputs for the price and discount percentage.")
