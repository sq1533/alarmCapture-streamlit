import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from customs.custom import css
#상단 빈칸제거 및 사이드바 제거
st.markdown(css,unsafe_allow_html=True)
#info_DB읽기 및 캐싱
@st.cache_data(ttl=60*60*12)
def data():
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\info_.json',
                        orient='records',
                        dtype={'mid':str,'info':str,'char':str})
    return DF
#실시간 알람 불러오기
A_df = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\Alarm_.json',
                    orient='records',
                    dtype={'Alarm':str,'mid':str,'URL':str})
Alarm_list = A_df['Alarm'].to_list()
mid_list = A_df['mid'].to_list()
#자동 새로고침 코드
count = st_autorefresh(interval=3000,
                        limit=None,
                        key="refresh")
#실시간 알람 불러오기
def H_page():
    #미정의 MID 확인
    TBD = ["미정의 MID"]
    if count:
        A_df = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\Alarm_.json',
                            orient='records',
                            dtype={'Alarm':str,'mid':str,'URL':str})
        Alarm_list = A_df['Alarm'].to_list()
        mid_list = A_df['mid'].to_list()
        st.code(Alarm_list[-1])
        if mid_list[-1] in data()['mid'].values:
            #st.write(f"URL:{A_df['URL'].to_list()[-1]}")
            st.write(data().loc[data()['mid']==mid_list[-1]]['info'].to_list()[0])
            st.write(data().loc[data()['mid']==mid_list[-1]]['char'].to_list()[0])
        else:
            TBD = list(set(TBD.append(mid_list[-1])))
            A_df.loc[A_df['mid']==mid_list[-1],'mid'] = "확인필요"
            A_df.to_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\Alarm_.json',orient='records',force_ascii=False,indent=4)
            A_df = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\Alarm_.json',
                                orient='records',
                                dtype={'Alarm':str,'mid':str,'URL':str})
            Alarm_list = A_df['Alarm'].to_list()
            mid_list = A_df['mid'].to_list()
        st.divider()
    with st.sidebar:
        stock = pd.read_json('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\Stock.json',orient='dict')
        stoKey = st.selectbox("증권사 이용 핫라인",stock["stock"].keys())
        st.write(stock["stock"][stoKey])
        st.write(TBD)

if __name__ == '__main__':
    H_page()