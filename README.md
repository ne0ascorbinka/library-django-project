# Library Management System (Django)
<!-- <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"> -->

## 📝| Description
A comprehensive web-based library management system built with Django. This system is designed to streamline the management of library resources, including books, authors, and user accounts, with a focus on efficiency and user-friendliness.

## ✅| Key Features
- **User Authentication**: Custom user model with roles (visitor, librarian) for differentiated access and functionalities.
- **Author Management**: Create, view, and delete authors. Authors are linked to books.
- **Book Management**: Add and manage books, including details like name, description, and associated authors.
- **Order Processing**: Handle book orders, including creation and tracking of orders.

## ⚙️| Technology Stack
- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Static files and templates in Django)
- **Containerization**: Docker (optional for deployment)

## 📦| Installation and Setup
1. Clone the repository.
```shell
git clone https://github.com/ne0ascorbinka/library-django-project.git
```
2. Install dependencies:
```shell
pip install -r requirements.txt
```
3. Set up a PostgreSQL database.
4. Configure project:
 - Go to `.env.template`;
 - Get your django key and paste in .env file. You can get your key by running:
```shell
python .\library\utils\get_key.py
# or on linux:
python ./library/utils/get_key.py 
```
 - configure DB parameters
 - rename template file to `.env`
5. Run migrations:
```shell
cd library;
python manage.py migrate;
```
6. Start the server: 
```shell
python manage.py runserver
```

## ❔| How to Use
- Access the web interface at `http://localhost:8000` (or configured port).
- Log in as a librarian to access full functionalities.
- Manage authors, books, and orders through the web interface.

## 💛| Contributing
Contributions to the project are welcome. Please follow standard GitHub pull request procedures.

