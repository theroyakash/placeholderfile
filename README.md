# Placeholder file
Fed up coming up names for your files? Placholder file name generator is your solution. Generates placholder name with any prefix or suffix.
## How to use
### Installation
Open your terminal and pip install this library like `pip install placeholderfile`
### Trying first code
- Now import the generator function from the generator module
```python
from placeholderfile.generateName import generateName as gn
```
- Now to generate placeholder names for some file specify the suffix and an optional prefix and an optional seed to recreate the results on a different machine:
```python
print(gn(suffix='.jpg'))
print(gn(suffix ='.mp4', prefix='video_'))
```
### Generate a batch of file names
```python
for i in range(5):
    print(gn(suffix =f'_{i}.mp4', prefix='video_'))
```

Here is an example of how random names are generated
```plain text
video_lcvddegdtq_0.mp4
video_nqwmjskzxa_1.mp4
video_vbpvbvpyhv_2.mp4
video_olxffcxayv_3.mp4
video_fmopkmtpqg_4.mp4
```
### Practical Example
AKDPRFramework has a built in image downloader module. When downloading image using same name for the image file can create conflict and overwrite the previously dowloaded image. So making a random name for image everytime is a good practice.

Here is an example how AKDPRFramework implements this module
```python
# Genearting a new name for each file downloaded.
from placeholderfile.generateName import generateName as gn

# Download image from the WEB
import requests
from PIL import Image
import io
import os
import sys

def downloadImageFromURL(url):
    '''
    Downloads Image from any image URL
    To know more about what are image URL visit here: https://bit.ly/what-are-imageurl
    '''
    b = requests.get(url).content
    image = Image.open(io.BytesIO(b))

    # Generate a new name for every new image file generated
    filename = gn(suffix='.jpg', prefix=None, seed=None)
    image.save(filename)
    print(f'Image saved at {os.getcwd()}/{filename}')
```

# UUID Generator
placeholderfile can now generate UUIDs for databases.

To be able to generate random 22 character length UUIDs use the following code:
```python
from placeholderfile.UUIDGenerator import UUIDGenerator

generator = UUIDGenerator(dtype='str-major')    # You can choose also 'int-major' for generating integer dominant UUID
uuid = generator.generate()

print(uuid)
```