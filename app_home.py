import streamlit as st

def run_app_home():
    
    st.subheader('welcome~~')

    st.text('이앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')

    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측해 줍니다.')

    img_url = 'https://img4.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/201911/27/GlobalAutoNews/20191127180025129cgek.jpg'

    st.image(img_url)