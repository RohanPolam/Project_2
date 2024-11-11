FROM python:3.8-slim

WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV WANDB_API_KEY=dec98b3a498230689df8aeef1d23016e9e5f5abc

# Copy the application code
COPY . .

# Expose the necessary port
EXPOSE 3000

# Run the main application
CMD ["python", "main.py"]
