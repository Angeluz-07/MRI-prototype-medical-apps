from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
WORKSPACE_DEFAULT_FOLDER = DATA_DIR / "workspace" / "default"
RESULTS_FOLDER = DATA_DIR / "out"
