# Airbnb-Property-Listing

> A project to predict the price of an Airbnb listing from tabular, text and image data

## Data Preparation

 - Loaded in and cleaned tabular data, both numerical and text into a useable format
 - Filled in missing data with sensible values and dropped any data that can't be imputed
 - Processed image data, such that every image is in RGB format and has the same image height, with the aspect ratio of the image being maintained

 **Original**                                              | **Processed**
----------------------------------------------------------|-------------------------------------------------------
<img src="./imgs/0a26e526-1adf-4a2a-888d-a05f7f0a2f33-a_original.png" />  |<img src="./imgs/0a26e526-1adf-4a2a-888d-a05f7f0a2f33-a_processed.png" />

## Regression Modelling

 - Created a regression model to predict the price of an AirBnB listing using only the numerical tabular data, which includes:
    - Number of guests
    - Number of beds
    - Number of bathrooms
    - Number of bedrooms
    - Number of amenities
    - Ratings out of 5 for:
        - Cleanliness
        - Accuracy (How accurate the description of the property is)
        - Communication (Rating for the host's communication with the customer)
        - Location (The rating for the location of the property)
        - Check-in (The rating for the check-in process given by the host)
        - Value (Rating of value given by the host)
- Tuned the parameters of a Linear Ridge Regression model and a Random Forest Regression model
- Used RMS as the evaluation metric
- Improved upon the score of the linear model with the Random Forest model, however it is still overfitting
