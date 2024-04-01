## FindDot

카메라 캘리브레이션 및 왜곡 보정 기능

카메라는 아이폰 11 pro를 사용

실행 화면

<img width="400" alt="before_calibration" src="https://github.com/SoTaeHo/FindDot/assets/91146046/20e08b5b-7f3c-4e35-bcc3-f85fd7a940cb">
<img width="400" alt="find_dot" src="https://github.com/SoTaeHo/FindDot/assets/91146046/d04dda9f-7990-438b-83ab-d78962302204">

카메라 캘리브레이션 결과

<img width="700" alt="calibration_result" src="https://github.com/SoTaeHo/FindDot/assets/91146046/5b31b3d0-d00e-48f6-a8b4-200bc7485e1c">

RMSE : 0.725
fx : 1107 / fy : 1107 / cx : 373 / cy : 628
근사치로 적었으면 자세한 수치는 첨부한 이미지를 확인

<img width="400" alt="before_distortion_correction" src="https://github.com/SoTaeHo/FindDot/assets/91146046/1ff76632-add5-4f7c-ad60-4b44668b7104">
<img width="400" alt="after_distortion_correction" src="https://github.com/SoTaeHo/FindDot/assets/91146046/51fc718c-731f-47b7-91ad-c375eb053f99">

아이폰 카메라의 특성 상 왜곡이 거의 없는 상태로 찍혀, 오히려 왜곡 보정을 한 이후 검은색 여백이 출력됨.
