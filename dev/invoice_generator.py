"""
Module: invoice_generator.py
Author: Ananya Krishnan
Created: January 2024

Description:
    This module generates invoices for an e-commerce platform.
    It calculates GST, applies discounts, and formats the output.

Usage:
    python invoice_generator.py
"""

def calculate_invoice(items, discount_percent=0):
    """
    Calculate the final invoice amount.

    Args:
        items (list): List of (name, price, qty) tuples
        discount_percent (float): Discount percentage (default: 0)

    Returns:
        float: Final invoice amount after GST and discount

    Example:
        >>> calculate_invoice([('Laptop', 50000, 1)], 5)
        56050.0
    """
    subtotal = sum(price * qty for name, price, qty in items)

    discount = subtotal * (discount_percent / 100)
    after_discount = subtotal - discount

    gst = after_discount * 0.18

    return after_discount + gst