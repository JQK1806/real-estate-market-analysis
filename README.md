# Real Estate Market Analysis

This project analyzes house prices using advanced regression techniques. The analysis is based on the Kaggle competition "House Prices - Advanced Regression Techniques".

## Project Structure

```
.
├── data/               # Data directory
│   ├── raw/           # Original, immutable data
│   └── cleaned/       # Cleaned and processed data
├── scripts/           # Data processing and analysis scripts
├── models/            # Trained models and model-related code
├── dashboards/        # Visualization dashboards
├── notebooks/         # Jupyter notebooks for exploration
└── sql/              # SQL queries and database scripts
```

## Data Source

The dataset used in this project comes from the [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) Kaggle competition. The dataset contains 79 explanatory variables describing various aspects of residential homes in Ames, Iowa.

### Dataset Description

- **train.csv**: Contains the training set with 1460 examples
- **test.csv**: Contains the test set with 1459 examples
- **data_description.txt**: Contains a detailed description of each feature

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-estate-market-analysis.git
   cd real-estate-market-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset:
   - Download from the [Kaggle competition page](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
   - Place the files in the `data/raw/` directory

## Data Processing Pipeline

The project includes a data cleaning pipeline that:
1. Handles missing values in numerical and categorical columns
2. Converts ordinal categorical variables to numeric
3. Creates dummy variables for categorical features
4. Adds derived features (age, price per square foot)

To run the data cleaning pipeline:
```bash
python scripts/clean_data.py
```
