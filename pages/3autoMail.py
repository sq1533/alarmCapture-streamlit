import time
from datetime import datetime
import pandas as pd
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
#메일 구분
tab1,tab2 = st.tabs(["영문메일 전송","쿠칩메일 전송"])
with tab1:
    #인증번호 입력
    if st.button(label="영문메일 전송"):
        pd.DataFrame([{"be":"end"},{"be":"start"}],index=[0]).to_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\start.json',orient='records',force_ascii=False,indent=4)
    #영문메일 자료 가져오기
    enMail = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\enMail.json',orient='records')
    servise = list(enMail["서비스"].dropna().keys())
    bank_servise = ["선택"]+list(enMail["원천사"]["은행"].keys())
    pg_servise = ["선택"]+list(enMail["원천사"]["PG원천사"].keys())
    #메일 정보 입력
    bady1 = row(3, vertical_align="center")
    st.text("수신자")
    bady2 = row([1,1,1,2], vertical_align="center")
    bady3 = row([2,1,1], vertical_align="center")
    bady4 = row([1,1], vertical_align="center")
    bady5 = row([1,1], vertical_align="center")
    #인증번호
    passN : str = bady1.text_input("pg_info 인증번호", max_chars=4)
    bady1.empty()
    bady1.empty()
    #메일 수신자 선택
    if bady2.checkbox("간편 송금"):adr1 : str = enMail["수신자"]["간편송금"]
    else:adr1 : str = ""
    if bady2.checkbox("내통장결제"):adr2 : str = enMail["수신자"]["내통장결제"]
    else:adr2 : str = ""
    if bady2.checkbox("PG"):adr3 : str = enMail["수신자"]["PG"]
    else:adr3 : str = ""
    adr : str = adr1+" "+adr2+" "+adr3
    if bady2.checkbox("참조(해외영업팀)"):subadr : str = "t_291ts@hecto.co.kr, mnt@hecto.co.kr"
    else:subadr : str = ""
    S = []
    O = ""
    #서비스, 원천사 선택
    serv_select = bady3.multiselect("서비스",servise)
    for i in serv_select:
        S.append(enMail["서비스"][i])
    S = " | ".join(S)
    bank_select = bady3.selectbox("은행선택",(bank_servise))
    pg_select = bady3.selectbox("PG선택", (pg_servise))
    if bank_select == "선택":bank_select = ""
    else:
        O = enMail["원천사"]["은행"][bank_select]
    if pg_select == "선택":pg_select = ""
    else:
        O = enMail["원천사"]["PG원천사"][pg_select]
    DAY = str(bady4.date_input("시작 시간",(datetime.now()),format="MM-DD-YYYY"))
    bady4.empty()
    TIME = str(bady5.text_input("장애 시작 시간", (datetime.now().strftime("%H:%M")),label_visibility="hidden"))
    bady5.empty()
    MtoS = str(datetime.strptime(DAY,'%Y-%m-%d').strftime("%A"))
    T = DAY+"("+MtoS+")"+" "+TIME
    title = "[{s}] {o} Error Recovery Notice ({t})".format(s=S,o=O,t=T)
    main = """
Dear valued customers.
Thank you for using Hecto Financial's {s} service.
We are sending you an emergency notice as an error has occurred. Please refer below for the details.

--------------------------------------------------------------------------------------------------------------
- Name of Institution   : {o}
- Impacted Service      : {s}
- Date & Time of Error : {t}
- Details                   : {Service not available}
--------------------------------------------------------------------------------------------------------------

We will send you an update as soon as the recovery is complete.
Thank you.


Please note that this email is for outgoing only, and inquiries via reply will not be processed.
Please contact below for inquiries.
Hecto Financial | www.hectofinancial.co.kr
9~10F, 6, Teheran-ro 34-gil, Gangnam-gu, Seoul, Republic of KoreaㆍCustomer Service : 1688-5130ㆍFAX : 02-588-2724\nCopyrightⓒ Hecto Financial Co., Ltd. All Rights Reserved.
""".format(s=S,o=O,t=T)
    email = {
        "passnumber":passN,
        "addr":adr,
        "subaddr":subadr,
        "title":title,
        "main":main
        }
with tab2:
    #인증번호 입력
    if st.button(label="쿠칩메일 전송"):
        pd.DataFrame([{"be":"start"},{"be":"end"}],index=[0]).to_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\start.json',orient='records',force_ascii=False,indent=4)
    coochip = pd.read_json("C:\\Users\\USER\\ve_1\\alarmCapture\\db\\mailText.json",orient='index',dtype={"선입금":str,"후입금":str,"IP미등록":str})
    bady1 = row(3, vertical_align="center")
    bady2 = row([2,1], vertical_align="center")
    passN : str = bady1.text_input("pg_info2 인증번호", max_chars=4)
    bady1.empty()
    bady1.empty()
    adr : str = bady2.text_input("수신자")
    if bady2.checkbox("참조"):
        subadr : str = "couchip@hecto.co.kr"
    else:
        subadr : str = ""
    title : str = st.text_input("제목")
    select = st.selectbox("메일 내용 선택",("선입금","후입금","IP미등록"))
    if select == "선입금":
        main = coochip[0]["선입금"]
    elif select == "후입금":
        main = coochip[0]["후입금"]
    elif select == "IP미등록":
        main = coochip[0]["IP미등록"]
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
        with st.spinner('Wait for it...'):
            time.sleep(3)
        st.success('메일전송 완료')