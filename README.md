# Airbnb-Property-Listing

> A project to predict the price and category of an Airbnb listing from tabular and text data

## Data Preparation

 - Loaded in and cleaned tabular data, both numerical and text into a useable format
 - Filled in missing data with sensible values and dropped any data that can't be imputed

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

## Classification Modelling

 - Used the same numeric features as above to create a classification model to predict the category of each listing, which was one of:
    - Amazing Pools
    - Beachfront
    - Chalets
    - Offbeat
    - Treehouses
 - Improved upon a baseline Logistic Regression model by tuning a Random Forest Classifier
 - Used Tf-Idf for feature engineering the text description column and fitted a baseline Logistic Regression model
 - Vastly improved performance compared to the numerical data
 - Used the `optuna` library to perform hyper-parameter tuning on the pipeline fitted with a Random Forest Classifier

 ## Feed-forward neural network

 - Used the same regression problem as before to train a 2-layer feed-forward neural network in PyTorch
 - Made sure to scale the inputs and outputs to avoid a exploding gradient problem
 - Visualised the RMS Error on the training and validation set
 - Evaluating the test set with the final trained model
