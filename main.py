from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create some customers
    customer1 = Customer("John")
    customer2 = Customer("Alice")
    customer3 = Customer("Bob")

    # Create some coffees
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    coffee3 = Coffee("Cappuccino")

    # Create some orders
    order1 = customer1.create_order(coffee1, 5.0)
    order2 = customer2.create_order(coffee1, 6.0)
    order3 = customer1.create_order(coffee2, 4.5)
    order4 = customer3.create_order(coffee3, 7.0)

    # Display orders for a customer
    print(f"Orders for {customer1.name}:")
    for order in customer1.orders():
        print(f"- {order.coffee.name} at ${order.price}")

    # Display customers for a coffee
    print(f"\nCustomers who ordered {coffee1.name}:")
    for customer in coffee1.customers():
        print(f"- {customer.name}")

    # Display the number of orders and average price for a coffee
    print(f"\n{coffee1.name} has been ordered {coffee1.num_orders()} times.")
    print(f"The average price of {coffee1.name} is ${coffee1.average_price():.2f}")

    # Find the customer who spent the most on a coffee
    top_customer = Customer.most_aficionado(coffee1)
    if top_customer:
        print(f"\n{top_customer.name} spent the most on {coffee1.name}.")
    else:
        print(f"\nNo orders found for {coffee1.name}.")

if __name__ == "__main__":
    main()
