import os
import pyzipper

# INPUT_PATH = '/mnt/warehouse/BackUp/MediaCenter'
# OUTPUT_PATH = '/mnt/store/YandexDisk/BackUp'

# INPUT_PATH = '/home/user/Docs/INPUT'
# OUTPUT_PATH = '/home/user/Docs/OUTPUT'

INPUT_PATH = 's:\\MediaCenter\\Documents\\'
OUTPUT_PATH = 'd:\\Data\\Result\\'

PASSWORD = b'pass'


def archive(file, in_path, out_path):
    os.makedirs(out_path, exist_ok=True)
    with pyzipper.AESZipFile(os.path.join(out_path, f'{file}.zip'),
                             'w',
                             compression=pyzipper.ZIP_LZMA,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(PASSWORD)
        zf.write(os.path.join(in_path, file), arcname=file)


def archive_dir(in_path, out_path):
    for file in os.listdir(in_path):
        if os.path.isfile(os.path.join(in_path, file)):
            archive(file, in_path, out_path)
        elif os.path.isdir(os.path.join(in_path, file)):
            archive_dir(os.path.join(in_path, file),
                        os.path.join(out_path, file))


archive_dir(INPUT_PATH, OUTPUT_PATH)
