import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Add and resize an image to the top of the app
img_fuel = Image.open("../img/fuel_efficiency.png")
st.image(img_fuel, width=700)

st.markdown("<h1 style='text-align: center; color: black;'>Fuel Efficiency</h1>", unsafe_allow_html=True)

# Import train dataset to DataFrame
train_df = pd.read_csv("../nb/dat/train_df.csv.gz", compression="gzip")
model_results_df = pd.read_csv("../nb/dat/model_results.csv")

# Create sidebar for user selection
with st.sidebar:
    # Add FB logo
    st.image("https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" )    

    # Available models for selection

    # YOUR CODE GOES HERE!
    models = ["DNN", "TPOT: ExtraTreesRegressor"]

    # Add model select boxes
    model1_select = st.selectbox(
        "Choose Model 1:",
        (models)
    )
    
    # Remove selected model 1 from model list
    # App refreshes with every selection change.
    # models.remove(model1_select)
    
    model2_select = st.selectbox(
        "Choose Model 2:",
        (models)
    )

# Create tabs for separation of tasks
tab1, tab2, tab3 = st.tabs(["🗃 Data", "🔎 Model Results", "🤓 Model Explainability"])

with tab1:    
    # Data Section Header
    st.header("Raw Data")

    # Display first 100 samples of the dateframe
    st.dataframe(train_df.head(100))

    st.header("Correlations")

    # Heatmap
    corr = train_df.corr()
    fig = px.imshow(corr)
    st.write(fig)

with tab2:    
    
    # YOUR CODE GOES HERE!
    cols = ['mse','mae','r2']

    # Data Section Header
    st.header("Model Results")

    # Display your performance metrics
    st.dataframe(model_results_df)

    # Columns for side-by-side model comparison
    col1, col2 = st.columns(2)

    # Build the confusion matrix for the first model.
    with col1:
        st.header(model1_select)

        # YOUR CODE GOES HERE!
        model1_results = model_results_df[model_results_df["model"] == model1_select][cols]

        fig1 = px.imshow(model1_results, text_auto=True)
        
        # add custom x-axis title
        fig1.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.00005,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom y-axis title
        fig1.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.25,
                                y=0.5,
                                showarrow=False,
                                text="True value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))


        # Write plotly chart and fit to the container width.
        st.plotly_chart(fig1, use_container_width=True)



    # Build confusion matrix for second model
    with col2:
        st.header(model2_select)

        # YOUR CODE GOES HERE!
        model2_results = model_results_df[model_results_df["model"] == model2_select][cols]

        fig2 = px.imshow(model2_results, text_auto=True)

        # add custom x-axis title
        fig2.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.00005,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom y-axis title
        fig2.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.25,
                                y=0.5,
                                showarrow=False,
                                text="True value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))


        # Write plotly chart and fit to the container width.
        st.plotly_chart(fig2, use_container_width=True)



with tab3: 
    # YOUR CODE GOES HERE!
        # Use columns to separate visualizations for models
        # Include plots for local and global explanability!
     
    st.header(model1_select)
    img_dnn_shap = Image.open('./dat/dnn_shap.png')
    st.image(img_dnn_shap, width=1000)
    
    st.header(model2_select)
    img_tpot_shap = Image.open('./dat/dnn_shap.png')
    st.image(img_tpot_shap, width=1000)
