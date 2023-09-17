 ## Sleep Detection using Wrist-Worn Accelerometer Data

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name : [Manikanta Panuganti]()
- [Github](https://github.com/mani-kantap)
- [Linkedin](https://www.linkedin.com/in/manikantap-dev/)
- [Power Point]()
- [Youtube Video]()
    
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
