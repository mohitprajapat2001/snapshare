# Use the official Python runtime image
FROM python:3.11-slim

# Create app directory
RUN mkdir /snapshare

# Set workdir inside the container
WORKDIR /snapshare

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements
COPY requirements.txt /snapshare/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect Static Files
RUN python manage.py collectstatic --noinput && python manage.py migrate --noinput

# Copy the Django Project
COPY . /snapshare/

# Exposr Port 8000
EXPOSE 8000

# Run Django Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]