import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Streamlit app title
st.title('Diamond Price Prediction')

# Collect input data from the user
carat = st.number_input('Carat')
depth = st.number_input('Depth')
table = st.number_input('Table')
x = st.number_input('X dimension')
y = st.number_input('Y dimension')
z = st.number_input('Z dimension')
cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2'])

# Prediction button
if st.button('Predict'):
    # Create CustomData instance
    data = CustomData(
        carat=carat,
        depth=depth,
        table=table,
        x=x,
        y=y,
        z=z,
        cut=cut,
        color=color,
        clarity=clarity
    )
    
    # Convert input data to dataframe
    pred_df = data.get_data_as_dataframe()
    
    # Predict using the pipeline
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(pred_df)
    
    # Display the result
    st.write(f'The predicted price of the diamond is: ${round(pred[0], 2)}')

# streamlit run app.py
