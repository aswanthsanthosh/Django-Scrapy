# Django-Scrapy Project

This project is an integration of Django with Scrapy to scrape data and manage it through Django's web interface. The scraped data can be stored and manipulated via Django's models and viewed in the Django admin interface.

Features
- Scrapy for web scraping.
- Django for data management and display.
- Celery for handling web scrapping as asynchronous task

__Setup__
__1. Clone the repository__
   ```
   git clone https://github.com/aswanthsanthosh/Django-Scrapy.git
   cd django_scrappy/
   ```
__2. Create a Virtual Environment__
   It's recommended to create a virtual environment to keep your dependencies isolated.
   ```
   python -m venv env
   source env/bin/activate
   ```
__3. Install Dependencies__
   Install the project dependencies listed in the requirements.txt file.
   ```
   pip install -r requirements.txt
   ```
__4. Apply Migrations__
   The default database will be sqlite. Unless you want to configure db to some other database, you can directly run the migrate command
   ```
   python manage.py migrate
   ```
__5. Run Development Server__
   use this command to run this django project :
   ```
   python manage.py runserver
   ```
__6. Celery__
   run this command in another terminal :
   ```
   celery -A django_scrappy worker -l INFO
   ```
__Usage :__
- after running the developement server & Celery go to http://127.0.0.1:8000/
  
   
