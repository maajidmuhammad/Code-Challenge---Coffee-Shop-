# coffee-shop code-challenge

# Coffee Shop System

This project models a simple coffee shop system that allows customers to place orders for different types of coffee. It manages customers, coffee types, and orders, and provides various operations related to these objects.


Represents a type of coffee in the system.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/maajidmuhammad/Code-Challenge---Coffee-Shop-
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```python
from system import Customer, Coffee, Order

customer = Customer("John Doe")
coffee = Coffee("Latte")
order = Order(customer, coffee, 4.99)

prepared by:maajidmuhammad