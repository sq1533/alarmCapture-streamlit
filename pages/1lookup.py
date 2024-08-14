import pandas as pd
import streamlit as st
from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)
#데이터 불러오기
midInfo = pd.read_json('C:\\Users\\USER\\ve_1\\DB\\2midInfo.json',orient="records",dtype={"mid":str,"info":str,"char":str})
midList = midInfo['mid'].tolist()
mid = st.text_input("MID조회(입력 후 Enter)")
if st.button("조회"):
    if mid in midList:
        st.write(midInfo[midInfo['mid']==mid]['info'].values.replace("<br>","  \n"))
        st.write(midInfo[midInfo['mid']==mid]['char'].values.replace("<br>","  \n"))
    else:
        st.write('존재하지 않는 MID입니다.')