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

**- Summary Statistics**
   
Summary statistics provide a snapshot of the central tendency, dispersion, and shape of the distribution of each variable. This information is crucial for understanding the range and characteristics of the data.

ADD picture of summary statistics

**- Visualizations using Plotly Express**
   
Visualizations are powerful tools for understanding the distribution and relationships within the data. Plotly Express is a Python library for creating interactive visualizations easily.

In this section, I have created histograms with box plots using Plotly Express. These visualizations help us understand the distribution of 'anglez' and 'enmo' for different sleep states.

ADD PLOTS and GRAPHS

**- Missing Values and Duplicate Rows**
   
Checking for missing values and duplicate rows is essential to ensure data quality and cleanliness.

**- Data Transformation**
   
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
- Train vs Test Split

The dataset will be split into training and testing sets to assess the model's performance on unseen data. I have used the common practice 80/20 split, where 80% of the data is used for training, and the remaining 20% is used for testing. Each selected model will be trained on the training dataset.

- Python Packages and Development Environment

The model training will be implemented on Google Colab using popular Python packages, primarily scikit-learn for machine learning algorithms.

### Performance Evaluation
- Metrics
  
To measure and compare the performance of the models, relevant metrics will be used. Common metrics for binary classification problems include accuracy, precision, recall, F1-score, and the area under the ROC curve (AUC-ROC).

- Model Comparison
  
The models' performance will be compared based on the selected metrics. The model with the highest accuracy, precision, recall, or other relevant metric, depending on the business context, will be considered the most suitable for the task.

## 6. Application of the Trained Models

The web app is designed to allow users to interact with the trained models, providing a seamless and intuitive experience for making predictions based on input data.

**Technology Stack**

The web application is built using Streamlit, a Python library that enables the creation of interactive web applications with minimal code. Streamlit is chosen for its simplicity and ease of integration with machine learning models.

**User Interface Design**

The user interface is designed to be user-friendly and intuitive. Users will be able to input relevant data through a simple form or interface, and the web app will provide predictions using the trained models. The design aims to make the application accessible to users with varying levels of technical expertise.

**Integration with Trained Models**

The trained predictive analytics models, including Logistic Regression, Gaussian Naive Bayes, Random Forest, and XG Boost, are seamlessly integrated into the web app. Streamlit provides a straightforward way to load the models and make predictions based on user inputs.

**Deployment**

The web app has been deployed on a platform using cloud services of AWS. The deployment process ensures that the application is accessible to users over the internet. The choice of deployment platform has made based on factors such as scalability, ease of use, and cost considerations.

**User Interaction with Trained Models**
- Input and Prediction
  
Users interact with the web app by providing input data through a user-friendly interface. The trained models process this input and generate predictions based on the underlying algorithms. The predicted outcomes are then presented to the user within the web app.
- Feedback Mechanism
  
To enhance user experience and provide transparency, the web app can include a feedback mechanism. Users may have the option to provide feedback on the predictions, which can be valuable for model improvement and refinement.

## 7. Conclusion

This project serves as a foundation for advancing the application of machine learning in sleep tracking and opens doors for further research to address existing challenges and uncover new insights into sleep analytics. Model training showcased the effectiveness of machine learning algorithms, with XG Boost achieving the highest accuracy of 97%. The development of the Streamlit web app extends the practical utility of these models to end-users, allowing them to make predictions based on their input data in a user-friendly environment.

The potential applications of this work are broad, ranging from personal sleep tracking applications to healthcare and wellness solutions. Individuals can benefit from personalized insights into their sleep patterns, while healthcare professionals may use the models for sleep disorder diagnostics and treatment planning.

### Limitations of the Work
Despite the promising results, there are certain limitations to this work. The accuracy achieved by the models may not generalize well to diverse datasets, and the performance may be sensitive to variations in data quality. Additionally, the models may not account for individual variations and complexities in sleep patterns, requiring further refinement for broader applicability.

### Future Research Directions
Future research can build upon this work by addressing its limitations and exploring additional avenues. Refinement of the models to handle diverse datasets and individual variations in sleep patterns is crucial. Integration of real-time data sources, such as wearable devices or continuous monitoring systems, can enhance the models' accuracy and applicability. Additionally, incorporating user feedback into the model training process can contribute to ongoing model improvement.

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.
