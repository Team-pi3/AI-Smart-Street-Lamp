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

### 5. 기대효과 및 활용분야 
> 기존의 불법주정차차량 등으로 시야확보가 되지 않는 운전자가 좁은 도로를 운전하는 경우 사고 위험이 있다. 특히나 사거리와 같은 평면교차로의 부도로인 경우 사고 위험률은 더 높다.
평면교차로 중 차도와 보도의 구분이 없는 이면도로나 무표지유형의 경우, 우선도로와 양보도로를 구분하지 않고 모든 방향에 황색점멸이나 양보, 서행 표지를 설치하거나 아예 표지 설치를 생략하는 경우로 별다른 통제 없이 운전자끼리 알아서 양보하여 교차로를 통행하는 체계이다. 다른 교통이 없을 경우 모든 방향에서 정지 의무가 없지만, 통행량이 급증할 경우 통행우선권이 불분명해 무질서해지기 쉽다. 또한, 좁은 골목길에서 ”정지차량”, “역주행차량”은 들어오는 차량의 시야를 방해하고, 교통사고 및 교통 혼잡을 유발하는 주요 요인이다.

<p align="center">
<img src="https://private-user-images.githubusercontent.com/101693311/262016875-c6b9a777-6267-4f02-a628-7937d536817c.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTk1ODUsIm5iZiI6MTY5MjYxOTI4NSwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE2ODc1LWM2YjlhNzc3LTYyNjctNGYwMi1hNjI4LTc5MzdkNTM2ODE3Yy5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMjAxMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNmQxMGRlMzU2YmY2NmMxNzNhZjNhN2NkZmY0ZmIxYmY3MzhlZjJhMjk1NzIyNTQwZTE4YTg1NmMzN2QyMzg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.qHa2UPxMNcejJLvEQc2XwzoLhwMV1_VLNbFnr9DDxoA">
</p>

> LED 조명을 이용해 야간 시 보행자와 차량 운전자에게 주의를 줘 교통 사고를 예방하는데 큰 도움을 주었다고 한다. 서울 성동구에서는 스마트횡단보도 설치 후 구의 교통 사고 발생률이 21.5% 감소하는 효과가 있었다. 전남 광주시는 교통 사고율을 줄이기 위해 지역 내 22개 구역에 스마트 횡단보도를 구축한다는 계획을 밝혔다.
현재 서울시는 시민이 더욱 안전하고 쾌적한 삶을 영위할 수 있도록  주요 장소에 가로등에 여러 기능을 추가한 “스마트폴”을 설치하고 있다. 

<p align="center">
<img src="https://private-user-images.githubusercontent.com/101693311/262016879-51a1e93a-9bcc-4c96-ad75-265646641a38.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTI2MTk1ODUsIm5iZiI6MTY5MjYxOTI4NSwicGF0aCI6Ii8xMDE2OTMzMTEvMjYyMDE2ODc5LTUxYTFlOTNhLTliY2MtNGM5Ni1hZDc1LTI2NTY0NjY0MWEzOC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDgyMVQxMjAxMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZDk2YmU2ZmVmNTBlYTJlNmZlZWZkMDk0MGE5NzIwOTY5YTVmNmE1MzgxMTkwZWI2OTFlMjU4YjFkZmZhYTFiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.wQu3HOXI3cOp2x-Siy05nS6TEIJ1XiVHnRA40JDch3g">
</p>

> 또한 2020년 은평구에서 5곳에 AI 보행자 교통사고 방지 시스템을 도입한 것을 시작으로 현재 인천시에서도 우회전 가로등이 설치되어있는 것을 보아 가로등에 기능을 추가하여 안전한 환경을 구축하려는 정항이 많이 보이고 있다.
스마트 가로등은 불법주정차를 단속하는 방법이 아닌, 불법주정차로 인해 시야 확보가 되지 않는 차량이 안전하게 이동할 수 있도록 신호를 주는 시스템이다. 불법주정차를 단속하는 것과 운전 차량에 신호를 주는 방식은 불법주정차를 장려하는 것이 아니냐는 의견이 나올 수 있다. 하지만 스마트 가로등은 기본적으로 불법 주정차로 인한 피해를 막고, 단속보다는 계도를 통한 원활한 교통 흐름을 만드는 것이 목적이다. 따라서 이런 순기능은 많은 지자체가 함께 참여할 때 가능하기 떄문에 지자체의 적극적인 제휴가 필요하다.

