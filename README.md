# My Portfolio Website Using Django

This is a portfolio website built using Django. It showcases personal projects, provides a way to contact me, and features an elegant design with dynamic content powered by Django's backend framework.

---

## **Features**

1. **Homepage**
   - Welcomes visitors with a brief introduction.
   - Links to the Projects and Contact pages.

2. **Projects Page**
   - Displays a list of personal projects.
   - Each project includes:
     - A title
     - A description
     - An image
     - A link to the live project or GitHub repository.

3. **Contact Page**
   - Provides a form for visitors to reach out.
   - Includes fields for name, email, and message.

4. **Admin Panel**
   - Manage projects, contact submissions, and website content dynamically.

---

## **Technologies Used**

- **Frontend**: HTML, CSS (with a focus on responsive design).
- **Backend**: Django (Python-based web framework).
- **Database**: SQLite (default Django database, easy to set up).
- **Version Control**: Git and GitHub.
- **Static and Media Files**:
  - Static files (CSS, JS) served via Django's static file management.
  - Media files (project images) uploaded and stored dynamically.

---

## **Setup Instructions**

### Prerequisites
- Python 3.x installed.
- Django installed (`pip install django`).
- Git installed.

### Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/my_portfolio_website_using_django.git
   ```

2. Navigate to the Project Directory:
   ```bash
   cd my_portfolio_website_using_django
   ```

3. Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply Migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the Development Server:
   ```bash
   python manage.py runserver
   ```

7. Access the Website:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## **Project Structure**

```
my_portfolio_website_using_django/
├── myproject/            # Project settings and configurations
├── portfolio_app/         # Main application folder
│   ├── models.py         # Database models for projects
│   ├── views.py          # Handles web requests and responses
│   ├── urls.py           # URL routing for the app
│   ├── templates/        # HTML templates
│   │   └── portfolio_app/
│   │       ├── home.html
│   │       ├── projects.html
│   │       └── contact.html
│   └── static/           # Static files (CSS, JS)
├── media/                # Uploaded media files (project images)
├── db.sqlite3            # Database file
├── manage.py             # Django project management script
└── requirements.txt      # List of dependencies
```

---

## **Future Enhancements**

- Add a blog section.
- Integrate a light/dark mode toggle.
- Implement user authentication for a more personalized experience.

---

## **Contributing**

Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**

If you have any questions or suggestions, feel free to contact me:

- Email: tayybahafeez.2022@gmail.com
- LinkedIn: https://www.linkedin.com/in/tayyba-hafeez-ullah-17980623b/ 

