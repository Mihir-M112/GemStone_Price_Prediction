# GemStone_Price_Prediction
<div id="introduction" style="color: magenta; font-weight: bold; font-size: 40px; font-family: 'Times New Roman';">INTRODUCTION</div>


<p> This dataset contains the prices of gemstones {Diamonds} (Regression Analysis). The dataset contains 10 independent variables (including <b> id </b>):

1. **`id`** :  unique identifier of each diamond
2. **`carat weight`**: Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
3. **`cut`**: The quality of the cut of the gemstones/diamonds.
4. **`color`**: The color of the gemstones/diamonds.
5. **`clarity`**: Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
6. **`depth`**: The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface).
7. **`table`**: A diamond's table is the facet which can be seen when the stone is viewed face up.
8. **`X`**: The length of the gemstones/diamonds. X is the length of the diamond as measured along the girdle.
9. **`Y`**: The width of the gemstones/diamonds. Y is the width of the diamond as measured along the girdle.
10. **`Z`**: The symmetry of the gemstones/diamonds. Z is the height of the diamond from the culet to the table.

<div style="color: White; font-weight: bold; font-style: italic; font-size: 25px;">
  Target variable:
</div>

**`Price`**: Price of the given Diamond.

The goal of this project is to predict the price of a gemstone based on independent variables.

Dataset Source Link : [GemStone Dataset](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

df.head()
![image](https://github.com/user-attachments/assets/4b62e2b5-beb0-48a2-bf78-59b14bc472ce)

### Model Selection:

CatBoost Regressor (97.8% Accuracy)

## **Approach for the project**

- **Data Ingestion** :

In Data Ingestion phase the data is read as csv.
Then the data is split into training and testing and saved as csv file.

- **Data Transformation** :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then One Hot encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file namely preprocessor.pkl.

- **Model Training** :

In this phase base model is tested . The best model found was CatBoost Regressor with 97.8% accuracy.
The model is selected on based on R2 Score Evaluation Metric. The highest R2 Score model selected.

- **Prediction Pipeline** :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

- **Web Work**:
  The entire project is shown by using HTML, CSS & FAST API for Web Work.

### How to use this project? 

1. Download the whole project in you system or you can also clone it.
2. Make a virtual environment uisng the command:  
    `python -m venv venv`
3. Activate the virtual environments:  
    `.\venv\Scripts\activate`
4. Run the requirements.txt file in venv:  
    `pip install -r requirements.txt`
5. Run the below command:   
    `uvicorn app.main:app --reload`


![image](https://github.com/user-attachments/assets/f234008f-69e1-4882-bff4-7f222c31d9db)
