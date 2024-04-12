# Mumbai-Businesses-Case-Study
This repository contains code which mainly focused on data cleaning and data processing.
Please refer following URL of Observable HQ Notebook for this case study - https://observablehq.com/d/f4e6d8242b9dabfe
# Business Case Study - Mapping and Analysis of Businesses in Mumbai City

## Technology Used

- Python
- JavaScript
- ObservableHQ
- d3.js

## Description

The main goal was to identify all businesses in the city, categorize them by industry type, and display each industry type on a frequency graph. Additionally, users can select an industry type, and all corresponding businesses will be shown on a city map.

For this case study, I focused on Mumbai city and utilized Python for data cleaning and processing.

I also implemented the K-means clustering algorithm to showcase ideal locations for each respective industry on a separate city map.

Overall, the case study aims to provide insights into the distribution of businesses in Mumbai city and visualize them in an interactive and informative manner.

## Steps Followed

### Data Collection

- Obtained dataset containing information on registered businesses in Mumbai.

### Data Cleaning and Preprocessing

- Eliminated irrelevant or duplicate entries to ensure data accuracy.
- Standardized business types and their counts for uniform analysis.

### Analysis and Visualization

#### Frequency Chart

- Generated a frequency chart depicting the distribution of various business types in Mumbai.
- Implemented JavaScript and d3.js within ObservableHQ Notebook to create an interactive frequency graph.

#### Geographical Mapping

- Plotted business locations on a map using latitude and longitude coordinates obtained from the dataset.
- Utilized Google Maps API and GeoJSON format for mapping.
- Leveraged ObservableHQ's mapping capabilities, including D3.js and Leaflet.js, for visualizing business distributions across the city.

#### Identifying Ideal Locations

- Employed the K-means clustering algorithm to identify ideal locations for different types of businesses.
- Clustered businesses based on their types to pinpoint suitable areas for specific industries.

### Conclusion and Recommendations

- Summarized key findings from the analysis, including insights into the distribution of businesses across Mumbai.
- Provided recommendations based on identified ideal locations for different business types, offering valuable guidance for entrepreneurs and stakeholders interested in starting or expanding businesses in the city.

## Question Can Be Asked

### Concept of K-means Clustering Algorithm

K-means clustering is a way to group similar things together in a dataset.

1. Start by randomly placing K points called centroids in the dataset.
2. Assign each data point to the closest centroid.
3. Move each centroid to the average position of its assigned points.
4. Repeat steps 2 and 3 until the centroids stop moving much.
5. Each data point now belongs to the cluster with the nearest centroid, and you've got your clusters.

### Data Source, Data Cleaning, and Processing

Data cleaning and processing is the process of preparing raw data for analysis by identifying and correcting errors, inconsistencies, and missing values. This involves tasks like removing duplicates, handling missing data, standardizing formats, and transforming variables to make the data suitable for analysis. The goal is to ensure that the data is accurate, consistent, and ready for meaningful analysis.

---

This README file provides an overview of the business case study, detailing the technology used, steps followed, and concepts relevant to the analysis. It aims to serve as a comprehensive guide to the project and its methodologies.

