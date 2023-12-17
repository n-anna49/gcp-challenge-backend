# Base image to use
FROM python:3.10-slim

# Port
ENV PORT 5000

# Copy files to working directory
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

# Run app
CMD exec gunicorn --bind :$PORT main:app
