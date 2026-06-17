# Regular set cannot be a dict key (unhashable)
# frozen set CAN be a dict key
# Store route info for city pairs (order doesn't matter)
routes = {
 frozenset({'Delhi', 'Mumbai'}): 1400,
 frozenset({'Delhi', 'Chennai'}): 2200,
}
# Look up distance regardless of order
key = frozenset({'Mumbai', 'Delhi'})
print(routes[key]) # 1400