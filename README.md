# coffee-shop code-challenge

# Coffee Shop Management System

This project implements a simple Coffee Shop Management System using Python classes to model the interactions between customers, coffee types, and orders. The system includes functionality for creating orders, managing coffee and customer records, and calculating statistics. The system features three main classes: `Coffee`, `Customer`, and `Order`.

**Features:**

- **Coffee**: Represents different types of coffee with attributes and methods to manage orders. It includes:
  - **Attributes**:
    - `name`: The name of the coffee (1-15 characters long).
  - **Methods**:
    - `orders()`: Returns a list of orders containing this coffee.
    - `add_order(order)`: Adds an order to the coffee.
    - `coffees()`: Returns a list of unique coffee types from all orders.
    - `create_order(customer, price)`: Creates a new order for this coffee and links it with the customer.

- **Customer**: Represents a customer who can place orders with attributes and methods to manage their orders. It includes:
  - **Attributes**:
    - `name`: The name of the customer (1-15 characters long).
  - **Methods**:
    - `orders()`: Returns a list of orders made by the customer.
    - `add_order(order)`: Adds an order to the customer's list.
    - `coffees()`: Returns a list of unique coffee types the customer has ordered.
    - `create_order(coffee, price)`: Creates a new order for the specified coffee and links it with this customer.
    - `num_orders()`: Returns the total number of orders placed by the customer.
    - `average_price()`: Returns the average price of all orders placed by the customer.

- **Order**: Represents an order for a specific coffee by a customer with attributes and methods to manage the order. It includes:
  - **Attributes**:
    - `customer`: The customer who placed the order.
    - `coffee`: The coffee that was ordered.
    - `price`: The price of the order (must be a float between 1.0 and 10.0).
  - **Class Attributes**:
    - `all`: A list to store all orders created.
  - **Methods**:
    - `price`: A property to get and set the price of the order (once set, it cannot be changed).
    - `customer`: A property to get and set the customer (must be an instance of `Customer`).
    - `coffee`: A property to get and set the coffee (must be an instance of `Coffee`).

    # Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/maajidmuhammad/Code-Challenge---Coffee-Shop-
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

    ``

    prepared by:maajidmuhammad









