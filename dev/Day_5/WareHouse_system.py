"""
Smart Warehouse & Inventory Management System"""

from __future__ import annotations
import heapq
import itertools
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

#  CUSTOM EXCEPTIONS  (Task 5 - Exception Handling)

class WarehouseSystemError(Exception):
    """Base class for all custom exceptions in this application."""


class DuplicateProductError(WarehouseSystemError):
    """Raised when attempting to add a product whose ID already exists."""

class ProductNotFoundError(WarehouseSystemError):
    """Raised when a requested Product ID does not exist."""

class InsufficientStockError(WarehouseSystemError):
    """Raised when an order requests more quantity than is available."""


class InvalidInputError(WarehouseSystemError):
    """Raised when supplied data fails validation."""

#  TASK 1 - PRODUCT & INVENTORY MANAGEMENT

@dataclass
class Product:    
    product_id: str
    name: str
    category: str
    quantity: int
    unit_price: float
    location: str

    def __post_init__(self):        
        if not self.product_id or not str(self.product_id).strip():
            raise InvalidInputError("Product ID cannot be empty.")
        if not self.name or not str(self.name).strip():
            raise InvalidInputError("Product name cannot be empty.")
        if self.quantity < 0:
            raise InvalidInputError("Quantity cannot be negative.")
        if self.unit_price < 0:
            raise InvalidInputError("Unit price cannot be negative.")

    def as_row(self) -> Tuple[str, str, str, int, float, str]:
        return (self.product_id, self.name, self.category,
                self.quantity, self.unit_price, self.location)

    def __str__(self) -> str:
        return (f"Product ID   : {self.product_id}\n"
                f"Name         : {self.name}\n"
                f"Category     : {self.category}\n"
                f"Quantity     : {self.quantity}\n"
                f"Unit Price   : Rs. {self.unit_price:,.2f}\n"
                f"Warehouse    : {self.location}")


class InventoryManager:
    """Encapsulates all CRUD operations on the product inventory."""

    def __init__(self):
        self._products: Dict[str, Product] = {}

    
    def add_product(self, product: Product) -> None:
        if product.product_id in self._products:
            raise DuplicateProductError(
                f"Product ID '{product.product_id}' already exists.")
        self._products[product.product_id] = product

    
    def update_quantity(self, product_id: str, new_quantity: int) -> None:
        product = self._get_or_raise(product_id)
        if new_quantity < 0:
            raise InvalidInputError("Quantity cannot be negative.")
        product.quantity = new_quantity

    def adjust_quantity(self, product_id: str, delta: int) -> None:
        """Increase (delta > 0) or decrease (delta < 0) stock safely."""
        product = self._get_or_raise(product_id)
        new_qty = product.quantity + delta
        if new_qty < 0:
            raise InsufficientStockError(
                f"Not enough stock for '{product_id}'. "
                f"Available: {product.quantity}, requested reduction: {-delta}.")
        product.quantity = new_qty

   
    def remove_product(self, product_id: str) -> Product:
        product = self._get_or_raise(product_id)
        del self._products[product_id]
        return product

    
    def search_product(self, product_id: str) -> Product:
        return self._get_or_raise(product_id)

    
    def display_all(self) -> List[Product]:
        return list(self._products.values())

    def exists(self, product_id: str) -> bool:
        return product_id in self._products

    
    def _get_or_raise(self, product_id: str) -> Product:
        product = self._products.get(product_id)
        if product is None:
            raise ProductNotFoundError(f"Product ID '{product_id}' not found.")
        return product

#  TASK 2 - ORDER PROCESSING (priority queue)
class Priority:
    """Lower numeric value = higher priority."""
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    LABELS = {HIGH: "HIGH", MEDIUM: "MEDIUM", LOW: "LOW"}


@dataclass(order=True)
class _QueuedOrder:
    priority: int
    sequence: int
    order_id: str = field(compare=False)
    product_id: str = field(compare=False)
    quantity: int = field(compare=False)


