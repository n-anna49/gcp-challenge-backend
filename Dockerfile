# Base image to use
FROM python:3.10-slim

# Copy files to working directory
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install -r requirements.txt
