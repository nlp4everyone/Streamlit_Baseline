import json
import os
import datetime

def save_json(model_name:str,data:list):
    # Defind log id
    log_id = os.getpid()

    # Define time
    current_time = datetime.datetime.now()
    string_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Save file
    with open(f"logging/{model_name}_log_{log_id}.json","w") as f:
        logging_state = {
            "messages":data,
            "last_update":string_time
        }
        json.dump(logging_state,f,indent=4)
