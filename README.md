Django CRUD Web Application with MySQL
This project demonstrates a web application built using Python's Django framework, integrating MySQL for data storage. It showcases fundamental CRUD (Create, Read, Update, Delete) operations, serving as a practical example for beginners and enthusiasts aiming to understand Django's capabilities in web development.​

Features
Order Management: Create, view, update, and delete orders with fields such as Order ID, First Name, Last Name, Price, Email, and Address.​
GitHub

Form Handling: Utilizes Django's ModelForm for efficient form creation and validation.​
GitHub
+1
GitHub
+1

Function-Based Views: Implements views to handle HTTP requests and responses for CRUD operations.​

MySQL Integration: Connects to a MySQL database for robust data management.​
GitHub
+5
GitHub
+5
GitHub
+5

Bootstrap Styling: Incorporates Bootstrap for responsive and modern UI design.​

Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.x​
GitHub
+1
Gist
+1

Django 3.x or higher​

MySQL Server​

mysqlclient Python package​

Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Ranshiv/WEBSITE-USING-PYTHON-MYSQL-DJANGO-and-Web-Scripts.git
cd WEBSITE-USING-PYTHON-MYSQL-DJANGO-and-Web-Scripts
Create a Virtual Environment (Optional but recommended):

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure MySQL Database:

Create a MySQL database (e.g., order_db).​
GitHub
+5
GitHub
+5
GitHub
+5

Update the DATABASES setting in settings.py with your MySQL credentials:​

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'order_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply Migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy
Edit
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Project Structure
plaintext
Copy
Edit
├── crudproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── crudapp/
│   ├── migrations/
│   ├── templates/
│   │   └── crudapp/
│   ├── static/
│   │   └── crudapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt
Usage
Create Order: Navigate to /ofv/ to access the order creation form.​
GitHub

View Orders: Visit /sv/ to see a list of all orders.​
GitHub

Update Order: Click on the update link next to an order in the list to modify its details.​

Delete Order: Click on the delete link next to an order to remove it from the database.​

Screenshots
Include screenshots of the application interfaces here to provide visual context.

Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.​

License
This project is open-source and available under the MIT License.​

Acknowledgments
This project is inspired by educational resources and tutorials aimed at teaching Django's CRUD functionalities.
