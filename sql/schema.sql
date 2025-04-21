CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    bedrooms INTEGER,
    bathrooms DECIMAL(3, 1),
    square_feet INTEGER,
    lot_size DECIMAL(10, 2),
    year_built INTEGER,
    property_type TEXT,
    listing_date DATE,
    days_on_market INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_listings_zip_code ON listings(zip_code);
CREATE INDEX IF NOT EXISTS idx_listings_price ON listings(price);
CREATE INDEX IF NOT EXISTS idx_listings_listing_date ON listings(listing_date);