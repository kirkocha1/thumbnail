__author__ = 'kochanik'

from PIL import Image
import os
import argparse


def resize(img,new_size,save_dir):
    for im in img:
        with Image.open(im) as imap:
            ima = imap
            if ima.size > new_size:
                ima.thumbnail(new_size)
                final_dir = save_dir + os.path.basename(im)
                ima.save(final_dir)


def get_all_images(dir):
    imagefilepath = []
    for root, dirs, files in os.walk(dir):
        for original_name in files:
            name = original_name.lower()
            if name.endswith('.jpg') or name.endswith('.jpeg'):
                imagefilepath.append(os.path.join(root, original_name))
    return imagefilepath


def main():
    parser = argparse.ArgumentParser(description='image resizer')
    parser.add_argument('-d',dest='dir', metavar='DIRECTORY',type=str,required=True,
                        help='input directory on your computer, example /disk1/dir1/')
    parser.add_argument('-s',dest='size', help='definition of the jpg file', type=int,nargs=2)
    parser.add_argument('-f',dest='save_dir', help='directory of the resized files',
                        type=str, required=True)
    arg = parser.parse_args()

    dir = arg.dir
    size = tuple(arg.size)
    if not arg.size:
        size = (600, 800)

    save_dir = arg.save_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    imgpath = get_all_images(dir)
    resize(imgpath, size, save_dir)

if __name__ == '__main__':
    main()



