# reverse geocoding fastapi

위도와 경도를 행정동 주소로 바꿔주는 역지오코딩 api 서버 입니다.

# 실행방법

[[Python] 좌표를 행정동 주소로 바꾸기](https://k1a2.github.io/posts/backend-geocoding/) 
게시글에서 만든 shp 파일을 data 폴더 안에 넣어주면 바로 사용이 가능합니다.

# 사용법

## /map/reverse-geocode

### query

* lat: 위도 좌표
  * 예) 37.553979
* lon: 경도 좌표
  * 예) 126.922668
* type: 가져올 행정동 주소 레벨
  * 0: 읍면동 까지 ex) 서울특별시 마포구 서교동
  * 1: 시군구 까지 ex) 서울특별시 마포구
  * 2: 시도 까지 ex) 서울특별시
* near: 어떠한 위치에도 포함되지 않을 때, 가장 가까운 행정동으로 리턴할지 여부