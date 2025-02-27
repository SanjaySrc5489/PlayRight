#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Chromium for Playwright
playwright install chromium

# Install dependencies required for Chromium to run on Render
apt update && apt install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libgbm1 \
    libgtk-3-0 \
    libasound2
