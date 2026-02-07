import streamlit as st

st.title('인터랙티브 앱')
number = st.slider('숫자 선택', 0, 100, 50)
st.write(f'선택한 숫자: {number}')
