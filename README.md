# 2023년 한이음 ICT 프로젝트
## 프로젝트 개요
###  1. 프로젝트 소개
> 최근 방범용 cctv, 비상벨(안심벨) 등 가로등에 기능을 추가한 스마트 가로등을 통해 범죄 예방에 도움을 주고 있다. 저희는 이면도로에서도 가로등에 대한 접근성이 용이하다는 점을 이용하여 교통사공 취약한 지역의 문제를 해결하고자 하였습니다. 
 방향성이 없는 보차혼용도로와 이면도로에서의 교차로의 경우 4개의 방향에서 교차로에 진입 할 수 있는 문제의 초점을 맞추어, 최근 발전 중인 AI 기술의 CV분야에서 YOLO와 SSD와 같은 객체 탐지 기술과 Object Tracking 기술을 접목하여 새로운 기능을 만들어내는 시스템입니다. 기능으로는 먼저 교차로에 진입하는 물체를 탐지 한 후, 진행 방향을 파악하여 도로를 이용하는 모든 사용자에게 시각 정보를 제공하여 사고를 대비할 수 있도록 하는 시스템을 만들고자 하였습니다.

### 2. 개발 배경 및 필요성

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/101693311/262010836-903ea5f3-6261-4749-a93e-b7c1ddc84f0b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTgzODYsIm5iZiI6MTY5MjYxODA4NiwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDEwODM2LTkwM2VhNWYzLTYyNjEtNDc0OS1hOTNlLWI3YzFkZGM4NGYwYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTQxMjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NGQzZWZkYTE2MzFmNzczNTc3NGVjZGVhODNmNGEwZTFlYjJmMjZhZjZlMzMyNWJmMTE4MTAyMzQ1ZmZmNmIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.2C1UD3BhVK5tAyRMJ0fXVbHtmd61dOB4JbcSepQvGXU">
</p>

  > 현재 교차로에서의 교통 사고율 다른 도로 유형에서의 사고 전체를 합한 것에 버금가는 수치를 나타내고 있습니다. 큰 교차로에서의 사고와, 비보호 좌회전 등 여러 교통사고가 있지만, 이면도로로 이루어진 주택가나 상권 지역에서도 발생하고 있습니다.

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/101693311/262010863-f037f7b0-ffb0-41a1-9e3f-5528257a9616.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTgzODYsIm5iZiI6MTY5MjYxODA4NiwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDEwODYzLWYwMzdmN2IwLWZmYjAtNDFhMS05ZTNmLTU1MjgyNTdhOTYxNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTQxMjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mOTNmNDRiMGUyODE3NmUxM2U1NGJmMTk1MmYwZDUwMWEzNWM3YTVjYWY4M2M0Y2NmMDU1OWU5NTcxMDg4NzM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.QLP3Z9MgCYmGNwrbzPA0V0F5V_repBeNiVi1sFWcXmA">
</p>

> 실제로 국토 교통부가 국가 보행교통 실태조사를 진행한 결과 차도와 보도의 구분이 없는 보차혼용도로가 차도와 보도가 분리된 도로보다 교통사고가 50% 더 발생한다고 하였다. 저희는 이러한 자료를 바탕으로 보차혼용도로의 유형 중 교차로가 가장 안전의 취약하다고 판단하였습니다.
 그에 대한 원인으로 교차로에서의 시각 부하량을 원인으로 잡았습니다. 운전자는 운전에 필요한 정보의 90%를 시각에 의존하지만, 교차로에 진입하는 상황에서는 조심해야하는 부분이 더 증가하여 도시 고속도로에 비해 약 10배 이상의 시각적 부하가 발생한다는 연구 결과가 있다. 최근에는 불법주정차, 적재물, 환경적인 문제로 인해 운전자의 시점에서 좌, 우에서 접근하는 차량을 파악하기 어려운 상황이다. 또한 최근 자동차 보유 수 증가로 야기되는 불법 주정차 차량 증가로 더욱 시야 확보가 어려운 상황입니다.

