import os
import json


def _make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
       

def save_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
                
        
def load_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path) as data_file:
            data_loaded = json.load(data_file)
        return data_loaded
    else:
        _make_dir(os.path.dirname(file_path))
        data = {}
        save_to_json(data, file_path)
        return data
