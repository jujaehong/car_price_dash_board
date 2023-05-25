import streamlit as st

def run_app_home():
    
    st.subheader('welcome~~')

    st.text('이앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')

    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측해 줍니다.')

    img_url = 'https://cdn.autoherald.co.kr/news/photo/201911/36589_61216_852.jpg'

    st.image(img_url)