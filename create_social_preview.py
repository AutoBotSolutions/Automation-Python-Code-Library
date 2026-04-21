#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create social preview image (1200x630 for Open Graph)
width, height = 1200, 630

# Create image with dark background
img = Image.new('RGB', (width, height), color='#1e1e2e')
draw = ImageDraw.Draw(img)

# Try to use a system font, fallback to default
try:
    title_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
    subtitle_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)
    stats_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    stats_font = ImageFont.load_default()

# Draw title
title = "Automation Python Code Library"
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (width - title_width) // 2
draw.text((title_x, 100), title, fill='#ffffff', font=title_font)

# Draw subtitle
subtitle = "383 Python Scripts in 36 Categories"
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (width - subtitle_width) // 2
draw.text((subtitle_x, 180), subtitle, fill='#a6accd', font=subtitle_font)

# Draw stats
stats = "Web Automation • Database • File Operations • HTTP • Email • FTP • System Commands"
stats_bbox = draw.textbbox((0, 0), stats, font=stats_font)
stats_width = stats_bbox[2] - stats_bbox[0]
stats_x = (width - stats_width) // 2
draw.text((stats_x, 350), stats, fill='#7aa2f7', font=stats_font)

# Draw GitHub URL
url = "github.com/AutoBotSolutions/Automation-Python-Code-Library"
url_bbox = draw.textbbox((0, 0), url, font=stats_font)
url_width = url_bbox[2] - url_bbox[0]
url_x = (width - url_width) // 2
draw.text((url_x, 450), url, fill='#9ece6a', font=stats_font)

# Draw decorative border
border_color = '#7aa2f7'
border_width = 8
draw.rectangle([0, 0, width-1, height-1], outline=border_color, width=border_width)

# Save image
output_path = '/home/robbie/Desktop/CodeLibrary/docs/social-preview.png'
img.save(output_path, 'PNG')
print(f"Social preview image created: {output_path}")
