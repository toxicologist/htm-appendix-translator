from PIL import Image, ImageDraw, ImageFont
from lib.image_utils import ImageText
from pathlib import Path
import os

# Phrases to translate: will appear in the input prompt, if enabled
phrases_to_translate = [
    'Sitting', 'Turning', 'Raising', 'Touching', 'Lowering', 'Bending',
    'Covering', 'Standing', 'Repeat 12 to 31 two more times, then continue, starting with 32.'
]

# Font: you may change this to something else. Just make sure the .ttf file is in the same directory as the program
font = ImageFont.truetype('arialbd.ttf', 28) 

# Translated: leave blank for input prompt, otherwise make a list here, with the same positions for each phrase as in 'phrases_to_translate'.
translated = []
#translated = ['Sentado', 'Virando', 'Levantando', 'Tocando', 'Abaixando', 'Dobrando', 'Cobrindo', 'Levantando', 'Repita 12 a 31 mais duas vezes, depois continue, começando com 32.']

# Root directory. Don't change this
root_dir = os.path.dirname(os.path.abspath(__file__))

# Input images path - default is the 'images' folder.
images_path = os.path.join(root_dir, 'images')  # change this to whatever you like


# Don't change anything below unless you know what you are doing
x_1 = [128, 546, 966]
y_1 = [720, 1080, 1436, 1786]

x_2 = [128, 546, 955]
y_2 = [312,668,1026,1377,1740]

x_3 = [147, 566, 954]
y_3 = [325, 687, 1043, 1399]

textbox_3 = [(431, 458), 370, 156]
standing_3 = [826, 1604]

def open_images():
    prost1 = Image.open(os.path.join(images_path, 'prost1.png')).convert('RGB')
    d1 = ImageDraw.Draw(prost1)
    prost2 = Image.open(os.path.join(images_path, 'prost2.png')).convert('RGB')
    d2 = ImageDraw.Draw(prost2)
    prost3 = Image.open(os.path.join(images_path, 'prost3.png')).convert('RGB')
    d3 = ImageDraw.Draw(prost3)
    m1 = Image.open(os.path.join(images_path, 'meditation-1.png')).convert('RGB')
    m2 = Image.open(os.path.join(images_path, 'meditation-2.png')).convert('RGB')

    return prost1, d1, prost2, d2, prost3, d3, m1, m2

def write_translations_to_images(images, translated: list):
    prost1, d1, prost2, d2, prost3, d3, m1, m2 = images

    def draw_1(x, y, text):
        x = x_1[x]
        y = y_1[y]
        text = translated[text]
        d1.text((x, y), text, (0, 0, 0),font)
    def draw_2(x, y, text):
        x = x_2[x]
        y = y_2[y]
        text = translated[text]
        d2.text((x, y), text, (0, 0, 0),font)
    def draw_3(x, y, text):
        x = x_3[x]         
        y = y_3[y]
        text = translated[text]
        d3.text((x, y), text, (0, 0, 0),font)

    # image 1
    draw_1(0, 0, 0)
    draw_1(1, 0, 1)
    draw_1(1, 1, 1)
    draw_1(2, 0, 2)
    draw_1(2, 1, 2)
    draw_1(1, 2, 2)
    draw_1(0, 1, 3)
    draw_1(0, 2, 3)
    draw_1(2, 2, 3)
    draw_1(1, 3, 3)
    draw_1(0, 3, 4)
    draw_1(2, 3, 5)
    
    # image 2
    draw_2(0, 3, 1)
    draw_2(0, 4, 1)
    draw_2(2, 2, 2)
    draw_2(1, 3, 2)
    draw_2(1, 4, 2)
    draw_2(1, 0, 3)
    draw_2(1, 1, 3)
    draw_2(1, 2, 3)
    draw_2(2, 3, 3)
    draw_2(2, 4, 3)
    draw_2(0, 0, 4)
    draw_2(0, 1, 4)
    draw_2(0, 2, 5)
    draw_2(2, 0, 6)
    draw_2(2, 1, 6)
    
    # image 3
    draw_3(2, 3, 0)
    draw_3(0, 0, 2)
    draw_3(1, 0, 3)
    draw_3(0, 1, 3)
    draw_3(0, 2, 3)
    draw_3(0, 3, 3)
    draw_3(2, 0, 4)
    draw_3(2, 1, 4)
    draw_3(2, 2, 4)
    draw_3(1, 2, 6)
    draw_3(1, 3, 6)
    d3.text(standing_3, translated[7], (0, 0, 0),font)

    return prost1, d1, prost2, d2, prost3, d3, m1, m2

    
phrases_to_translate = [
    'Sitting', 'Turning', 'Raising', 'Touching', 'Lowering', 'Bending',
    'Covering', 'Standing', 'Repeat 12 to 31 two more times, then continue, starting with 32.'
]


def main():
    if not translated:
        for phrase in phrases_to_translate:
            translated.append(input('Enter the translation for "%s": ' % phrase))

    font_input = input('Enter desired .ttf file for the font - must be in the same folder as the program (leave blank for arial bold): ')
    font_input = font_input if font_input else 'arialbd.ttf'
    font_size = input('Enter desired font size (leave blank for default 28px): ')
    font_size = int(font_size) if font_size else 28
    
    # create output folder
    Path("output/").mkdir(parents=True, exist_ok=True)

    # write all captions
    prost1, d1, prost2, d2, prost3, d3, m1, m2 = write_translations_to_images(open_images(), translated)

    # save images
    prost1.save("output/prost_1.png")
    prost2.save("output/prost_2.png")
    prost3.save("output/prost_3.png")
    m1.save("output/meditation_1.png")
    m2.save("output/meditation_2.png")

    # write the wrapping text in prost_3
    prost3 = ImageText('output/prost_3.png')
    prost3.write_text_box(xy=textbox_3[0], text=translated[8], box_width=textbox_3[1], font_filename=font_input, font_size=font_size, place='justify')
    prost3.save('output/prost_3.png')

    print("Done! Images have been saved to 'output' folder.")
    if os.name == 'nt':
        os.startfile(os.path.join(root_dir, 'output'))
    else:
        input('Press enter to exit.')

if __name__ == '__main__':
    main()