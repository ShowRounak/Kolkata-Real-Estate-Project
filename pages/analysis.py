import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config('Analysis Page')

st.title('Analytics')

new_df = pd.read_csv('data/data_viz1.csv')
grp_df = new_df.groupby('Location')[['price','PRICE_PER_UNIT_AREA','AREA','Latitude','Longitude']].mean()


fig = px.scatter_mapbox(grp_df, lat="Latitude", lon="Longitude", color="PRICE_PER_UNIT_AREA", size='AREA',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map", width=1200, height=700, hover_name=grp_df.index)

st.plotly_chart(fig,use_container_width=True)

st.header('Area vs Price')
fig1 = px.scatter(new_df, x="AREA", y="price", color="BEDROOM_NUM")
st.plotly_chart(fig1,use_container_width=True)

st.header('Bedroom Pie Chart')
city_zones = new_df['CITY'].unique().tolist()
city_zones.insert(0, 'overall')
selected_zone = st.selectbox('Select Zone', city_zones)
if selected_zone == 'overall':
    fig2 = px.pie(new_df, names='BEDROOM_NUM')
    st.plotly_chart(fig2,use_container_width=True)
else:
    fig3 = px.pie(new_df[new_df['CITY'] == selected_zone], names='BEDROOM_NUM')
    st.plotly_chart(fig3,use_container_width=True)


st.header('Price DistPlot')
hist_data = [new_df[new_df['PROPERTY_TYPE'] == 'Residential Apartment']['price'], new_df[new_df['PROPERTY_TYPE'] == 'Independent House/Villa']['price']]

group_labels = ['Residential Apartment', 'Independent House/Villa']

# Create distplot with custom bin_size
fig4 = ff.create_distplot(hist_data, group_labels, bin_size=.2)
st.plotly_chart(fig4,use_container_width=True)