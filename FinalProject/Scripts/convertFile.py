import os
from PIL import Image

path_data_fire_tmp = 'data_tmp/fire/'
path_data_nonfire_tmp = 'data_tmp/nonfire/'

path_data_fire = 'data/fire/'
path_data_nonfire = 'data/nonfire/'
    
def renameFileInFolder(path_folder_tmp, path_folder, prefix):
    k = 0;
    files = os.listdir(path_folder_tmp)
    for file in files:
        path_file_old = os.path.abspath(path_folder_tmp + file)
        print(" + STT:", k, " --> ", path_file_old)
        img = Image.open(path_file_old)
        img = img.convert('RGB')
        path_file_new = os.path.abspath(path_folder + prefix + str(k).zfill(4) + '.jpg')
        img.save(path_file_new)
        img.close()
        
        k += 1;
    print("Done:", path_folder, "- Length:", len(files))
    
renameFileInFolder(path_data_fire_tmp, path_data_fire, "fire_")
renameFileInFolder(path_data_nonfire_tmp, path_data_nonfire, "nonfire_")