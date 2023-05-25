import streamlit as st
import numpy as np
import joblib

def run_app_ml() :
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을
    # 유저한테 입력받는다.

    gender = st.radio('성별 선택', ['남자', '여자'])
    if gender == '남자' :
        gender = 0
    else :
        gender = 1


    age = st.number_input('나이 입력', 18 , 100) # 최소 18세 , 최대 100세
    salary = st.number_input('연봉 입력', 5000, 1000000) # 최소 5000달러, 최대 1000000달러
    dedt = st.number_input('카드빚', 0, 1000000) # 최소 0달러 , 최대 1000000달러
    worth = st.number_input('자산', 1000, 10000000) # 최소 1000달러, 최대 10000000달러

    # 버튼을 누르면 예측한 금액을 표시한다.
    if st.button('금액 예측') : 
        new_data = np.array([gender, age, salary, dedt, worth])
        new_data = new_data.reshape(1,5)
        regressor = joblib.load('model/regressor.pkl') # joblib(주피터 노트북에서 잡립라이브러리로 저장한 인공지능 regressor.pkl 파일 가져오기)
        y_pred = regressor.predict(new_data) # 예측
        print(y_pred)

        
        #달러짜리 차량 구매 가능합니다.
        
        print(round(y_pred[0]))
        
        price = round(y_pred[0])

        print(str(price)+ '달러짜리 차량 구매 가능합니다.')
        print(f'{price}달러짜리 차량 구매 가능합니다.')
        print('.{}달러짜리 차량 구매 가능합니다.'.format(price))

        st.text(f'{price}달러짜리 차량 구매 가능합니다.')