class OrderProcessor:
    """
    Maintains a priority queue of customer orders and processes them
    against the live inventory, updating stock as each order succeeds.
    """

    def __init__(self, inventory: InventoryManager):
        self._inventory = inventory
        self._heap: List[_QueuedOrder] = []
        self._counter = itertools.count()  
        self._order_counter = itertools.count(1)
        self._results: List[str] = []

    def place_order(self, product_id: str, quantity: int,
                     priority: int = Priority.MEDIUM) -> str:
        if quantity <= 0:
            raise InvalidInputError("Order quantity must be greater than zero.")
        if priority not in Priority.LABELS:
            raise InvalidInputError("Priority must be HIGH(1), MEDIUM(2) or LOW(3).")

        order_id = f"ORD{next(self._order_counter):04d}"
        entry = _QueuedOrder(priority, next(self._counter),
                              order_id, product_id, quantity)
        heapq.heappush(self._heap, entry)
        return order_id

    def process_all(self) -> List[str]:
        """Processes queued orders strictly in priority order."""
        self._results.clear()
        while self._heap:
            order = heapq.heappop(self._heap)
            self._process_single(order)
        return self._results

    def _process_single(self, order: _QueuedOrder) -> None:
        label = Priority.LABELS[order.priority]
        try:
            product = self._inventory.search_product(order.product_id)
            if product.quantity < order.quantity:
                msg = (f"[{order.order_id}] [{label}] FAILED - Insufficient stock "
                       f"for '{order.product_id}' ({product.name}). "
                       f"Requested: {order.quantity}, Available: {product.quantity}")
            else:
                self._inventory.adjust_quantity(order.product_id, -order.quantity)
                remaining = self._inventory.search_product(order.product_id).quantity
                msg = (f"[{order.order_id}] [{label}] SUCCESS - {order.quantity} unit(s) "
                       f"of '{order.product_id}' ({product.name}) dispatched. "
                       f"Remaining stock: {remaining}")
        except ProductNotFoundError as e:
            msg = f"[{order.order_id}] [{label}] FAILED - {e}"
        except InsufficientStockError as e:
            msg = f"[{order.order_id}] [{label}] FAILED - {e}"
        self._results.append(msg)
        
#  TASK 3 - WAREHOUSE CONNECTIVITY (shortest route)

class WarehouseGraph:
    
    def __init__(self):
        self._adj: Dict[str, Dict[str, float]] = {}

    def add_warehouse(self, name: str) -> None:
        self._adj.setdefault(name, {})

    def add_route(self, warehouse_a: str, warehouse_b: str, distance: float = 1.0) -> None:
        if distance <= 0:
            raise InvalidInputError("Route distance must be positive.")
        self.add_warehouse(warehouse_a)
        self.add_warehouse(warehouse_b)
        self._adj[warehouse_a][warehouse_b] = distance
        self._adj[warehouse_b][warehouse_a] = distance

    def shortest_route(self, source: str, destination: str
                        ) -> Optional[Tuple[List[str], float]]:
        if source not in self._adj:
            raise ProductNotFoundError(f"Warehouse '{source}' is not registered.")
        if destination not in self._adj:
            raise ProductNotFoundError(f"Warehouse '{destination}' is not registered.")

        if source == destination:
            return [source], 0.0

        distances = {node: float("inf") for node in self._adj}
        previous: Dict[str, Optional[str]] = {node: None for node in self._adj}
        distances[source] = 0.0
        visited = set()
        heap = [(0.0, source)]

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == destination:
                break
            for neighbor, weight in self._adj[node].items():
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = node
                    heapq.heappush(heap, (new_dist, neighbor))

        if distances[destination] == float("inf"):
            return None  # no route exists

        # reconstruct path
        path = []
        node = destination
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        return path, distances[destination]

#  TASK 4 - PRODUCT REPORT

class ReportGenerator:
    """Generates a tabular product report sorted by business rules."""

    @staticmethod
    def generate(inventory: InventoryManager) -> str:
        products = inventory.display_all()        
        products.sort(key=lambda p: (p.quantity, -p.unit_price))

        header = (f"{'Product ID':<12}{'Name':<20}{'Category':<15}"
                  f"{'Qty':>6}{'Unit Price':>14}{'Warehouse':>15}")
        divider = "-" * len(header)
        lines = [divider, header, divider]
        for p in products:
            lines.append(
                f"{p.product_id:<12}{p.name:<20}{p.category:<15}"
                f"{p.quantity:>6}{p.unit_price:>14,.2f}{p.location:>15}"
            )
        lines.append(divider)
        return "\n".join(lines)

#  INPUT VALIDATION HELPERS  (Task 5)

def read_nonempty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  -> This field cannot be empty. Please try again.")


def read_int(prompt: str, minimum: int = 0) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < minimum:
                print(f"  -> Value must be >= {minimum}.")
                continue
            return value
        except ValueError:
            print("  -> Please enter a valid whole number.")


def read_float(prompt: str, minimum: float = 0.0) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < minimum:
                print(f"  -> Value must be >= {minimum}.")
                continue
            return value
        except ValueError:
            print("  -> Please enter a valid number.")


