<h1>Django CRUD Web Application with MySQL</h1>

<p>This repository presents a web application built using Python's Django framework, integrated with a MySQL database. It demonstrates fundamental CRUD (Create, Read, Update, Delete) operations, serving as a practical example for those interested in web development with Django.</p>

<h2>Features</h2>

<ul>
  <li><strong>Order Management</strong>: Create, view, update, and delete orders with fields such as Order ID, First Name, Last Name, Price, Email, and Address.</li>
  <li><strong>Form Handling</strong>: Utilizes Django's <code>ModelForm</code> for efficient form creation and validation.</li>
  <li><strong>Function-Based Views</strong>: Implements views to handle HTTP requests and responses for CRUD operations.</li>
  <li><strong>MySQL Integration</strong>: Connects to a MySQL database for robust data management.</li>
  <li><strong>Bootstrap Styling</strong>: Incorporates Bootstrap for responsive and modern UI design.</li>
</ul>

<h2>Prerequisites</h2>

<p>Before setting up the project, ensure you have the following installed:</p>

<ul>
  <li>Python 3.x</li>
  <li>Django 3.x or higher</li>
  <li>MySQL Server</li>
  <li><code>mysqlclient</code> Python package</li>
</ul>

<h2>Installation</h2>

<ol>
  <li><strong>Clone the Repository</strong>:
    <pre><code>git clone https://github.com/Ranshiv/WEBSITE-USING-PYTHON-MYSQL-DJANGO-and-Web-Scripts.git
cd WEBSITE-USING-PYTHON-MYSQL-DJANGO-and-Web-Scripts</code></pre>
  </li>
  <li><strong>Create a Virtual Environment</strong> (Optional but recommended):
    <pre><code>python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate</code></pre>
  </li>
  <li><strong>Install Dependencies</strong>:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Configure MySQL Database</strong>:
    <ul>
      <li>Create a MySQL database (e.g., <code>order_db</code>).</li>
      <li>Update the <code>DATABASES</code> setting in <code>settings.py</code> with your MySQL credentials:
        <pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'order_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}</code></pre>
      </li>
    </ul>
  </li>
  <li><strong>Apply Migrations</strong>:
    <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
  </li>
  <li><strong>Run the Development Server</strong>:
    <pre><code>python manage.py runserver</code></pre>
    <p>Access the application at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</p>
  </li>
</ol>

<h2>Project Structure</h2>

<pre><code>├── crudproject/
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
└── requirements.txt</code></pre>

<h2>Usage</h2>

<ul>
  <li><strong>Create Order</strong>: Navigate to <code>/ofv/</code> to access the order creation form.</li>
  <li><strong>View Orders</strong>: Visit <code>/sv/</code> to see a list of all orders.</li>
  <li><strong>Update Order</strong>: Click on the update link next to an order in the list to modify its details.</li>
  <li><strong>Delete Order</strong>: Click on the delete link next to an order to remove it from the database.</li>
</ul>

<h2>Screenshots</h2>

<p><em>Include screenshots of the application interfaces here to provide visual context.</em></p>

<h2>Contributing</h2>

<p>Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.</p>

<h2>License</h2>

<p>This project is open-source and available under the <a href="LICENSE">MIT License</a>.</p>

<h2>Acknowledgments</h2>

<p>This project is inspired by educational resources and tutorials aimed at teaching Django's CRUD functionalities.</p>

<hr>

<p><em>Note: Replace placeholders like <code>your_mysql_username</code> and <code>your_mysql_password</code> with your actual MySQL credentials. Additionally, ensure that the <code>requirements.txt</code> file includes all necessary dependencies for the project.</em></p>
