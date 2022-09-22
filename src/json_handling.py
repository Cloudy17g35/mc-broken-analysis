import json
from typing import Dict


def write_lost_revenue_to_dict(lost_revenue:float) -> Dict[str, float]:
    
    return {
        'lost_revenue': lost_revenue
    }


def write_dict_to_json_object(d:dict) -> str:
    json_object:str = json.dumps(
        d,
        indent=4,
        sort_keys=True,
        default=str
        )
    return json_object


def write_json_object_to_path(
    json_object:str,
    path:str) -> None:
    with open(path, 'w') as f:
        f.write(
            json_object
            )


def read_json_to_dict(
    path:str
    ) -> dict:
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

