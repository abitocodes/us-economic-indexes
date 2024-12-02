U.S. Economic Indexes Visualization

This repository contains a Python script (index.py) that fetches and visualizes key U.S. economic indicators from January 2022 to the most recent available date. The script generates a line graph and a table displaying the following economic indexes:

	•	Federal Funds Rate
	•	Core Personal Consumption Expenditures (PCE) Inflation Rate
	•	Unemployment Rate

Overview

The script performs the following tasks:

	1.	Data Retrieval: Fetches data for the specified economic indicators from the Federal Reserve Economic Data (FRED) database.
	2.	Data Processing: Calculates the year-over-year Core PCE Inflation Rate and merges the data into a single DataFrame.
	3.	Visualization: Creates a line graph showing the trends of the three indicators and a table displaying the most recent 36 data points.
	4.	Display: Shows the graph and table in a single window for easy comparison and analysis.

Data Sources

The data is sourced from the Federal Reserve Economic Data (FRED) using the following series IDs:

	•	Federal Funds Rate: FEDFUNDS
	•	Unemployment Rate: UNRATE
	•	Core PCE Price Index: PCEPILFE

Prerequisites

	•	Python 3.7 or higher
	•	pip (Python package installer)

Usage

Run the script using Python:

python index.py

Output

The script will display a window containing:

	•	Line Graph: Visualizes the trends of the Federal Funds Rate, Core PCE Inflation Rate, and Unemployment Rate from January 2022 onwards.
	•	Data Table: Shows the most recent 36 data points for the three indicators.