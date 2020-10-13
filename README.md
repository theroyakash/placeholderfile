# Placeholder file
Fed up coming up names for your files? Placholder file name generator is your solution. Generates placholder name with any prefix or suffix.
## How to use
### Installation
Open your terminal and pip install this library like `pip install https://github.com/theroyakash/placeholderfile/tarball/main`
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