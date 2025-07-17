# BlogApp

A full-featured Django blog application with user authentication, profiles, blog posts, comments, likes, and image uploads.

---

## 🚀 Features

- User signup, login, logout with secure authentication  
- User profile management with profile pictures  
- Create, edit blog posts with images  
- Auto-generated unique slugs with Unicode support  
- Comment and Like system with live counts  
- Responsive UI using Bootstrap 5 
- Media upload handling (profile pics, blog images)  

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.8+  
- MySQL Server 
- Git  

### Steps

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/blogapp.git
cd blogapp

python -m venv env
# Linux/Mac
source env/bin/activate

# Windows
env\Scripts\activate

pip install -r requirements.txt

Create a .env file in the root directory
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py collectstatic

python manage.py runserver

```php
 Project Structure
blogapp/             # Django project root
├── App_Blog/        # Blog application
│   ├── models.py    # Blog, Comment, Like models
│   ├── views.py     # Blog views (List, Detail, Create, Update)
│   ├── urls.py      # Blog URL patterns with slug converter
│   └── templates/   # Blog-related HTML templates
├── App_Users/       # User authentication and profiles
│   ├── models.py    # UserProfile model
│   ├── forms.py     # Signup, profile forms
│   ├── views.py     # Auth views (Signup, Login, Logout, Profile)
│   └── urls.py      # User-related URLs
├── blog/            # Project settings and URL conf
│   ├── settings.py  # Settings (database, static/media, templates)
│   └── urls.py      # Main URL config
├── templates/       # Base templates shared by apps
├── static/          # Static assets (CSS, JS, images)
├── media/           # Uploaded media files (profile pics, blog images)
├── manage.py        # Django management script
└── requirements.txt # Python dependencies

