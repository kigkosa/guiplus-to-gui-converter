import os 
import yaml 
import shutil


if not os.path.exists("./input"):
    os.mkdir("./input")

for gui_file in  os.listdir('./input'):
    with open(r'./input/'+gui_file) as file:
        gui = yaml.full_load(file)

    
    
    if not os.path.exists('./output'):
        shutil.rmtree('./output')
    else:
        os.mkdir('./output')


    # deluxmenus
    

