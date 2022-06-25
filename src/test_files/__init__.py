import sys
from pathlib import Path

source_path = Path(__file__).parents[1].resolve()
print(source_path)
sys.path.append(str(source_path))