# ======================================================================
#  APPLICATION / CLI LAYER
# ======================================================================
class WarehouseApp:
    """Ties all modules together and drives the interactive console menu."""

    def __init__(self):
        self.inventory = InventoryManager()
        self.orders = OrderProcessor(self.inventory)
        self.routes = WarehouseGraph()
        self._seed_demo_data()

    
    def _seed_demo_data(self) -> None:        
        for a, b, dist in [
            ("Kolkata", "Delhi", 4.0),
            ("Kolkata", "Bhubaneswar", 1.5),
            ("Bhubaneswar", "Chennai", 3.0),
            ("Chennai", "Delhi", 5.0),
            ("Delhi", "Mumbai", 2.5),
            ("Mumbai", "Chennai", 3.5),
        ]:
            self.routes.add_route(a, b, dist)

    
    def run(self) -> None:
        menu = """
   SMART WAREHOUSE & INVENTORY MANAGEMENT SYSTEM
 1. Add Product
 2. Update Product Quantity
 3. Remove Product
 4. Search Product
 5. Display All Products
 6. Place Order
 7. Process All Pending Orders
 8. Find Shortest Route Between Warehouses
 9. Generate Product Report
 0. Exit
"""
        while True:
            print(menu)
            choice = input("Enter your choice: ").strip()
            try:
                if choice == "1":
                    self.add_product_ui()
                elif choice == "2":
                    self.update_quantity_ui()
                elif choice == "3":
                    self.remove_product_ui()
                elif choice == "4":
                    self.search_product_ui()
                elif choice == "5":
                    self.display_all_ui()
                elif choice == "6":
                    self.place_order_ui()
                elif choice == "7":
                    self.process_orders_ui()
                elif choice == "8":
                    self.find_route_ui()
                elif choice == "9":
                    self.generate_report_ui()
                elif choice == "0":
                    print("Exiting. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid menu option.")
            except WarehouseSystemError as e:
                print(f"\n[ERROR] {e}\n")
            except Exception as e:  # safety net - unexpected errors
                print(f"\n[UNEXPECTED ERROR] {e}\n")

    # ---- Task 1 UI handlers -----------------------------------------
    def add_product_ui(self):
        print("\n-- Add New Product --")
        product_id = read_nonempty("Product ID   : ")
        name = read_nonempty("Name         : ")
        category = read_nonempty("Category     : ")
        quantity = read_int("Quantity     : ")
        price = read_float("Price        : ")
        location = read_nonempty("Warehouse    : ")
        product = Product(product_id, name, category, quantity, price, location)
        self.inventory.add_product(product)
        self.routes.add_warehouse(location)
        print(f"Product '{product_id}' added successfully.")

    def update_quantity_ui(self):
        print("\n-- Update Product Quantity --")
        product_id = read_nonempty("Product ID : ")
        new_qty = read_int("New Quantity : ")
        self.inventory.update_quantity(product_id, new_qty)
        print(f"Quantity for '{product_id}' updated to {new_qty}.")

    def remove_product_ui(self):
        print("\n-- Remove Product --")
        product_id = read_nonempty("Product ID : ")
        removed = self.inventory.remove_product(product_id)
        print(f"Product '{removed.product_id}' ({removed.name}) removed.")

    def search_product_ui(self):
        print("\n-- Search Product --")
        product_id = read_nonempty("Product ID : ")
        product = self.inventory.search_product(product_id)
        print("\n" + str(product))

    def display_all_ui(self):
        print("\n-- All Products --")
        products = self.inventory.display_all()
        if not products:
            print("No products in inventory.")
            return
        for p in products:
            print("-" * 40)
            print(p)
        print("-" * 40)

    
    def place_order_ui(self):
        print("\n-- Place Order --")
        product_id = read_nonempty("Product ID : ")
        if not self.inventory.exists(product_id):
            raise ProductNotFoundError(f"Product ID '{product_id}' not found.")
        quantity = read_int("Quantity   : ", minimum=1)
        print("Priority: 1-HIGH, 2-MEDIUM, 3-LOW")
        priority = read_int("Priority   : ", minimum=1)
        if priority > 3:
            priority = Priority.LOW
        order_id = self.orders.place_order(product_id, quantity, priority)
        print(f"Order placed successfully with ID: {order_id} "
              f"(queued, not yet processed).")

    def process_orders_ui(self):
        print("\n-- Processing All Pending Orders (priority order) --")
        results = self.orders.process_all()
        if not results:
            print("No pending orders to process.")
            return
        for line in results:
            print(line)

    
    def find_route_ui(self):
        print("\n-- Find Shortest Route --")
        source = read_nonempty("Source Warehouse      : ")
        destination = read_nonempty("Destination Warehouse : ")
        result = self.routes.shortest_route(source, destination)
        if result is None:
            print(f"No route exists between '{source}' and '{destination}'.")
        else:
            path, distance = result
            print(f"Shortest Route: {' -> '.join(path)}")
            print(f"Total Distance: {distance}")

    
    def generate_report_ui(self):
        print("\n-- Product Report (Qty Ascending, Price Descending) --")
        print(ReportGenerator.generate(self.inventory))

#  ENTRY POINT

if __name__ == "__main__":
    app = WarehouseApp()
    app.run()
