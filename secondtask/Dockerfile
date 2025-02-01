FROM python:3.13


ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /loginapp

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000 5000

