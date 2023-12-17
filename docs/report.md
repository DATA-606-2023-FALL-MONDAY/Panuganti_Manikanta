 # Sleep Detection using Wrist-Worn Accelerometer Data

## 1. Title and Author
- **Sleep Detection using Wrist-Worn Accelerometer Data**
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name : [Manikanta Panuganti]()
- [Github](https://github.com/mani-kantap)
- [Linkedin](https://www.linkedin.com/in/manikantap-dev/)
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

Sleep is undeniably crucial for both physical and mental well-being. It plays a fundamental role in maintaining overall health, impacting various facets of human life, including cognitive function, mood regulation, behavior, and emotional well-being. However, despite its paramount importance, conducting comprehensive and precise sleep research has been a persistent challenge. Polysomnography (PSG) stands as the gold standard for sleep measurement, providing highly accurate data. However, PSG is not without its drawbacks, as it is an expensive and time-consuming method, making it impractical for large-scale studies and routine monitoring.In contrast, wrist-worn accelerometers present a more accessible and cost-effective means of measuring sleep patterns. Nevertheless, the analysis of accelerometer data poses its own set of challenges, including the need for robust and accurate algorithms to extract meaningful sleep-related information.

The goal of this project is to develop a model to detect sleep onset and wake using wrist-worn accelerometer data. This will enable researchers to conduct more reliable, larger-scale sleep studies across a range of populations and contexts.


## 3. Data 

The data for this project was provided by the [Healthy Brain Network](https://healthybrainnetwork.org/). The data consists of wrist-worn accelerometer data which includes the following features:

- Data sources: https://healthybrainnetwork.org/, https://www.kaggle.com/competitions/child-mind-institute-detect-sleep-states/data
- Data size : 220 MB
- Data shape: 13165560 rows, 6 cols
- Each row is a continuous series recording of accelerometer data for a single subject spanning many days.

  
| Column Name | Data Type | Definition | Potential Values |
|-------------|-----------|------------|------------------------------------------------------------------------|
| series_id   | string    | Unique identifier for each accelerometer series. | 08db4255286f|
| step        | integer   | An integer timestep for each observation within a series. | 1|
| timestamp   | datetime  | A corresponding datetime with ISO 8601 format `%Y-%m-%dT%H:%M:%S%z`. |2018-11-05T10:00:05-0400 |
| anglez      | float     | As calculated and described by the GGIR package, z-angle is a metric derived from individual accelerometer components that is commonly used in sleep detection and refers to the angle of the arm relative to the vertical axis of the body. |-34.181801	 |
| enmo        | float     | As calculated and described by the GGIR package, ENMO is the Euclidean Norm Minus One of all accelerometer signals, with negative values rounded to zero. While no standard measure of acceleration exists in this space, this is one of the several commonly computed features. | 0.0443	|
| awake       | integer   | State of the sleep | 0 (awake) or 1 (asleep) |


- Target Label: Awake
- features/predictors: anglez, enmo

  ## 4. Exploratory Data Analysis (EDA)

The Exploratory Data Analysis is performed using Google Colab with a primary goal of understanding the data, summarizing key statistics, creating visualizations, identifying potential data cleansing requirements, and ensuring the resulting dataset is tidy.

1. Summary Statistics
   
Summary statistics provide a snapshot of the central tendency, dispersion, and shape of the distribution of each variable. This information is crucial for understanding the range and characteristics of the data.

ADD picture of summary statistics

2. Visualizations using Plotly Express
   
Visualizations are powerful tools for understanding the distribution and relationships within the data. Plotly Express is a Python library for creating interactive visualizations easily.

In this section, I have created histograms with box plots using Plotly Express. These visualizations help us understand the distribution of 'anglez' and 'enmo' for different sleep states.

ADD PLOTS and GRAPHS

3. Missing Values and Duplicate Rows
   
Checking for missing values and duplicate rows is essential to ensure data quality and cleanliness.

4. Data Transformation
   
Data transformation involves preparing the data for analysis, including tasks like splitting, merging, pivoting, or melting.


The EDA emphasizes the readiness of the dataset for machine learning modeling and the dataset is tidy and ready to apply various models now.

## 5. Model Training 

### Models for Predictive Analytics
The following models have been chosen for predictive analytics:
* Logistic Regression
* Gaussian Naive Bayes
* Random Forest
* XG Boost

### Training Methodology
Train vs Test Split
The dataset will be split into training and testing sets to assess the model's performance on unseen data. I have used the common practice 80/20 split, where 80% of the data is used for training, and the remaining 20% is used for testing. Each selected model will be trained on the training dataset.

Python Packages and Development Environment
The model training will be implemented on Google Colab using popular Python packages, primarily scikit-learn for machine learning algorithms.

### Performance Evaluation
Metrics
To measure and compare the performance of the models, relevant metrics will be used. Common metrics for binary classification problems include accuracy, precision, recall, F1-score, and the area under the ROC curve (AUC-ROC).

Model Comparison
The models' performance will be compared based on the selected metrics. The model with the highest accuracy, precision, recall, or other relevant metric, depending on the business context, will be considered the most suitable for the task.

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease to learn)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.
