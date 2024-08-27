# Predicting laptop price regression project

## Sources
**Python version:** 3.11.9<br/>
**Imported packages:** pandas, numpy, matplotlib, seaborn, sklearn, xgboost<br/>
**Dataset:** https://www.kaggle.com/datasets/muhammetvarl/laptop-price

## Data cleaning
After loading the data I checked duplicated observations and the missing (or incorrect) values for each feature.<br/>
The dataset was ready for EDA without any modifications.

## Feature engineering
* Log transformation of the target feature
* New feature introduced as *PixelsPerInch* from *ScreenResolution*
* Binary features created from screen types of *ScreenResolution*
* Define and merge new categories for *CPUCategory* and *OpSysCategory*
* Create different features for handling *Memory* categories as SSD, HDD, Flash Storage and Hybrid
* Dummy feature transformation for categorical features

## Exploratory Data Analysis
Since the target feature has a right-skewed distribution I applied a log transformation.
![Alt text](https://github.com/horvathadam07/laptop-price/blob/main/img/price.PNG "Price")
![Alt text](https://github.com/horvathadam07/laptop-price/blob/main/img/log_price.PNG "Log of Price")

I prepared barplots for categorical features and histograms for numerical features to show insights about the distributions and then remove some outliers based on the group frequencies of Memory-type features.
![Alt text](https://github.com/horvathadam07/laptop-price/blob/main/img/memoryssd.PNG "Memory SSD")
![Alt text](https://github.com/horvathadam07/laptop-price/blob/main/img/weight.PNG "Weight")

## Model Building
At first I splitted the data into train and test samples with a 30% test part.<br/>
I fitted four different models and evaluated them by R2-Score to reach the best goodness of fit measurement.

The same cross validation (k=5) was used for all tree-based models to find the best hyperparameters using GridSearchCV.

## Model Performances
The XGBoost algorithm performed significantly better than the others in the test sample, the R2-Score values can be seen below:

  * **Linear regression:** 0.7654<br/>
  * **Decision tree:** 0.7422<br/>
  * **Random forest:** 0.8312<br/>
  * **XGBoost:** 0.8606
