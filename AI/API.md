### API

#### Interface

Interface : 서로 다른 두 개의 시스템 (기기, 소프트웨어 등)이 정보를 교환할 때, 그 사이에 존재하는 접점. 사용자가 기기를 쉽게 동작 시키거나, 기계와 기계가 통신할 때 필요한 '약속된 방식'.
    
    예시 : 
    키보드, 마우스, 모니터 : 컴퓨터와 사람 사이의 물리적 인터페이스
    TV 리모콘 : TV와 사람 사이의 인터페이스
    자동차 운전대, 페달 : 자동차의 내부 장치와 운전자 사이를 연결
    스마트폰 터치 스크린 : 디지털 인터페이스

UI (User Interface) : 사람(사용자)이 소프트웨어에 접근하는 그래픽적, 화면적 요소

    예시 : 
    ATM의 언어 선택 화면
    브라우저의 뒤로 가기 버튼
    스마트폰 앱의 아이콘 등

-> 눈에 보이지 않을 뿐 (UI가 없을 뿐), 기계와 기계, 시스템과 시스템 사이에도 수많은 '인터페이스'를 통해 정보를 주고받고 있음.

#### 클라이언트와 서버
클라이언트 (Client) : 서비스를 요청하는 쪽. (사용자의 웹 브라우저, 모바일 앱)

서버 (Server) : 요청을 받아서 처리하고, 결과를 응답해주는 쪽. (웹 서버, 데이터베이스 서버)

예시) 사용자가 브라우저로 특정 주소(URL)를 요청 -> 서버가 해당 페이지, 데이터 등을 보내줌

#### API 활용

API (Application Programming Interface) : 두 소프트웨어(또는 시스템)가 서로 통신할 수 있게 하는 메커니즘. '약속된 방식의 인터페이스'. 특정 규칙에 따라 데이터를 요청하고 응답하는 규칙을 제공.

Application : 특정 기능을 수행하는 모든 소프트웨어. 웹, 모바일, 데스크탑 앱 등, 우리가 만든 서비스나 프로그램도 모두 앱의 일종.

    예시 1) ChatGPT에 구글 로그인 시
    1. ChatGPT가 Google API에 어떤 사람이 Google로 "내 사이트에 회원가입하려고 하는데 어떤 사용자인지 정보를 줘"
    2. Google API가 ChatGPT에게 "이 사용자는 내 사이트에 올바르게 로그인 했고, 확인해보니 ~~한 정보를 가진 사용자야"

    - Google 로그인 계정으로 로그인을 성공했을 경우 Google API는 ChatGPT에게 로그인에 성공한 인증된 사용자 정보를 넘겨줌.
    - 사용자 정보를 넘겨받은 ChatGPT는 해당 정보를 활용해 회원가입 및 로그인을 진행.


#### API Key

API Key : API에게 요청을 보내는 애플리케이션을 구별하기 위한 고유한 식별 문자열.

API Key가 필요한 이유 : 
- 보안 강화 : 무단 접근을 막고, 승인된 사용자 (또는 앱)만 요청할 수 있도록
- 데이터 관리 : API 호출 횟수, 사용량 모니터링. 일정량 이상의 사용 시 제안 또는 과금 정책 적용 가능

API Key 사용 시 주의사항 :
- 공개된 곳에 노출하지 말 것
- 키가 유출될 경우 무단 사용 위험 > 정기 갱신 필요
- 서버-클라이언트 구조에서 키를 안전하게 저장하는 방법들 고려


