import streamlit as st
import pandas as pd

st.title("CSV 파일 컬럼명 확인")

# CSV 절대 경로 (윈도우용, 꼭 r붙이기!)
csv_path = r"C:\Users\dyddn\OneDrive\바탕 화면\volcano_data_2010.csv"

# CSV 불러오기
data = pd.read_csv(csv_path)

# 컬럼명 리스트 화면에 출력하기
st.write("CSV 컬럼명:", data.columns.tolist())

