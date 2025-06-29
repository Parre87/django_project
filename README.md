
# 🧳 TravelBooking - A Django Travel Reservation App
Welcome to TravelBooking, a simple yet powerful travel destination booking platform built using Django. This app allows users to browse destinations, book trips, and manage their bookings through a user-friendly interface.

Live Demo: (https://django-travel-96afa0cf92c6.herokuapp.com/)

## 🚀 Features

🔍 Search, Sort, and Paginate travel destinations

🧾 User authentication with login/logout and dashboard

🏖️ Destination booking with custom form and date picker

📦 Media upload for destination images

📈 Responsive UI with CSS styling and optional Leaflet map

🔐 Secure settings via .env for deployment


## Deployment
To deploy on Heroku or a similar platform:

Set up Procfile
Ensure whitenoise, gunicorn, and .env settings are correctly configured
Add staticfiles and media handling in production.
PostgreSQL databases by Code Institute are only available to CI Students.

Deployment steps are as follows, after account setup:

Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
Your app name must be unique and then choose a region closest to you (EU or USA), then finally click Create App.
From the new app Settings, click Reveal Config Vars, and set your environment variables to match your private env.py file.

The Procfile can be created with the following command:

echo web: gunicorn app_name.wsgi > Procfile

Postgres Database from Code Institute, I followed these steps:

Submitted email address to the CI PostgreSQL Database link above.
An email was sent to me with my new Postgres Database.
Paste URL into your env.py file and Heroku Config Vars as DATABASE_URL.

Install WhiteNoise package:
pip install whitenoise
Update the requirements.txt file with the newly installed package:
pip freeze --local > requirements.txt
Edit your settings.py file and add WhiteNoise to the MIDDLEWARE list, above all other middleware.


