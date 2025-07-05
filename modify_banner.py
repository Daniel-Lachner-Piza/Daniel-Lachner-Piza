#!/usr/bin/env python3
"""
Script to modify the existing banner.png and remove "University of Calgary" text
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_modified_banner():
    """Create a new banner without University of Calgary text"""
    # Banner dimensions
    width, height = 1200, 300
    
    # Create image with gradient background (sky)
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient sky background
    for y in range(height):
        # Sky gradient from light blue to darker blue
        r = int(135 + (70 - 135) * (y / height))  # 135 to 70
        g = int(206 + (130 - 206) * (y / height))  # 206 to 130
        b = int(235 + (180 - 235) * (y / height))  # 235 to 180
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
    
    # Create mountain silhouettes
    points1, points2 = create_mountain_silhouette(width, height)
    
    # Draw background mountains (lighter)
    draw.polygon(points1, fill=(80, 100, 120))
    
    # Draw foreground mountains (darker)
    draw.polygon(points2, fill=(60, 80, 100))
    
    # Try to load a font, fallback to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        try:
            title_font = ImageFont.truetype("arial.ttf", 48)
            subtitle_font = ImageFont.truetype("arial.ttf", 24)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
    
    # Text content (REMOVED University of Calgary)
    name = "Daniel Lachner Piza, PhD"
    subtitle = "Data Scientist | Machine Learning & Signal Processing"
    
    # Calculate text positions for center alignment
    try:
        name_bbox = draw.textbbox((0, 0), name, font=title_font)
        name_width = name_bbox[2] - name_bbox[0]
        
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    except:
        # Fallback for older PIL versions
        name_width = len(name) * 25
        subtitle_width = len(subtitle) * 12
    
    # Position text in upper portion of banner
    name_x = (width - name_width) // 2
    name_y = 80  # Moved down since we removed the third line
    
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = name_y + 60
    
    # Add text shadow for better readability
    shadow_offset = 2
    
    # Draw text shadows
    draw.text((name_x + shadow_offset, name_y + shadow_offset), name, 
              fill=(0, 0, 0), font=title_font)
    draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, 
              fill=(0, 0, 0), font=subtitle_font)
    
    # Draw main text in white
    draw.text((name_x, name_y), name, fill=(255, 255, 255), font=title_font)
    draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 255, 255), font=subtitle_font)
    
    return img

def create_mountain_silhouette(width, height):
    """Create a mountain silhouette using PIL"""
    # First mountain range (background)
    points1 = [
        (0, height),
        (width * 0.15, height * 0.6),
        (width * 0.3, height * 0.7),
        (width * 0.45, height * 0.5),
        (width * 0.6, height * 0.65),
        (width * 0.75, height * 0.55),
        (width * 0.9, height * 0.7),
        (width, height * 0.6),
        (width, height),
        (0, height)
    ]
    
    # Second mountain range (foreground)
    points2 = [
        (0, height),
        (width * 0.1, height * 0.8),
        (width * 0.25, height * 0.65),
        (width * 0.4, height * 0.75),
        (width * 0.55, height * 0.6),
        (width * 0.7, height * 0.7),
        (width * 0.85, height * 0.65),
        (width, height * 0.75),
        (width, height),
        (0, height)
    ]
    
    return points1, points2

if __name__ == "__main__":
    # Create and save the modified banner
    banner = create_modified_banner()
    banner.save('/home/dlp/Development/mossdet/banner.png', 'PNG', quality=95)
    print("Modified banner created successfully: banner.png (University of Calgary text removed)")
