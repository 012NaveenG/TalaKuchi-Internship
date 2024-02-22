
import os
from PIL import Image, ImageDraw, ImageFont


def take_screenshot(filepath,screenshot_dir,line_number,search_word):

    with open (filepath, "r", encoding="utf-8",errors="replace") as file:
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        lines = file.readlines()
        start_line = max(0,line_number - 5)
        end_line = min(len(lines),line_number + 5 )

        relevant_line = lines[start_line:end_line]
        relevant_content = ''.join(relevant_line)
        

        secret_word = search_word.replace('android', '').replace('=','_').replace('"','_').replace('"','')

        filename = f'{secret_word}_{os.path.basename(filepath)}_{line_number}.png'

        screenshot_path = os.path.join(screenshot_dir,filename)

        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


        image = Image.new('RGB',(3000,600), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, 20)
        

        draw.text((5,100),relevant_content,fill=(0,0,0),font=font)

        draw.text((5,50),f'File location : {filepath}',fill=(0,0,0),font=ImageFont.truetype(font_path,30))

        image.save(screenshot_path)
        print(f"Screenshot saved in {screenshot_dir}")