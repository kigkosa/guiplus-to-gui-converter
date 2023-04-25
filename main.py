import os 
import yaml 
import shutil
import json



def conver_json_to_mc(json_text):
        display_name_dict = json.loads(json_text)


        # Extract the message text and formatting
        text = display_name_dict["text"]
        color = display_name_dict["color"]
        italic = display_name_dict["italic"]

        # Define the Minecraft color codes
        color_codes = {
            "black": "&0",
            "dark_blue": "&1",
            "dark_green": "&2",
            "dark_aqua": "&3",
            "dark_red": "&4",
            "dark_purple": "&5",
            "gold": "&6",
            "gray": "&7",
            "dark_gray": "&8",
            "blue": "&9",
            "green": "&a",
            "aqua": "&b",
            "red": "&c",
            "light_purple": "&d",
            "yellow": "&e",
            "white": "&f"
        }

        # Convert the color name to a color code
        color_code = color_codes[color]

        # Define the Minecraft formatting codes
        format_codes = {
            "bold": "&l",
            "italic": "&o",
            "underline": "&n",
            "strikethrough": "&m",
            "obfuscated": "&k"
        }

        # Convert the italic formatting to a formatting code
        format_code = format_codes["italic"] if italic else ""

        # Create the Minecraft chat message string
        return f"{color_code}{format_code}{text}"


if not os.path.exists("./input"):
    os.mkdir("./input")

for gui_file in  os.listdir('./input'):
    with open(r'./input/'+gui_file) as file:
        gui = yaml.full_load(file)
    
    if os.path.exists('./output'):
        shutil.rmtree('./output')
        os.mkdir('./output')
    else:
        os.mkdir('./output')


    # deluxmenus
    if not os.path.exists("./output/deluxmenus"):
        os.mkdir("./output/deluxmenus")
    deluxmenu = {}
    deluxmenu["open_command"] = gui["inv"]["alias"]
    deluxmenu["size"] = gui["inv"]["size"]
    deluxmenu["menu_title"] = gui["inv"]["title"]
    deluxmenu["items"] = {}
    for slot in gui["inv"]["items"]:
        id = first_key = list(gui["inv"]["items"][slot].keys())[0]
        
        display_name = conver_json_to_mc(gui["inv"]["items"][slot][id]["item"]["meta"]["display-name"])
        lores = []
        for lore in gui["inv"]["items"][slot][id]["item"]["meta"]["lore"]:
            lores.append(conver_json_to_mc(lore))

        


        deluxmenu["items"][id] = {
            "material": gui["inv"]["items"][slot][id]["item"]["type"],
            "slot": slot,
            "display_name": display_name,
            "lore": lores,
        }
        if gui["inv"]["items"][slot][id]["item"]["meta"]["custom-model-data"]:
            deluxmenu["items"][id]["model_data"] = gui["inv"]["items"][slot][id]["item"]["meta"]["custom-model-data"]
        if gui["inv"]["items"][slot][id]["leftaction"]:
            print(gui["inv"]["items"][slot][id]["leftaction"])
    with open(r'./output/deluxmenus/'+gui_file+".yml", 'w') as file:
        documents = yaml.dump(deluxmenu, file)