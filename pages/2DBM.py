import requests
import json

import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)
#데이터 불러오기
with open('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json','r',encoding="UTF-8") as f:
    DF = json.load(f)

url = "http://127.0.0.1:8000/mk_info"
url_d = "http://127.0.0.1:8000/mk_info_d"
def create():
    requests.post(url,json.dumps(mk_info))
def change():
    requests.put(url,json.dumps(mk_ch))
def delete():
    requests.post(url_d,json.dumps(mk_d))

#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill'
row_ = row(3, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("home")
if row_.button("조회", use_container_width=True):
    sp("lookup")
if row_.button("쿠칩 메일", use_container_width=True):
    sp("autoMail")

tab1,tab2,tab3 = st.tabs(["생성","수정","삭제"])

with tab1:
    with st.form(key="mk_info"):
        mid: str = st.text_input("mid", max_chars=20)
        info: str = st.text_area("정보")
        char: str = st.text_area("담당자")
        mk_info = {
            "mid":mid,
            "info":info.replace('\n','  \n'),
            "char":char.replace('\n','  \n')
        }
        btn = st.form_submit_button(label="생성")
        look1 = [i for i in range(len(DF)) if DF[i]['mid']==mk_info['mid']]
        if btn:
            if look1 == []:
                create()
                st.markdown("생성완료")
            else:
                st.markdown("MID가 이미 존재합니다.")

with tab2:
    with st.form(key="mk"):
        mid: str = st.text_input("mid", max_chars=20)
        mk = {
            "mid":mid
        }
        btn_1 = st.form_submit_button(label="조회")
        look2 = [i for i in range(len(DF)) if DF[i]['mid']==mk['mid']]
        if btn_1:
            if look2 == []:
                st.markdown("MID가 존재하지 않습니다.")
    with st.form(key="mk_ch"):
        if look2 != []:
            pass
        else:
            look2 = [0]
        mid: str = st.text_input("mid",DF[look2[0]]['mid'].replace("  \n","\n"),max_chars=20)
        info: str = st.text_area("정보",DF[look2[0]]['info'].replace("  \n","\n"),height=250)
        char: str = st.text_area("담당자",DF[look2[0]]['char'].replace("  \n","\n"),height=100)
        mk_ch = {
            "mid":mid,
            "info":info.replace('\n','  \n'),
            "char":char.replace('\n','  \n')
        }
        btn_2 = st.form_submit_button(label="수정")
        if btn_2:
            change()
            st.markdown("수정완료")
with tab3:
    with st.form(key="mk_d"):
        mid: str = st.text_input("mid", max_chars=20)
        mk_d = {
            "mid":mid
        }
        btn = st.form_submit_button(label="삭제")
        look3 = [i for i in range(len(DF)) if DF[i]['mid']==mk_d['mid']]
        if btn:
            if look3 == []:
                st.markdown("MID가 존재하지 않습니다.")
            else:
                delete()
                st.markdown("삭제완료")