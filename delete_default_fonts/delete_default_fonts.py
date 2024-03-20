import os

def get_default_fonts():
    default_fonts = set()
    system_fonts_folder = r"C:\Windows\Fonts"

    for font_file in os.listdir(system_fonts_folder):
        font_name, _ = os.path.splitext(font_file)
        default_fonts.add(font_name.lower())

    return default_fonts

def delete_default_fonts(folder_path):
    default_fonts = get_default_fonts()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            font_name = os.path.splitext(file)[0].lower()

            if font_name in default_fonts:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted font file: {file}")

if __name__ == "__main__":
    folder_path = r"C:\Users\grant\OneDrive\Code\fonts"

    # Ensure the folder path is correct and the script has necessary permissions
    delete_default_fonts(folder_path)
