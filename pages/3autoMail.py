import pandas as pd
import subprocess
import requests
import json
import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp
from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)
#네비게이터 버튼
row_ = row(3, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("home")
if row_.button("조회", use_container_width=True):
    sp("lookup")
if row_.button("DB관리", use_container_width=True):
    sp("DBM")
#메일 DB저장
def sendMail():
    requests.post("http://127.0.0.1:8000/email",json.dumps(email))
#인증번호 입력
if st.button(label="쿠칩 메일전송 시작"):
    subprocess.run(["python", "C:\\Users\\USER\\ve_1\\alarmCapture\\worksMail.py"])
bady1 = row(3, vertical_align="center")
bady2 = row([2,1], vertical_align="center")
passN : str = bady1.text_input("인증번호", max_chars=4)
bady1.empty()
bady1.empty()
adr : str = bady2.text_input("수신자")
if bady2.checkbox("참조"):
    subadr : str = "618356@naver.com"
else:
    subadr : str = ""
title : str = st.text_input("제목")
select = st.selectbox("메일 내용 선택",("교환당","발행당"))
if select == "교환당":
    main = "교환당입니다."
elif select == "발행당":
    main = "발행당입니다."
else:
    main = ""
email = {
    "passnumber":passN,
    "addr":adr,
    "subaddr":subadr,
    "title":title,
    "main":main
    }
if st.button(label="전송"):
    sendMail()
    st.markdown("메일 전송 완료")