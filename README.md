# Perfume Shop Management System

A desktop-based retail management application developed using **Python (Tkinter)** and **MySQL**. This project automates perfume shop operations such as inventory handling, billing, vendor management, and sales tracking through a user-friendly graphical interface.

## Features

* Secure Login Page
* Add New Products
* Smart Brand Suggestions while typing
* View Inventory in table format
* Search Products by name or brand
* Low Stock Alerts
* Update Product Details
* Delete Products
* Billing Module with product dropdown
* Auto stock reduction after billing
* Dummy Invoice / Receipt generation
* Vendor Management
* Sales Report / Transaction History

## Tech Stack

| Layer         | Technology      |
| ------------- | --------------- |
| Frontend      | Python Tkinter  |
| Backend Logic | Python          |
| Database      | MySQL           |
| Connectivity  | mysql.connector |
| IDE           | VS Code         |

## Database Tables

* `inventory` - Stores perfume products
* `sales` - Stores billing transactions
* `vendors` - Stores supplier details
* `customers` - Stores customer records

## Installation & Setup

1. Clone the repository.
2. Install Python 3.x.
3. Install MySQL and create the project database.
4. Install dependency:

```bash
pip install mysql-connector-python
```

5. Update MySQL credentials inside the Python file.
6. Run the project:

```bash
python perf_shop.py
```

## Screenshots

Add screenshots here:

* Login Page
* Dashboard
* Add Product Window
* Inventory Module
* Billing Window
* Invoice Output
* Sales Report

## Learning Outcomes

This project demonstrates:

* DBMS concepts
* CRUD operations
* SQL queries
* GUI development with Tkinter
* Frontend-backend integration
* Real-world retail workflow automation

## Future Enhancements

* Barcode scanner integration
* GST invoice generation
* Export reports to PDF/Excel
* Customer loyalty system
* Analytics dashboard
* Cloud deployment

## Contributors

* Sanya Singh
* Vedika Shankhapal
* Sayee Shiurkar
* Vedant Sonawane

## License

This project is created for educational and academic purposes.
