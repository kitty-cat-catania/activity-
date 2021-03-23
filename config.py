import os
import json

<<<<<<< HEAD
=======

>>>>>>> darren
key_dict = {}
keys_json_path = os.path.expanduser(os.path.join("~", ".api_keys.json"))
if os.path.exists(keys_json_path):
    with open(keys_json_path, 'r') as keys_file:
        key_dict = json.load(keys_file)
else:
<<<<<<< HEAD
    print(f"Could not find {keys_json_path}")
=======
    print(f"Could not find {keys_json_path}")
>>>>>>> darren
