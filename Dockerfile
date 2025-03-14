# Use Python 3.11 official image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install system dependencies required for PyQt6 and the xcb platform plugin
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxkbcommon-x11-0 \
    libdbus-1-3 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libxcb-randr0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-render0 \
    libxcb-shm0 \
    libxcb1 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-util1 \
    libxcb-xkb1 \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable to ensure Qt finds the xcb plugin
ENV QT_QPA_PLATFORM=xcb
ENV QT_DEBUG_PLUGINS=1  
# Enable debug logs for Qt plugins

# Copy the project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
