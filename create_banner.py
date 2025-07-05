#!/usr/bin/env python3
"""
Script to generate a PNG banner from HTML template
Requires: pip install selenium webdriver-manager pillow
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io

def create_banner_png():
    """Create a PNG banner from the HTML template"""
    
    # Setup Chrome options for headless operation
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=800,200")
    
    try:
        # Setup Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Get the current directory and HTML file path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(current_dir, "banner.html")
        
        # Load the HTML file
        driver.get(f"file://{html_file}")
        
        # Wait for page to load
        time.sleep(2)
        
        # Take screenshot
        png_data = driver.get_screenshot_as_png()
        
        # Save as PNG
        banner_path = os.path.join(current_dir, "banner.png")
        with open(banner_path, "wb") as f:
            f.write(png_data)
        
        print(f"Banner saved as: {banner_path}")
        
        # Close driver
        driver.quit()
        
        return True
        
    except Exception as e:
        print(f"Error creating banner: {e}")
        print("\nTo create the banner manually:")
        print("1. Open banner.html in your browser")
        print("2. Take a screenshot of the banner")
        print("3. Save it as banner.png")
        return False

if __name__ == "__main__":
    create_banner_png()
