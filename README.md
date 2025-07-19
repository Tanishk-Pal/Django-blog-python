# 📝 Django Blog App

This is a simple blog application built with **Django**. Users can view blog posts, each with a title, summary, image, and full body content.

## 📌 Features

- Home page with a list of all posts  
- Each post has a:
  - Title
  - Summary
  - Image
  - Full content
- Individual post detail view

## 🛠️ Technologies Used

- Python 3.13  
- Django 5.2  
- SQLite3 (default Django DB)

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Tanishk-Pal/Django-blog-python.git
cd Django-blog-python
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate      # On Linux/macOS
env\Scripts\activate.bat     # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, install Django manually:
```bash
pip install django
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```

### 6. Access the site
Open your browser and go to:  
[http://localhost:8000](http://localhost:8000)

## 📂 Project Structure
```
website/
├── blog/             # App containing models, views, templates
├── website/          # Main project folder
├── db.sqlite3        # Database
├── manage.py         # Django management file
└── media/            # Uploaded images
```

## 🧠 Author

**Tanishk Pal**
