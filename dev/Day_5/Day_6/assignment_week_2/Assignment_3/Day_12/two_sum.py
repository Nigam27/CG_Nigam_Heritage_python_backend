def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
 
    while left < right:
        current_sum = arr[left] + arr[right]
 
        if current_sum == target:
            return (arr[left], arr[right])   # Found the pair!
        elif current_sum < target:
            left += 1                         # Need larger sum → move left pointer right
        else:
            right -= 1                        # Need smaller sum → move right pointer left
 
    return None   # No pair found
 
# ── REAL LIFE: Online shopping cart ─────────────────────────────────────
# You have a gift card of Rs 1000. Find two products that together cost exactly Rs 1000.
product_prices = [150, 250, 350, 400, 500, 600, 750, 850]
gift_card = 1000
 
pair = two_sum_sorted(product_prices, gift_card)
print(f'Buy products costing: Rs {pair[0]} and Rs {pair[1]}')  # Rs 250 and Rs 750
