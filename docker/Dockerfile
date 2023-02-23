# Specify the base image
FROM ubuntu:latest

RUN apt-get update && \
        apt-get install -y python3 python3-pip 

# Set the working directory
WORKDIR /app

# Copy the application code
COPY docker/app/ .

# Copy the requirements file
COPY docker/app/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Set the default environment variables
ENV FLASK_APP=webapp.py
ENV FLASK_ENV=production

# Expose the application port
EXPOSE 8080

# Start the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "debug=True"]

