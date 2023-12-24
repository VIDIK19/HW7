import os
import shutil
import sys
import argparse

def normalize(name):
    cyrillic_to_latin = {
        "а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g", "д": "d", "е": "e", "є": "ie",
        "ж": "zh", "з": "z", "и": "y", "і": "i", "ї": "i", "й": "i", "к": "k", "л": "l",
        "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ю": "iu", "я": "ia"
    }

    for cyr, lat in cyrillic_to_latin.items():
        name = name.replace(cyr, lat)
        name = name.replace(cyr.upper(), lat.upper())

    normalized_name = ''.join(
        char if (char.isalnum() or char == '.') else '_' for char in name)

    return normalized_name

def process_folder(folder_path):
    known_extensions = {
        'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
        'video': ['AVI', 'MP4', 'MOV', 'MKV'],
        'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
        'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
        'archives': ['ZIP', 'GZ', 'TAR']
    }

    for entry in os.scandir(folder_path):
        if entry.is_dir():
            if entry.name not in ['archives', 'video', 'audio', 'documents', 'images']:
                process_folder(entry.path)
                if not os.listdir(entry.path):
                    os.rmdir(entry.path)
            continue


def main():
    parser = argparse.ArgumentParser(description="Очищення папки від непотрібних файлів")
    parser.add_argument('path', nargs='?', default=os.getcwd(), help='Шлях до папки, яку потрібно очистити')
    args = parser.parse_args()

    process_folder(args.path)