# ====================================================================================
# Stage 1: Builder Stage
#
# This stage installs dependencies and prepares the application. It uses a standard
# Python image that includes build tools. The artifacts from this stage will be
# copied to the final, smaller production stage.
# ====================================================================================
FROM python:3.9-slim-bullseye AS builder

# Set the working directory
WORKDIR /usr/src/app

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents python from writing .pyc files to disc.
# PYTHONUNBUFFERED: Prevents python from buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for some Python packages if needed
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir: Disables the cache, which reduces the image size.
# --user: Installs packages in the user's home directory, not as root.
RUN pip install --no-cache-dir --user -r requirements.txt

# ====================================================================================
# Stage 2: Production Stage
#
# This is the final stage that will be used to run the application. It uses a
# slim Python image to keep the size down. It also creates a non-root user
# to run the application for better security.
# ====================================================================================
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user and group
# This is a critical security best practice to avoid running as root.
RUN addgroup --system app && adduser --system --group app

# Copy installed packages from the builder stage
# This copies the installed dependencies from the builder's user directory.
COPY --from=builder /root/.local /home/app/.local

# Copy the application code into the container
COPY ./app ./app

# Set the PATH environment variable to include the installed packages
ENV PATH=/home/app/.local/bin:$PATH

# Change ownership of the app directory to the new user
RUN chown -R app:app /usr/src/app

# Switch to the non-root user
USER app

# Expose the port the app runs on
EXPOSE 8000

# Add a healthcheck to ensure the application is running
# This command will be run inside the container to check its health.
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Command to run the application
# Using exec form to run as the main process (PID 1)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
