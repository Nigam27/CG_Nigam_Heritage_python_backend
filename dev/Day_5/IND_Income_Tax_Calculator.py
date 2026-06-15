# Indian Income Tax Calculator (New Regime FY 2024-25)

def calculate_tax(income):
    if income <= 0:
        return "Invalid income"

    tax = 0

    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 300000 * 0.05 + (income - 600000) * 0.10
    elif income <= 1200000:
        tax = (
            300000 * 0.05
            + 300000 * 0.10
            + (income - 900000) * 0.15
        )
    elif income <= 1500000:
        tax = (
            300000 * 0.05
            + 300000 * 0.10
            + 300000 * 0.15
            + (income - 1200000) * 0.20
        )
    else:
        tax = (
            300000 * 0.05
            + 300000 * 0.10
            + 300000 * 0.15
            + 300000 * 0.20
            + (income - 1500000) * 0.30
        )

    surcharge = 0

    if income > 10000000:
        surcharge = tax * 0.15
    elif income > 5000000:
        surcharge = tax * 0.10

    cess = (tax + surcharge) * 0.04
    total = tax + surcharge + cess

    return {
        "income": income,
        "base_tax": round(tax),
        "cess": round(cess),
        "total_tax": round(total),
        "take_home": round(income - total)
    }


result = calculate_tax(950000)

print(f'Annual Income : Rs. {result["income"]:,}')
print(f'Base Tax : Rs. {result["base_tax"]:,}')
print(f'Health & Ed Cess : Rs. {result["cess"]:,}')
print(f'Total Tax : Rs. {result["total_tax"]:,}')
print(f'Take-Home : Rs. {result["take_home"]:,}')