#!/usr/bin/env python3
"""
Simple banner generator using PIL
Requires: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_simple_banner():
    """Create a simple PNG banner using PIL"""
    
    # Banner dimensions
    width, height = 800, 200
    
    # Create image with gradient-like background
    img = Image.new('RGB', (width, height), color='#2E3440')
    draw = ImageDraw.Draw(img)
    
    # Create a subtle gradient effect
    for y in range(height):
        alpha = y / height
        r = int(46 + (76 - 46) * alpha)
        g = int(52 + (86 - 52) * alpha)
        b = int(64 + (106 - 64) * alpha)
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
    
    # Add grid pattern
    grid_color = (94, 129, 172, 30)  # Semi-transparent
    for x in range(0, width, 20):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 20):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
    
    try:
        # Try to use a nice font (fallback to default if not available)
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except:
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Text content
        name = "Daniel Lachner Piza, PhD"
        title = "Data Scientist | Machine Learning & Signal Processing"
        affiliation = "University of Calgary | Neurophysiological Data Analysis"
        
        # Text colors
        text_color = (236, 239, 244)  # Light text
        subtitle_color = (136, 192, 208)  # Blue accent
        small_color = (129, 161, 193)  # Lighter blue
        
        # Draw text
        draw.text((40, 50), name, fill=text_color, font=font_large)
        draw.text((40, 85), title, fill=subtitle_color, font=font_medium)
        draw.text((40, 110), affiliation, fill=small_color, font=font_small)
        
        # Add decorative circles
        draw.ellipse([720, 30, 728, 38], fill=(136, 192, 208, 200))
        draw.ellipse([740, 50, 746, 56], fill=(129, 161, 193, 150))
        draw.ellipse([760, 70, 770, 80], fill=(94, 129, 172, 100))
        
        # Add wave line
        wave_y = 140
        wave_color = (136, 192, 208, 150)
        draw.line([(40, wave_y), (600, wave_y)], fill=wave_color, width=2)
        
        # Save the image
        current_dir = os.path.dirname(os.path.abspath(__file__))
        banner_path = os.path.join(current_dir, "banner.png")
        img.save(banner_path, "PNG")
        
        print(f"Banner created successfully: {banner_path}")
        return True
        
    except Exception as e:
        print(f"Error creating banner: {e}")
        return False

if __name__ == "__main__":
    create_simple_banner()
