from PIL import Image, ImageOps
import logging
import math
import requests
from telegraph import Telegraph
def create_collage(image_paths, output_path, border_size=10):

    images = [Image.open(image_path) for image_path in image_paths]

    grid_size = math.ceil(math.sqrt(len(images)))

    max_width = max(image.size[0] for image in images) + border_size * 2
    max_height = max(image.size[1] for image in images) + border_size * 2


    collage_width = grid_size * max_width + (grid_size - 1) * border_size
    collage_height = grid_size * max_height + (grid_size - 1) * border_size


    collage = Image.new('RGB', (collage_width, collage_height), color='white')


    for i, image in enumerate(images):
        row = i // grid_size
        col = i % grid_size
        x = col * (max_width + border_size)
        y = row * (max_height + border_size)
        

        image_with_border = ImageOps.expand(image, border=border_size, fill='white')
        
        collage.paste(image_with_border, (x, y))

    collage.save(output_path)


def upload_image_to_telegraph(image_path):

    telegraph = Telegraph()
    telegraph.create_account(short_name='Anon')

    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://telegra.ph/upload',
            files={'file': ('file', image_file, 'image/jpeg')}
        )
        
    response_json = response.json()
    
    if response.status_code == 200 and response_json[0].get('src'):
        image_url = 'https://telegra.ph' + response_json[0]['src']
        return image_url
    else:
        raise Exception("Rasimni yuklashda xatolik yuz berdi")