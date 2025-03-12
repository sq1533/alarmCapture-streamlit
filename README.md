# alarmCapture
streamlit, fast API, selenium, bueatifulSoup, Pandas

## 구성
* customs/
  * custom.py
* pages/
  * 1lookup.py
  * 2DBM.py
  * 3autoMail.py
* database.py
* home.py
* main.py
* worksAlarm.py
* worksMail.py

## 목적
팀원 간 업무의 정보 불균형 해소를 위한 실시간 알람 데이터 수집 및 mid정보 매칭 / 통합 화면 노출

## 기대효과
* 신규 이슈의 실시간 피드백
* 매뉴얼 정보의 빠른 접근
* mid 정보 아카이브 생성

## 기능
* selenium 웹 크롤링을 통한 신규 알람 텍스트 파일 수집
* 알람 id 정제 및 midInfo.json 파일 mid와 매칭
* streamlit 웹 서비스 구축 및 수집 알람 텍스트 노출
* 매칭된 id의 정보 노출