> 시야 제한을 야기하는 대표적인 원인으로 불법주정차의 문제를 해결하면 교통사고율이 낮아질 수 있다. 최근 각 도시의 주차 문제를 해결하기 위해 공용 주차 구역을 설치하는 정책을 시행 중에 있는데 2025년까지 증축 계획이며, 많은 시간과 비용이 든다.
 그렇기 때문에 저희는 새로운 기능을 제공하는 스마트 가로등과 같이 이러한 문제를 해결하기 위해 카메라를 접목하여 진입하는 차량, 사람, 퍼스널 모빌리티를 감지하고, 이동방향 및 위치를 파악하여 이를 불빛이나, 소리 등을 통해 정보를 제공하여 시각적 부하를 줄이고, 사고의 취약한 부분에 운전자가 집중할 수 있도록 제공하고자 하였습니다. 이러한 기능을 제공받는 운전자는 다른 방향에서 진입하는 것을 확인하여 속도를 줄여서 교차로의 진입하거나, 정지하여 차량이 지나가도록 양보하는 행동을 야기함으로써 교차로에서의 교통사고를 줄일 수 있는 시스템을 설계하고자 하였습니다.

### 3. 프로젝트 특징 및 장점
> 기존의 교차로에서 사고를 예방하기 위해 반사 거울을 설치하거나 불법 주정차를 단속하여 시야를 확보할 수 있도록 하였습니다. 하지만, 반사거울에 경우 특정 각도가 아닌이상 확인 어려울 수 있으며, 밤에는 거울을 통해 다가오는 물체를 확인하기 어렵다는 문제점이 있고, 최근에는 거울앞에도 주정차를 하며 거울을 찾을 수도 없는 문제점이 있습니다.
 또한 세대 당 보유 차량수가 증가하면서, 빌라나 주택가, 상권은 주차공간을 확보하기 어려워 불법주정차를 하는 차량이 늘어나고 있으며, 이를 모두 단속하여 벌금을 부과하기에는 애매한 상황이 야기되었습니다.
 이를 해결하는 방법으로, 주차 공간을 마련하는 방안을 전국적으로 실행 중에 있지만, 설치 비용이 크다는 점과 공사기간이 길다는 점, 주차공간이 확보되어도 거리 때문에 불법주정차가 해결되지 않을 수도 있다는 점이 발목을 잡고있습니다. 
 하지만 저희 시스템상 교차로를 바라볼 수 있는 위치인 건물 외벽이나, 교차로 중앙으로 뻗어있는 가로등(보안등)에 설치하며, 카메라의 각도 정보와 조금의 데이터셋을 확보하게 된다면 바로 설치가 가능하며, 주차장 설치 비용보다 훨씬 적은 비용으로 교통사고 문제의 해결점을 제공할 수 있습니다.

### 4. 프로젝트 구성도
  * HW 구성도    
    > - GPU가 탑재된 Jetson nano 보드와 Arduino 보드를 통해 기능을 구현하였으며, 외관은 3D프린터를 통해 제작하였습니다.
    <p align="center">
      <img src="https://private-user-images.githubusercontent.com/101693311/262010882-8a1dda16-9779-43a9-88ed-0cfd35107b1d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTgzODYsIm5iZiI6MTY5MjYxODA4NiwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDEwODgyLThhMWRkYTE2LTk3NzktNDNhOS04OGVkLTBjZmQzNTEwN2IxZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTQxMjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MWFhMGNjYmQ0MzFjNTQ2MDllNGE3NDU5ZmI1NzVmYWM0NmVlOGMyOTYzMTJhN2M2M2M4YWYxNTcwNjEwYzAzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.2ZL3pO9hksrbUZSw7ShlE3f7_N05YRzDbyHRNh4JhnE">
    </p>

  * SW 구성도
    > - 데이터 수집, 학습 과정, 객체 탐지 및 추적 
   <p align="center">
     <img src="https://private-user-images.githubusercontent.com/101693311/262014633-2e2758b5-5dd8-4bd8-9765-e73a0f2282d6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTkwMjYsIm5iZiI6MTY5MjYxODcyNiwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE0NjMzLTJlMjc1OGI1LTVkZDgtNGJkOC05NzY1LWU3M2EwZjIyODJkNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTUyMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MjYwMjc3NjMyMDA3MGM4NjZiNzRiNTYxOWVjM2Q3NTY2M2JlMDYyNjM1ZjhiNzAzMWJmYTRhMjc0Y2Y0YzQ2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.-vGkOyJM6Ryk2TLCcyzIBIj6a4X4KnIs7gCsf1F1cnk">
   </p>  

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/101693311/262014821-d5e4cc02-d5e0-4496-b2a5-86b3f5268696.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTkwMzMsIm5iZiI6MTY5MjYxODczMywicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE0ODIxLWQ1ZTRjYzAyLWQ1ZTAtNDQ5Ni1iMmE1LTg2YjNmNTI2ODY5Ni5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTUyMTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZDUzMmUzYTMyZDhkYTFkNGE5NGU5MmY0NWZiMTRhNzNlODk3ZGFmOWE0N2RkMTIwNzU2YTY4YmM3MTFlN2UwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.RQKONmADEfLSS9rGQMOAualeqGuMXngc5bF7KCbhycg">
</p>
    
  * 서비스 흐름도
