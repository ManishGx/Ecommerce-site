# My E-commerce Project

## Overview
This project is an e-commerce web application built using Django. It provides a platform for users to browse products, add them to their cart, and make purchases. The application features user authentication, product management, and a responsive design.

## Features
- User registration and authentication
- Product listing and detail views
- Shopping cart functionality
- Order management
- Admin panel for managing products and orders

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite**: A lightweight database for development and testing.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For client-side interactivity.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my_ecomm
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.
- Register a new account or log in to an existing account to start shopping.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Django documentation for guidance on building web applications.
- Online resources and tutorials for learning Django and web development best practices.
