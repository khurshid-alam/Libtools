import json
import time
import datetime
import dropbox
from dropbox.exceptions import ApiError

def file_exists_in_db(dbx,path):
    try:
        dbx.files_get_metadata(path)
        return True
    except:
        return False

def load_json_from_db(dbx, path):
    try:
        m, res = dbx.files_download(path)
    except ApiError as e:
        res = None
        print (e.error)
        
    if res:
        data = ((res.content).decode('utf-8')).strip('\n')
        data = json.loads(data)
    else:
        data = {}
        
    return data
    
    
def save_json_to_db(dbx, path, **data):
    data_s = json.dumps(data, indent=4)
    data_b = data_s.encode('ascii')
    
    mtime = int(time.time())
    mode = dropbox.files.WriteMode.overwrite

    try:
        res = dbx.files_upload(
                            data_b, path, mode,
                            client_modified=datetime.datetime(*time.gmtime(mtime)[:6]),
                            mute=True)
    except ApiError as e:
        print (e)
        return None
                        
    return res
