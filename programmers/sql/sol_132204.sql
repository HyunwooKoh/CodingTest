-- 코드를 입력하세요
-- 2022년 4월 13일 -> 예약 날짜
-- 취소되지 않은 CS 진료 예약 내역
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- ORDER BY 진료예약일시
SELECT  A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A inner JOIN PATIENT P ON A.PT_NO = P.PT_NO inner JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.APNT_CNCL_YN = 'N'
AND DATE_FORMAT(A.APNT_YMD, "%Y-%m-%d") = "2022-04-13"
ORDER BY A.APNT_YMD