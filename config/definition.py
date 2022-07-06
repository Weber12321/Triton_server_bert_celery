from pathlib import Path, PurePath

ROOT_DIR = PurePath(__file__).parent.parent

LOGS_DIR = Path(ROOT_DIR / "logs")
Path(LOGS_DIR).mkdir(exist_ok=True)

DATA_DIR = Path(ROOT_DIR / "data")
Path(DATA_DIR).mkdir(exist_ok=True)

MODEL_DIR = Path(ROOT_DIR / "model")
Path(MODEL_DIR).mkdir(exist_ok=True)

