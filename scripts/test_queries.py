import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path('data/real_estate.db')

# Run a query and return the result as a df to visualize
def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

def main():
    with open('sql/queries.sql', 'r') as file:
        queries = file.read().split(';')
    
    for query in queries:
        query = query.strip()
        if not query:
            continue
            
        query_name = query.split('\n')[0].replace('--', '').strip()
        print(f"\n=== {query_name} ===")
        
        try:
            results = run_query(query)
            print("\nResults:")
            print(results.to_string(index=False))
            print(f"\nTotal rows: {len(results)}")
        except Exception as e:
            print(f"Error running query: {e}")

if __name__ == "__main__":
    main() 