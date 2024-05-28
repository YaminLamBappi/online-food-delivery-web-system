Online Food Delivery Web System

This project is an online food delivery web system built using Django. The system allows customers to subscribe to meal plans and manage their meal preferences. It also includes an admin panel for monitoring orders and customer subscriptions.
Features
1. Meal Off System

    Customers can toggle their meal preferences to turn off lunch, dinner, or both.
    Lunch can be turned off from 12 AM to 9 AM.
    Dinner can be turned off from 12 AM to 3 PM.
    Both lunch and dinner can be turned off from 12 AM to 9 AM.

2. Balance Management

    Customers must pay for their subscription plan in full.
    The balance is reduced according to the meals taken (lunch, dinner, or both).

3. Admin Panel

    Admins can view the number of orders placed daily.
    Orders are categorized into basic and premium.
    Orders are further separated into lunch and dinner.

Technology Stack

    Backend: Django
    Frontend: HTML, CSS, JavaScript
    Database: SQLite (default Django setup)

Setup Instructions
Prerequisites

    Python 3.8+
    Django 3.2+

Installation

    Clone the Repository

    bash

git clone https://github.com/your-username/online-food-delivery.git
cd online-food-delivery

Create a Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

Apply Migrations

bash

python manage.py migrate

Create a Superuser

bash

python manage.py createsuperuser

Run the Development Server

bash

    python manage.py runserver

    Access the Application
        Open your web browser and navigate to http://127.0.0.1:8000/
        Access the admin panel at http://127.0.0.1:8000/admin/

Usage
Customer Interface

    Customers can subscribe to meal plans and manage their meal preferences.
    Customers can turn off their lunch or dinner according to the allowed time windows.
    Customers can place orders and their balance will be adjusted accordingly.

Admin Interface

    Admins can view detailed reports on the number of orders placed.
    Admins can see the breakdown of basic and premium orders for both lunch and dinner.

Sample Data

Use the following sample customer data to test the application:
Name	Category	Plan
Customer 1	Basic	7 Days
Customer 2	Basic	7 Days
Customer 3	Premium	30 Days
Customer 4	Basic	15 Days
Customer 5	Basic	30 Days
Customer 6	Premium	15 Days
Customer 7	Premium	3 Days
Customer 8	Premium	3 Days
Customer 9	Basic	3 Days
Customer 10	Basic	3 Days
Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
