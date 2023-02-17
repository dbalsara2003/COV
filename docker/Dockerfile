# Specify the base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY docker/app/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY docker/app/ .

# Set the default environment variables
ENV FLASK_APP=webapp.py
ENV FLASK_ENV=production

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0"]

