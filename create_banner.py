#!/usr/bin/env python3
"""
Banner generator for GitHub profile with mountain background
"""

from PIL import Image, ImageDraw, ImageFont

def create_mountain_silhouette(width, height):
    """Create a mountain silhouette using PIL"""
    # Create mountain points
    mountains = []
    
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

def create_banner():
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
        # Try to use a clean, professional font
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        try:
            title_font = ImageFont.truetype("arial.ttf", 48)
            subtitle_font = ImageFont.truetype("arial.ttf", 24)
            small_font = ImageFont.truetype("arial.ttf", 18)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
    
    # Text content
    name = "Daniel Lachner Piza, PhD"
    subtitle = "Data Scientist | Machine Learning & Signal Processing"
    location = "University of Calgary"
    
    # Calculate text positions for center alignment
    # Get text dimensions
    try:
        name_bbox = draw.textbbox((0, 0), name, font=title_font)
        name_width = name_bbox[2] - name_bbox[0]
        
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        
        location_bbox = draw.textbbox((0, 0), location, font=small_font)
        location_width = location_bbox[2] - location_bbox[0]
    except:
        # Fallback for older PIL versions
        name_width = len(name) * 25
        subtitle_width = len(subtitle) * 12
        location_width = len(location) * 10
    
    # Position text in upper portion of banner
    name_x = (width - name_width) // 2
    name_y = 50
    
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = name_y + 60
    
    location_x = (width - location_width) // 2
    location_y = subtitle_y + 40
    
    # Add text shadow for better readability
    shadow_offset = 2
    shadow_color = (0, 0, 0, 128)
    
    # Draw text shadows
    draw.text((name_x + shadow_offset, name_y + shadow_offset), name, 
              fill=(0, 0, 0), font=title_font)
    draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, 
              fill=(0, 0, 0), font=subtitle_font)
    draw.text((location_x + shadow_offset, location_y + shadow_offset), location, 
              fill=(0, 0, 0), font=small_font)
    
    # Draw main text in white
    draw.text((name_x, name_y), name, fill=(255, 255, 255), font=title_font)
    draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 255, 255), font=subtitle_font)
    draw.text((location_x, location_y), location, fill=(220, 220, 220), font=small_font)
    
    return img
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
if __name__ == "__main__":
    # Create and save the banner
    banner = create_banner()
    banner.save('/home/dlp/Development/mossdet/banner.png', 'PNG', quality=95)
    print("Banner created successfully: banner.png")
