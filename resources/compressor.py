import os
from PIL import Image

output_dir = 'compressed_images'
os.makedirs(output_dir, exist_ok=True)

def compress_image(input_path, output_path, quality=50):
    with Image.open(input_path) as img:
        img.save(output_path, 'JPEG', quality=quality)

for i in range(1, 68):
    input_filename = f'MMKCMeetup-{i:02d}.jpg'
    output_filename = os.path.join(output_dir, input_filename)
    
    if os.path.exists(input_filename):
        compress_image(input_filename, output_filename)
        print(f'Compressed and saved {input_filename} to {output_filename}')
    else:
        print(f'{input_filename} does not exist')
