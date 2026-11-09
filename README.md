# 🐱 Cat Growth Dashboard
A Python project that tracks cat growth, analyzes weight history, and generates growth charts using real measurement data.

This project was built as my second Python project after completing a Smart File Organizer. The goal was to practice working with:

- CSV files
- Functions
- Dictionaries
- Lists and tuples
- Date calculations
- Data visualization with Matplotlib
- Refactoring and code organization

## Features
✅ Read cat weight data from a CSV file

✅ Calculate age automatically from birth dates

✅ Display a growth dashboard summary

✅ Generate individual growth charts for each cat

✅ Track:

- Current weight
- Ideal weight range
- Growth trend
- Highest weight
- Weight gain
- Number of measurements

✅ Visualize:

- Kitten phase
- Adult phase
- Adult threshold (12 months)
- Healthy adult weight range

## Dashboard Output
==== Cat Growth Dashboard Summary ====

#### Misty 🐱

- Age: 3y 3m
- Current Weight: 5.50 kg
- Ideal Range: 4.8 - 5.8 kg
- Status: ✅ Healthy
- Trend: 📈 Increasing

- First Weight: 1.03 kg
- Highest Weight: 5.50 kg
- Weight Gain: 4.47 kg


Measurements: 76

#### Ash 🐱

- Age: 3y 0m
- Current Weight: 7.30 kg
- Ideal Range: 6.8 - 7.5 kg
- Status: ✅ Healthy
- Trend: 📉 Decreasing

- First Weight: 1.78 kg
- Highest Weight: 7.45 kg
- Weight Gain: 5.52 kg

Measurements: 63

## Growth Chart

The project automatically creates PNG charts showing:

- Weight vs Age
- Kitten to Adult transition
- Healthy adult weight range
- Current status


![Misty Growth Chart](misty_growth.png)

![Ash Growth Chart](ash_growth.png)


## Project Structure
``` 
Cat_Growth_Dashboard/
│
├── main.py
├── cat_data.csv
├── project_development.py
├── charts/
│   ├── misty_growth.png
│   └── ash_growth.png
└── README.mdd
```
#### Files
- main.py – final application
- cat_data.csv – weight history dataset
- project_development.py – learning and experimentation code
- charts/ – generated growth charts
- README.md – project documentation

## Technologies Used
- Python 3
- Matplotlib
- Datetime module

## Dataset
The dashboard uses real weight measurements collected over several years for two cats:

- Misty
- Ash

The dataset currently contains more than 130 historical measurements.

## What I Learned
During this project I learned how to:

- Read and process CSV files
- Work with dictionaries containing lists
- Store and manage related data using tuples
- Calculate age from dates
- Create graphs with Matplotlib
- Use helper functions to avoid repeating code
- Refactor code into reusable functions
- Organize a larger Python project

## Future Improvements
Possible future versions may include:

- Improved trend detection
- Weight alerts
- More advanced health statistics
- Menu-based interface
- Automatic support for additional cats
- Weight forecasts
- Exporting reports
