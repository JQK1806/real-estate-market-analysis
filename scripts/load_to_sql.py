import pandas as pd
import sqlite3
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create SQL database and initialize the schema
def create_database():
    db_path = Path("data/real_estate.db")
    logger.info(f"Creating database at {db_path.absolute()}")
    
    db_path.parent.mkdir(exist_ok=True)
    
    schema_path = Path("sql/schema.sql")
    logger.info(f"Reading schema from {schema_path.absolute()}")
    
    with open(schema_path, "r") as f:
        schema = f.read()
    
    conn = sqlite3.connect(db_path)
    conn.executescript(schema)
    logger.info("Database schema created successfully")
    return conn

# Load cleaned data into db
def load_data(conn):
    try:
        csv_path = Path("data/cleaned/data_cleaned.csv")
        logger.info(f"Reading data from {csv_path.absolute()}")
        
        df = pd.read_csv(csv_path)
        logger.info(f"Read {len(df)} rows from CSV")
        
        # Convert date columns to datetime
        date_columns = ['listing_date']
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])
                logger.info(f"Converted {col} to datetime")
        
        df.to_sql('listings', conn, if_exists='replace', index=False)
        logger.info(f"Successfully loaded {len(df)} records into database")
        
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

# Create and load data into db
def main():
    try:
        conn = create_database()
        load_data(conn)
        conn.close()
        logger.info("Database creation and data loading completed successfully")
    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        raise

if __name__ == "__main__":
    main()