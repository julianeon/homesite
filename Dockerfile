# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=homesite.settings

# Create and set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install Djano
RUN pip install Django

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port that the Django development server will run on
EXPOSE 8080

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
