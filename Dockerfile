FROM python:3.12-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY dep.txt .
RUN pip install --no-cache-dir -r dep.txt

EXPOSE 8000

# Copy your application code
COPY . .

# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