<p align="center">
<img src="https://private-user-images.githubusercontent.com/101693311/262014838-0c7fb924-b542-464a-8a0a-3c3fadd20f17.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTkwMzMsIm5iZiI6MTY5MjYxODczMywicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE0ODM4LTBjN2ZiOTI0LWI1NDItNDY0YS04YTBhLTNjM2ZhZGQyMGYxNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTUyMTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MWI0NGNjYzdhMzdlZTZhNDE4NzVmZGQ0MDE3NTE5MTIwZDQxOTFiZWJhMTQyNTIzOWEyZDBhNDE0YjZjMWI5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Ps9SVKZoG-BPzwKlGqZzcvNEpwqg4HGCA_WAevS4hKM">
</p>

> - 기본적인 원리는 카메라를 통해 받은 이미지를 연산 처리하여 객체를 검출합니다. 물체가 탐지되지 않았을 경우 초기상태로 돌아가며, 물체가 탐지되었을 경우에는 객체 추적 기술을 통해 방향과, 위치 정보를 받아와 신호를 전달해야하는 특정 상황에 도달하면 아두이노에 신호를 전달합니다. 전달 된 신호를 처리하여 객체가 검출된 방향에 맞게 진입하는 양측 도로에서 확인할 수 있도록 LED가 점등되어 시각 정보를 제공합니다.

* 3D 렌더링 사진
<p align="center">
<img src="https://private-user-images.githubusercontent.com/101693311/262016104-4ee7397c-b52d-40c8-9223-3bb2363e4823.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTkzNjksIm5iZiI6MTY5MjYxOTA2OSwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE2MTA0LTRlZTczOTdjLWI1MmQtNDBjOC05MjIzLTNiYjIzNjNlNDgyMy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTU3NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MWQwZTM1OTM3NDFkZTE5YzVmZDAwODk4ZjBkMTdlNjhjZmNlN2NiYWYxYjI3MmRiMDIzOGJlYTljMzlhNDVhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.kNYePoptj0TBrQWsTyqpHSWte7o_0zBPxjENCgmwOrM">
</p>

<p align="center">
<img src="https://private-user-images.githubusercontent.com/101693311/262016110-aa2ff0d5-3957-4429-963c-e8adb562c036.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTkzNzEsIm5iZiI6MTY5MjYxOTA3MSwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE2MTEwLWFhMmZmMGQ1LTM5NTctNDQyOS05NjNjLWU4YWRiNTYyYzAzNi5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMTU3NTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OTM2Njc0MjE2MGZlMDBiNDljODc1NTE1M2E3ZmZjZmEzYWY2Zjg2ZDhhMDU0YmM2ODM1ZWVlNTgwYTE2Njg5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.5yorOqJReq03JeFEL7gEf2UHGiHAlbT38mNoWjKhzmU">
</p>

