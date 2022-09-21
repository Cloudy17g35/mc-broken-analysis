from pathlib import Path


def create_data_dir_if_not_exists(path:str) -> None:
    data_dir:Path = Path(path)
    data_dir.mkdir(
        parents=True,
        exist_ok=True
        )