import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("📍 진주시 CCTV 지도")

# CSV 불러오기
data = pd.read_csv('volcano_data_2010.csv')

# 평균 위치를 기준으로 지도 중심 설정
map_center = [data['latitude'].mean(), data['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=13)

# 마커 추가
for _, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name'],  # CCTV 이름
        icon=folium.Icon(color='red', icon='camera')
    ).add_to(m)

# Streamlit에서 지도 표시
st_data = st_folium(m, width=700, height=500)
