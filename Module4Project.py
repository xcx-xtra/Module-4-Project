# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # Initialize menu items with their respective prices and categories
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Mocha", "Peppermint Patty Coffee", "Caramel Apple Latte", "Iced Ginger Spice Coffee"],
            "Breakfast": ["Bagel", "Donut", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Prices for each item in the menu
        self.prices = {
            "Monster": 3.00, "Rockstar": 3.00,
            "Latte": 4.50, "Mocha": 4.00,
            "Peppermint Patty Coffee": 5.00, "Caramel Apple Latte": 5.50, "Iced Ginger Spice Coffee": 4.50,
            "Bagel": 2.50, "Donut": 1.50, "Scone": 2.00,
            "Falafel Wrap": 5.50, "Hummus & Pita": 4.00, "Chicken Wrap": 6.00
        }

        # Delivery time in minutes to various locations on campus
        self.delivery_locations = {
            "Library": 10,  # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 15
        }
        
        # List to store ratings given by customers
        self.delivery_ratings = []

    def show_menu(self, category=None):
        # Display the menu, filtered by category if specified
        if category:
            print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        # Calculate the total cost of the order, applying discounts and priority charge if applicable
        total = sum([self.prices[item] for item in items])
        if priority_delivery:
            total += 2  # Add $2 for priority delivery
        if has_student_id and total > 10:
            total *= 0.9  # Apply a 10% discount for students
        return total

    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        # Estimate the delivery time based on location and peak hours, adjusting for priority delivery
        base_time = self.delivery_locations[location]
        if priority_delivery:
            base_time -= 3  # Reduce delivery time by 3 minutes for priority delivery
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5  # Add time for peak hours
        return base_time

    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        # Print the order summary including items, total cost, and delivery time
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems ordered:")
        for item in items:
            print(f" - {item}: ${self.prices[item]:.2f}")

        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)

        print(f"\nSubtotal: ${sum([self.prices[item] for item in items]):.2f}")
        if has_student_id and total < sum([self.prices[item] for item in items]):
            print("Student discount applied!")
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

    def rate_delivery(self, rating):
        # Allow customers to rate the delivery service
        if 1 <= rating <= 5:
            self.delivery_ratings.append(rating)
            print(f"Thank you for your feedback! You rated our delivery {rating} stars.")
        else:
            print("Invalid rating. Please provide a rating between 1 and 5 stars.")

    def search_items_under_price(self, price_limit):
        # Search for menu items that are under a specified price
        affordable_items = []
        print(f"Items priced under ${price_limit:.2f}:")
        for category in self.menu:
            for item in self.menu[category]:
                if self.prices[item] <= price_limit:
                    affordable_items.append(item)
                    print(f"{item}: ${self.prices[item]:.2f}")
        return affordable_items

# Example usage
def main():
    delivery = DunnDelivery()
    delivery.show_menu("Coffee Drinks")
    order = ["Latte", "Peppermint Patty Coffee"]
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True, priority_delivery=True)
    delivery.rate_delivery(4)
    delivery.search_items_under_price(5)

if __name__ == "__main__":
    main()
