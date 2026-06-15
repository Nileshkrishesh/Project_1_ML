# Data Directory

Place your dataset files here:

## Required Files

1. **train.csv** - Training data with labels (~10,000 rows)
   - Contains all features + `Converted` target column
   
2. **public_test.csv** - Labeled validation set
   - Used for threshold optimization and evaluation
   - Contains all features + `Converted` target column

3. **private_test.csv** - Unlabeled test set
   - Used for final submission predictions
   - Contains all features except `Converted`

4. **sample_submission.csv** (optional)
   - Template showing required submission format
   - Columns: User_ID, Converted

## Dataset Features

### User Demographics
- `Age` - User age (numeric, has missing values)
- `Income` - Annual income (numeric, has missing values)
- `City_Tier` - City tier classification (1, 2, or 3)

### Browsing Behavior
- `Pages_Viewed` - Number of pages viewed in session
- `Products_Viewed` - Number of products viewed
- `Time_On_Site` - Time spent on site in minutes (has missing values)

### Purchase History
- `Previous_Purchases` - Number of past purchases

### Device & Traffic
- `Device_Type` - Type of device (Mobile, Desktop, Tablet)
- `Traffic_Source` - How user arrived (Organic, Paid, Social, etc.)

### Marketing
- `Campaign_Clicked` - Whether user clicked on campaign (0 or 1)
- `Discount_Seen` - Whether user saw discount (0 or 1)

### User Feedback
- `User_Rating` - User rating (1-5)
- `Cart_Abandonment` - Whether user abandoned cart (0 or 1)

### Target Variable
- `Converted` - Whether user made a purchase (0 or 1)

## Download Instructions

Download the dataset from the hackathon portal:
https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/

## Notes

- Missing values exist in: Age, Income, Time_On_Site
- Class imbalance: ~69% non-converted, ~31% converted
- Total features: 13 base features
- File format: CSV (comma-separated values)
