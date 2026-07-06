def format_price(price):

    if price >= 10000000:
        return f"₹ {price/10000000:.2f} Crore"

    elif price >= 100000:
        return f"₹ {price/100000:.2f} Lakh"

    else:
        return f"₹ {price:,.2f}"
