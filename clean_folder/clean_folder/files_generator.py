from os import path
import shutil
from pathlib import Path
from random import randint, choice, choices
import numpy
from PIL import Image

MESSAGE = "Hello, Привіт"


def get_random_filename():
    random_value = '()+,-0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz' \
                   '{}~абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    return ''.join(choices(random_value, k=8))


def generate_text_files(path):
    documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    with open(path / f"{get_random_filename()}.{choice(documents).lower()}", "wb") as f:
        f.write(MESSAGE.encode())


def generate_archive_files(path):
    archive = ('ZIP', 'GZ', 'TAR')
    shutil.make_archive(f"{path}/{get_random_filename()}", f'{choice(archive).lower()}', path)


def generate_image(path):
    images = ('JPEG', 'PNG', 'JPG', 'SVG')
    image_array = numpy.random.rand(100, 100, 3) * 255
    image = Image.fromarray(image_array.astype('uint8'))
    image.save(f"{path}/{get_random_filename()}.{choice(images).lower()}")

def generate_video_files(path):
    video_files = ('AVI', 'MP4', 'MOV', 'MKV')
    video_files.save(f"{path}/{get_random_filename()}.{choice(video_files).lower()}")

def genetate_music(path):
    music = ('MP3', 'OGG', 'WAV', 'AMR')
    music.save(f"{path}/{get_random_filename()}.{choice(music).lower()}")


def generate_folders(path):
    folder_name = ['temp', 'folder', 'dir', 'tmp', 'OMG', 'is_it_true', 'no_way', 'find_it']
    folder_path = Path(
        f"{path}/" + '/'.join(choices(folder_name, weights=[10, 10, 1, 1, 1, 1, 1, 1], k=randint(5, len(folder_name)))))
    folder_path.mkdir(parents=True, exist_ok=True)


def generate_folder_forest(path):
    for i in range(0, randint(2, 5)):
        generate_folders(path)


def generate_random_files(path):
    for i in range(3, randint(5, 7)):
        function_list = [generate_text_files, generate_archive_files, generate_image, genetate_music, generate_video_files]
        choice(function_list)(path)


def parse_folder_recursion(path):
    for elements in path.iterdir():
        if elements.is_dir():
            generate_random_files(path)
            parse_folder_recursion(elements)


def exist_parent_folder(path):
    path.mkdir(parents=True, exist_ok=True)


def file_generator():
    Path("temp")
    exist_parent_folder(path)
    generate_folder_forest(path)
    parse_folder_recursion(path)


if __name__ == 'main':
    file_generator(Path("temp"))