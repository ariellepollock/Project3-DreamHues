import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_imgix_palette(image_url):
    imgix_api_url = 'https://api.imgix.com/v2/palette'
    imgix_api_key = os.getenv('IMGIX_KEY')

    headers = {
        'Authorization': f'Bearer {imgix_api_key}',
    }

    params = {
        'url': image_url,
    }

    try:
        response = requests.get(imgix_api_url, headers=headers, params=params)
        response.raise_for_status()

        palette_data = response.json()
        if 'palette' in palette_data:
            palette = palette_data['palette']
            return palette
        else:
            print('Imgix API error: Palette is None')
            return None
    except requests.RequestException as e:
        print(f'Error calling Imgix API: {e}')
        return None