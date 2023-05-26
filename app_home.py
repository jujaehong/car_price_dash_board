import streamlit as st

def run_app_home():
    
    st.subheader('환영합니다.')
    st.text('좋은 서비스로 제공하겠습니다.')
    st.text('자동 배포 처리된 앱입니다.')

    st.text('이앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')

    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측해 줍니다.')

    img_url = 'https://cdn.autoherald.co.kr/news/photo/201911/36589_61216_852.jpg'

    st.image(img_url)