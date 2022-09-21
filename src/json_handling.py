import json


def write_lost_revenue_to_dict(
    lost_revenue:float
    ) -> dict:
    return {
        'lost_revenue': lost_revenue
    }


def write_dict_to_json_object(
    d:dict) -> str:
    json_object = json.dumps(
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