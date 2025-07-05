#!/usr/bin/env python3
"""
ASCII Art Banner Generator
Converts an image to ASCII art and creates a banner
"""

from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=100, height=25):
    """Convert an image to ASCII art with edge detection"""
    
    # Extended ASCII characters from darkest to lightest
    ascii_chars = "█▉▊▋▌▍▎▏▒░ .:;+=xX$&#@"
    
    try:
        # Open and convert image
        img = Image.open(image_path)
        
        # Convert to grayscale
        img = img.convert('L')
        
        # Resize image (wider aspect ratio for better text display)
        img = img.resize((width, height))
        
        # Convert to numpy array
        img_array = np.array(img)
        
        # Apply histogram equalization for better contrast
        from PIL import ImageOps
        img_eq = ImageOps.equalize(Image.fromarray(img_array))
        img_array = np.array(img_eq)
        
        # Apply edge detection
        from PIL import ImageFilter
        img_pil = Image.fromarray(img_array)
        edges = img_pil.filter(ImageFilter.FIND_EDGES)
        edge_array = np.array(edges)
        
        # Combine original and edges
        combined = np.maximum(img_array, edge_array * 2)
        combined = np.clip(combined, 0, 255)
        
        # Convert to ASCII
        ascii_str = ""
        for row in combined:
            for pixel in row:
                # Map pixel value (0-255) to ASCII character index
                ascii_index = min(int(pixel * len(ascii_chars) / 256), len(ascii_chars) - 1)
                ascii_str += ascii_chars[len(ascii_chars) - 1 - ascii_index]  # Invert for better visibility
            ascii_str += "\n"
        
        return ascii_str
        
    except Exception as e:
        print(f"Error processing image: {e}")
        # Fallback to simple conversion
        try:
            img = Image.open(image_path).convert('L').resize((width, height))
            img_array = np.array(img)
            
            ascii_str = ""
            simple_chars = " .:-=+*#%@"
            for row in img_array:
                for pixel in row:
                    char_index = min(int(pixel * len(simple_chars) / 256), len(simple_chars) - 1)
                    ascii_str += simple_chars[char_index]
                ascii_str += "\n"
            return ascii_str
        except:
            return None

def create_ascii_banner(image_path):
    """Create a complete ASCII banner with text and image"""
    
    # Convert image to ASCII
    ascii_art = image_to_ascii(image_path, width=80, height=20)
    
    if ascii_art is None:
        # Create a stylized text banner if image conversion fails
        ascii_art = """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║  ███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗ ██████╗██╗███████╗  ║
    ║  ████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝██╔════╝██║██╔════╝  ║
    ║  ██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║███████╗██║     ██║█████╗    ║
    ║  ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║╚════██║██║     ██║██╔══╝    ║
    ║  ██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝███████║╚██████╗██║███████╗  ║
    ║  ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚══════╝  ║
    ╚══════════════════════════════════════════════════════════════════════════╝
        """
    
    # Create banner content
    banner = f"""
{ascii_art}

╔══════════════════════════════════════════════════════════════════════════════╗
║                         Daniel Lachner Piza, PhD                            ║
║                Data Scientist | Machine Learning & Signal Processing        ║
║                              University of Calgary                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

    🔬 Neurophysiological Data Analysis
    🧠 EEG/iEEG Signal Processing  
    💻 MLOps & Cloud Computing
    📊 Biomedical Data Science

📍 Calgary, Canada | 🌐 lachner-piza.com | 📧 daniellachner@gmail.com
"""
    
    return banner

def save_ascii_banner(image_path, output_path):
    """Generate and save ASCII banner"""
    
    banner = create_ascii_banner(image_path)
    
    if banner:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(banner)
        print(f"ASCII banner saved to: {output_path}")
        return True
    else:
        print("Failed to create ASCII banner")
        return False

if __name__ == "__main__":
    image_path = "/home/dlp/Development/mossdet/MK2_3201.jpg"
    output_path = "/home/dlp/Development/mossdet/ascii_banner.txt"
    
    # Check if PIL is available
    try:
        from PIL import Image
        print("PIL is available, creating ASCII banner...")
        save_ascii_banner(image_path, output_path)
    except ImportError:
        print("PIL not available. Please install with: pip3 install Pillow")
        
        # Create a simple text-based banner as fallback
        simple_banner = """
████████╗██████╗  ██╗      
██╔═══██║██╔══██╗ ██║      
██║   ██║██████╔╝ ██║      
██║   ██║██╔═══╝  ██║      
╚██████╔╝██║      ███████╗ 
 ╚═════╝ ╚═╝      ╚══════╝ 
                           
╔══════════════════════════════════════════════════════════════════════════════╗
║                         Daniel Lachner Piza, PhD                            ║
║                Data Scientist | Machine Learning & Signal Processing        ║
║                              University of Calgary                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔬 Neurophysiological Data Analysis | 🧠 EEG/iEEG Processing | 💻 MLOps & Cloud
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(simple_banner)
        print(f"Simple ASCII banner saved to: {output_path}")
