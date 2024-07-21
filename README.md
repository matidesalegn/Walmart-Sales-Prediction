# Sales Prediction for Clothing Categories at Walmart

## Overview

This project aims to predict sales for different clothing categories (Women, Men, and Other) at Walmart using historical sales data and various external factors such as weather, macroeconomic indicators, and holidays/events. The prediction model is developed using Facebook's Prophet.

## Libraries and Tools

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning utilities and metrics.
- **Prophet**: For time series forecasting.
- **Jupyter Notebook**: For interactive development and visualization.

## Data Sources

1. **Historical Sales Data**: Contains sales figures for different clothing categories over time.
2. **Weather Data**: Provides daily weather information.
3. **Macroeconomic Data**: Includes economic indicators such as GDP, unemployment rates, etc.
4. **Holiday/Event Data**: Lists holidays and special events that might affect sales.
5. **Submission Data**: Template for submitting predictions.

## Project Workflow

1. **Data Loading**: 
    - Load datasets using `pandas`.

2. **Data Cleaning and Preprocessing**: 
    - Handle missing values.
    - Format dates.
    - Normalize and standardize data.

3. **Data Integration**: 
    - Merge datasets to create a comprehensive dataset.

4. **Feature Selection**: 
    - Identify features with high correlation to sales for each clothing category.

5. **Data Preparation for Modeling**: 
    - Create dataframes with 'ds' (date) and 'y' (sales) columns.
    - Incorporate selected features.

6. **Model Training and Forecasting**: 
    - Train Prophet models separately for Women, Men, and Other categories.
    - Incorporate country holidays for better seasonality handling.
    - Generate forecasts using the trained models.

7. **Model Evaluation**: 
    - Evaluate model performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
    - Compare performance across different clothing categories.

8. **Submission and Evaluation on Kaggle**: 
    - Prepare test data similarly to training data.
    - Generate predictions for the test set.
    - Submit predictions on Kaggle platform.
    - Evaluate performance based on Public and Private Scores.

## Results

The model's performance was evaluated based on Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). The results were compared across different clothing categories, and the final predictions were submitted to Kaggle. The evaluation on Kaggle provided both Public and Private Scores, indicating the model's performance on unseen data.

## Conclusion

This project demonstrates the use of time series forecasting techniques, specifically Prophet, to predict sales in different clothing categories at Walmart. The integration of various external factors such as weather and macroeconomic indicators improved the model's accuracy. The results highlight the importance of comprehensive data analysis and feature selection in building robust predictive models.

## Acknowledgements

Special thanks to the contributors of the datasets and the developers of the libraries used in this project. Also, gratitude to the Kaggle community for providing a platform to test and validate predictive models.
