import os
from glob import glob

def get_font_names(folder_path):
    font_files = glob(os.path.join(folder_path, '*'))
    font_names = [os.path.splitext(os.path.basename(file))[0] for file in font_files]
    return font_names

def save_to_text(font_names, output_path):
    with open(output_path, 'w') as file:
        file.write(' '.join(font_names))

if __name__ == "__main__":
    folder_path = r"C:\Users\grant\OneDrive\Code\fonts"
    output_path = 'output.txt'

    font_names = get_font_names(folder_path)
    save_to_text(font_names, output_path)

    print(f"Font names have been saved to {output_path}")
