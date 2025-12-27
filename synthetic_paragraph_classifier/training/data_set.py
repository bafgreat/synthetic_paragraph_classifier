from pathlib import Path
from typing import List, Tuple

import pandas as pd


def load_training_data(
    data_dir: Path | None = None,
    filename: str = "Training_data_for_sentiment_analysis.xlsx",
    text_column: str = "paragraph",
    label_column: str = "label",
) -> Tuple[List[str], List[int]]:
    """
    Load training data for synthetic paragraph classification.

    Parameters
    ----------
    data_dir : Path | None, optional
        Directory containing the training data file. If None, defaults to
        'data/training_data' in the project root.
    filename : str, optional
        Name of the Excel file containing training data.
    text_column : str, optional
        Name of the column containing paragraph texts.
    label_column : str, optional
        Name of the column containing labels (0 or 1).

    Returns
    -------
    texts : list[str]
        Paragraphs.
    labels : list[int]
        Corresponding labels.
    """

    # Resolve project root robustly
    if data_dir is None:
        project_root = Path(__file__).resolve().parents[2]
        data_dir = project_root / "data" / "training_data"

    data_path = data_dir / filename
    if not data_path.exists():
        raise FileNotFoundError(f"Training data not found: {data_path}")

    # Load Excel
    df = pd.read_excel(data_path)

    # Validate required columns
    missing = {text_column, label_column} - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # --- Clean paragraphs: drop NaN and drop len==0 after strip ---
    df = df.dropna(subset=[text_column])
    df[text_column] = df[text_column].astype(str).str.strip()
    df = df[df[text_column].str.len() > 0]

    # --- Clean labels: drop NaN and coerce to int safely ---
    df = df.dropna(subset=[label_column])
    # If labels might be "0"/"1" strings, floats, etc., this is safer:
    df[label_column] = pd.to_numeric(df[label_column], errors="raise").astype(int)

    text = df[text_column].tolist()
    label = df[label_column].tolist()
    return text, label


if __name__ == "__main__":
    texts, labels = load_training_data()
    print(f"Loaded {len(texts)} paragraphs with labels.")
    positive_count = sum(1 for lbl in labels if lbl == 1)
    negative_count = sum(1 for lbl in labels if lbl == 0)
    print(f"Positive samples: {positive_count},  Negative samples: {negative_count}")
