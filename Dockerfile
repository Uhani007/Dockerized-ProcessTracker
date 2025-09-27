FROM python:3


# Create app directory
WORKDIR /app


# Copy files
COPY server.py /app/server.py
COPY main.py /app/main.py
COPY start.sh /app/start.sh
COPY requirements.txt /app/requirements.txt


# Install Python deps
RUN pip install --no-cache-dir -r /app/requirements.txt


# Make start script executable
RUN chmod +x /app/start.sh


# Default command
CMD ["/app/start.sh"]
