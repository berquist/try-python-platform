import json
from pathlib import Path

import pandas as pd

if __name__ == "__main__":

    p = Path(__file__).resolve()
    data_dir = p.parent / "data"
    results = [
        json.loads(result.read_text(encoding="utf-8"))
        for result in sorted(data_dir.glob("*.json"))
    ]
    df = pd.DataFrame(results)
    print(df)
