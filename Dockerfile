# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

RUN ls -l

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variable to ensure Python prints everything to the console
#ENV PYTHONUNBUFFERED=1
#ENV FLASK_ENV=development


# Define environment variable
ENV FLASK_APP=app.py

# Run flask command to start the server
#CMD ["flask", "run", "--host=0.0.0.0","--reload", "--debug"]
#https://stackoverflow.com/questions/29663459/why-doesnt-python-app-print-anything-when-run-in-a-detached-docker-container
CMD ["python","-u","app.py"]

