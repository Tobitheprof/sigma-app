# Sigma Project

This Django project was generated using Django 5.0.2. It serves as the backend for the Sigma application.

## Overview

This project is structured to handle various functionalities required for the Sigma application. It includes settings for authentication, database configuration, static files handling, email services, and integration with cloud services.

## Getting Started

To set up this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed. This project is developed using Python 3.x.
3. Install the required dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables. This project uses environment variables for sensitive information such as database credentials, cloud service credentials, and email configuration. Ensure you have these variables set up in your environment.
5. Perform database migrations:
    ```
    python manage.py makemigrations
    ```
   ```
   python manage.py migrate
   ```
6. (Only load if you have avaiable data else, ignore this step) Load initial data if needed:
   ```
   python manage.py loaddata <fixture_file>
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
8. Access the application at `http://localhost:8000/`.

## Configuration

### Environment Variables

This project uses the `environ` package to manage environment variables. Ensure you have the following environment variables set:

- `DATABASE_URI`: URI for the database connection.
- `CLOUD_NAME`, `API_KEY`, `API_SECRET`: Credentials for Cloudinary storage.
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`: Credentials for SMTP email backend.
- `GOOGLE_API_KEY`: API key for Google services.

### Database

The project supports both SQLite and other relational databases supported by Django. The database configuration can be adjusted in `settings.py` based on the environment.

### Static and Media Files

Static files are served from the `static` directory, while media files are stored in the `media` directory. Cloudinary is used for media storage in production.

### Authentication

The project implements authentication using Django's built-in authentication system along with `django-allauth` for social authentication.

### Email Configuration

Email functionality is configured using either console backend (for development) or SMTP backend (for production).

## Additional Notes

- Ensure proper security measures are taken before deploying this project to a production environment.
- Refer to Django's documentation for further customization and deployment options.

For more information on Django, refer to [Django Documentation](https://docs.djangoproject.com/en/5.0/).

---




## NB
    - Create a .env file in the same directory as the settings.py file and specify the required key and values there.
    - If running the project with DEBUG set to False in the settings.py file, you only need to specify values for the GOOGLE_API_KEY.




# Running Liz

Liz is Sigma's AI assistant and it's source code is separate from the main Sigma app since it's a gradio app. However, upon a successful startup of Sigma, Liz should be activcated as well.

Liz's source code is located in the same directory as this README.md file under the title "app.py"


To run Liz;

- Ensure you are in the same directory as the "app.py" file for Liz and you have ran all of the pip installaions in the steps for running Sigma.

- Create a .env file in the same directory as the "app.py" and add the variable as for the API key as shown below

```
GOOGLE_API_KEY=<your_api_key> 
```

- To start Liz, run this command


```
python app.py
```

- Liz should startup after this. To visit Liz, paste the link "localhost:7860"


# MISC INFO

Contact me via my email if you have any questions tobiekundayo07@gmail.com. 

Demo Video On: https://www.youtube.com/watch?v=k2rLF6mp6FA

Live URL: https://www.youtube.com/watch?v=k2rLF6mp6FA