> 스마트 가로등의 요구기능 및 개발방향은 영상처리 기반 도로 차량 검지, 객체 구분의 정확성 및 효율적인 학습 알고리즘, 학습 데이터 활용 및 지속적인 성능 고도화 기능 등을 통해 차량 운전자의 시야를 보완해주는 것
보행자와 운전자에게 신호를 줄 수 있는 제품이 있다면, 보행자와 운전자 모두에게 더욱 안전하고 편안한 이동환경을 제공해 줄 수 있을 것이며, 교통 혼잡과 교통사고의 감소로 인해 지자체 차원에서도 좋은 결과일 것이다.
> 
> 일전에 문제 분석을 통해 좁은 골목 교차로 사고에서 우리가 집중한 원인은 신호의 부재와 주정차 차량이나 건물로 인한 시야각 감소였다. 그래서 우리가 생각한 해결법은 미리 시야를 확보한 후 신호를 주는 것이다.  교차로에 가로등을 설치하고 암을 중앙에 뻗고 그 끝에 4방향의 카메라를 설치해 교차로의 모든 방향을 확인할 수 있도록 한다.  그리고 4방향에 모두 디스플레이나 LED등의 시각적인 정보를 전달할 수 있는 장치를 설치한다, 만약 카메라에 교차로에 진입하려는 차량이 인식되면 진입하려는 차량의 수직 방향이 되는 2개의 도로에 어느 방향에서 지금 차량이 접근하고 있는지 시각적인 신호를 통해 알려준다.

> 이런 식으로 상단에 설치된 카메라를 통해 운전자의 시야각을 보완하고 마라 정보를 제공해 사고를 예방하는 방법이다. 이를 통해 보행자와 운전자에게 보다 안전한 교통상황을 제공할 수 있으며, 지자체 차원에서는 교통사고율 감소의 효과를 낳을 수 있다. 
 국가의 교통 정보체계가 소통정보에서 안전정보로 변화하고, 주행하는 차의 원활한 통행을 방해할 수 있는 좁은 골목길의 도로 장애물(불법 주정차, 역주행차량)을 정확하게 검지하는 기술은 현재는 물론 미래 자율주행차의 교통 환경에서도 반드시 필요한 핵심기술이다.
또한 국내에서도 오래전부터 돌발 상황검지를 위한 기술 개발을 진행해왔으며, 지난‘18년 국가 공인인증제도’가 수립되면서, 도로 장애물 감지 기술 적용에 대한 관심과 필요성이 대두되고 있다.
도로 장애물 차량 검지는 “도로 안전”과 밀접하게 관련된 것으로 현재 및 미래도로 환경에 필요한 기술이며, ”실시간성“이 필수이다. 현재의 기술은 검지 범위 및 실시간성에 대한 제약이 존재하기 때문에 이를 극복할 수 있는 기술을 ‘스마트 가로등’ 프로젝트를 통해 개발하였다.

> 마지막으로 정보 제공측면이다. 현재 네비게이션의 길찾기 기능을 사용하면 길의 혼잡도를 색깔로 알려주는 기능이 있는데, 이는 골목길이나 좁은 길에대한 데이터를 수집하기 어려워 위치를 기반으로 그 지점에 사용자가 몇이나 있는지를 측정한 후에 색깔로 표시하는게 최선일 것이다. 저희 시스템을 통해 각 도로의 차량의 수나 상황에 대한 정보를 이용하여 혼잡도를 표시하는데 이용할 뿐 아니라, 응급 출동 시 진입이 불가능한 도로에 대해서 미리 파악하고 갈 수 있는 효과를 얻을 수 있을 것이다. 
