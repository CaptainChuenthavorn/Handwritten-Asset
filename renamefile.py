import os

folder_path = "C:\\Users\\captain\\0-Handwritten CNN\\binarized_image\\amikacin"

file_names = os.listdir(folder_path)
file_names.sort()

new_name_counter = 1

for file_name in file_names:
    if new_name_counter>100:
        num_counter_str = '0'+str(new_name_counter)
    elif new_name_counter>10:
        num_counter_str = '00'+str(new_name_counter)
    else:
        num_counter_str = '000'+str(new_name_counter)
    file_path = os.path.join(folder_path, file_name)
    new_file_name = "amoxicillin-"+num_counter_str+ ".png"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(file_path, new_file_path)
    new_name_counter += 1
