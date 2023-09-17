"""
Test goes here

"""

from main import data_filter
import polars as pl


def test_data_filter():
    mock_csv_file = pl.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
            "Sex": ["F", "M", "M", "M", "F", "M"],
        }
    )
    res = data_filter(mock_csv_file)
    assert len(res) == 4


if __name__ == "__main__":
    test_data_filter()
    print("All tests passed.")
