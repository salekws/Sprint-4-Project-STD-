#read in required libraries
import streamlit as st
import pandas as pd
import plotly.express as px


#read in CSV file
vehicles_df = pd.read_csv('vehicles_us.csv')

#header text
st.header('Secondhand Vehicle Market')

#Description of the purpose of the page
st.write("Analysis on the differences between 4wd and 2wd vehicles.") 

#Fills missing values in 'is_4wd' column with '2wd' and converts entire column to string type
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna('2wd').astype('str')

#Replaces values of 1 (assuming 1 = vehicle is 4wd) with '4wd'
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].replace(['1.0'], '4wd')

#Scatterplot of model year vs price for each vehicle type
fig = px.scatter(vehicles_df, x="price", y="model_year", color="is_4wd")
fig.update_layout(xaxis_title="Price", yaxis_title="Model Year")
st.plotly_chart(fig, use_container_width=True)
st.write("There are more 4wd vehicles among modern vehicles than older models.") 
st.write("Here we look at the price and amount of each drivetrain vehicle type.")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
#create checkbox
cbox_4wd = st.checkbox('Display of 4wd vehicles', value=True)

#checkbox logic
if cbox_4wd:
    pc_df = vehicles_df.loc[vehicles_df['is_4wd'] == '4wd']  
elif not cbox_4wd:
    pc_df = vehicles_df

#histogram settings    
fig = px.histogram(pc_df, title='Number of vehicles with specific drivetrain vs. Price', x='price', color='is_4wd', nbins=50, barmode='overlay')
fig.update_layout(xaxis_title="Price", yaxis_title="Number of Vehicles", yaxis_range=[0,5000], xaxis_range=[0,100000])
# showing the histogram of drivetrain vs price
st.plotly_chart(fig, use_container_width=True)

#comment on above histogram
st.write("We can clearly say that 2wd vehicles are larger in number and cheaper in comparison with 4wd vehicles.") 
