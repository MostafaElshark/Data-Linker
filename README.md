# Data Linking and Connecting

This repository contains Python scripts for cleaning, linking, and connecting data. Specifically, it includes three classes:

1. `TextCleaner`: A class for cleaning text data.
2. `DataLinker`: A class for linking two datasets based on specified criteria.
3. `DataConnector`: A class for connecting two datasets based on the links created by `DataLinker`.

## Requirements

- Python 3.x
- pandas
- recordlinkage
- fuzzywuzzy
- nltk

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## How to Use

1. Clone this repository or download the source code.
2. Install the required packages mentioned above.
3. Update the `main.py` script with the paths to your datasets and any other customizations you need.
4. Run the `main.py` script.

The `main.py` script will clean the data, link the two datasets, connect them, and save the results to CSV files.

## Customization

Here are the places where you might need to customize the code to match your data:

- `TextCleaner.py`: 
  - In the `regex_cleaning` method in the `TextCleaner` class, you can customize the `replacements` dictionary to include any other specific text replacements or removals you need.

- `DataLinker.py`: 
  - In the `preprocess` method, customize the columns that you want to clean and preprocess.
  - In the `create_pairs` method, customize the column that you want to block the data on.
  - In the `compare_pairs` method, customize the columns that you want to compare and the thresholds for each comparison.
  - In the `classify` method, customize the weights for each comparison and the threshold for considering a pair as a match.
  - In the `post_process` method, customize the logic for selecting the best match if there are multiple matches for the same record.

- `DataConnector.py`: 
  - In the `connect_data` method, customize the logic for connecting the two datasets based on the matches found by `DataLinker`.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
