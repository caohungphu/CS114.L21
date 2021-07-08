import os

path_folder = ['full', 'train', 'test', 'validation']
path_label = ['fire', 'nonfire']

def renameFileInFolder(full_path, prefix):
    k = 0;
    files = os.listdir(full_path)
    for file in files:
        path_file_old = os.path.abspath(full_path + "/" + file)
        path_file_new = os.path.abspath(full_path + "/"  + prefix + str(k).zfill(4) + '.jpg')
        os.rename(path_file_old, path_file_new)
        k += 1
    print("Done:", full_path, "- Length:", len(files))

for path in path_folder:
    for sub_path in path_label:
        full_path = path + "/" + sub_path
        prefix = sub_path + "_"
        renameFileInFolder(full_path, prefix)
