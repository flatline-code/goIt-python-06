import os
import sys
import zipfile

def normalize(string):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = t
        TRANS[ord(c.upper())] = t.upper()
        
    normalized_string = ''

    for char in string:
        if char.isalpha() or char.isnumeric():
            normalized_string += char  
        else:
            normalized_string += '_'   
        
    return normalized_string.translate(TRANS)

def sort_files(original_path):
    all_folders = {
      'images': ['jpeg', 'png', 'jpg', 'svg'],
      'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
      'audio': ['mp3', 'ogg', 'wav', 'amr'],
      'video': ['avi', 'mp4', 'mov', 'mkv'],
      'archives': ['zip'],
    }

    all_files = os.listdir(original_path)

    for file in all_files:
        file_path = os.path.join(original_path, file)

        if os.path.isdir(file_path):
          
            if file in all_folders.keys():
                continue
            
            if len(os.listdir(file_path)) == 0:
                os.rmdir(file_path)
                continue

            sort_files(file_path)

            os.rename(file_path, os.path.join(original_path, normalize(file)))

        file_type = file.split('.')[-1]

        if file_type in all_folders['images']:
            if not os.path.exists(os.path.join(original_path, 'images')):
                os.makedirs(os.path.join(original_path, 'images'))
            
            normalized_file = normalize(file.removesuffix(f'.{file_type}')) + f'.{file_type}'
            new_file_path = os.path.join(os.path.join(original_path, 'images'), normalized_file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['documents']:
            if not os.path.exists(os.path.join(original_path, 'documents')):
                os.makedirs(os.path.join(original_path, 'documents'))

            normalized_file = normalize(file.removesuffix(f'.{file_type}')) + f'.{file_type}'
            new_file_path = os.path.join(os.path.join(original_path, 'documents'), normalized_file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['audio']:
            if not os.path.exists(os.path.join(original_path, 'audio')):
                os.makedirs(os.path.join(original_path, 'audio'))

            normalized_file = normalize(file.removesuffix(f'.{file_type}')) + f'.{file_type}'
            new_file_path = os.path.join(os.path.join(original_path, 'audio'), normalized_file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['video']:
            if not os.path.exists(os.path.join(original_path, 'video')):
                os.makedirs(os.path.join(original_path, 'video'))

            normalized_file = normalize(file.removesuffix(f'.{file_type}')) + f'.{file_type}'
            new_file_path = os.path.join(os.path.join(original_path, 'video'), normalized_file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['archives']:
            if not os.path.exists(os.path.join(original_path, 'archives')):
                os.makedirs(os.path.join(original_path, 'archives'))

            normalized_file = normalize(file.removesuffix(f'.{file_type}')) + f'.{file_type}'
            new_file_path = os.path.join(os.path.join(original_path, 'archives'), normalized_file)
            os.replace(file_path, new_file_path)

            unzip_folder = normalize(file.removesuffix(f'.{file_type}'))
            unzip_folder_path = os.path.join(os.path.join(original_path, 'archives'), unzip_folder)
            archive = zipfile.ZipFile(new_file_path)
            archive.extractall(unzip_folder_path)

if __name__ == '__main__':
    try:
        original_path = os.path.join(sys.argv[1])
        sort_files(original_path)
    except IndexError:
        print('Enter path to the directory.')
    