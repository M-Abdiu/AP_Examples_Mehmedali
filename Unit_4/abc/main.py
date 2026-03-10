from taxable_items import RegularProduct, ReducedProduct, TaxExemptProduct
from shopping_cart import ShoppingCart

if __name__ == "__main__":
    # Example usage
    cart = ShoppingCart()

    cart.add_item(RegularProduct("Headphones", 100.00))
    cart.add_item(ReducedProduct("Bread", 10.00))
    cart.add_item(TaxExemptProduct("Postage Stamp", 5.00))

    print(f"Net total:   {cart.total_net():.2f} CHF")
    print(f"VAT total:   {cart.total_vat():.2f} CHF")
    print(f"Gross total: {cart.total_gross():.2f} CHF")
