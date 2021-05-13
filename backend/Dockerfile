FROM python:3.9

# We copy just the requirements.txt first to leverage Docker cache
RUN apt-get update

# Create working directory
RUN mkdir /app
WORKDIR /app

# Install the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the server
EXPOSE 5000
CMD [ "uvicorn", "app:app", "--reload"]