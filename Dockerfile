FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
# Copy templates directory (ensure templates/ exists in project root)
COPY templates/ templates/

# Expose port
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]