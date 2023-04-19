-- 자동차 종류가 '세단' 또는 'SUV'
-- 2022년 11월 1일 부터 2022년 11월 30일까지 대여 가능
-- 30일간의 금액이 50이상 200만원 미만
--  자동차 ID, 자동차 종류, 대여 금액(FEE) 
--  대여 금액 기준으로 내림차순, 같은 경우 종류로 오름차순
--  모두 같은 경우 ID를 기준으로 내림차선

SELECT CAR.CAR_ID, CAR.CAR_TYPE, ROUND(CAR.DAILY_FEE * 30 * (1 - (PLAN.DISCOUNT_RATE / 100))) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CAR INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN PLAN ON CAR.CAR_TYPE = PLAN.CAR_TYPE
WHERE CAR.CAR_ID NOT IN (SELECT CAR_ID
                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        WHERE (CAR_ID, END_DATE) IN (SELECT CAR_ID, MAX(END_DATE)
                                                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                    GROUP BY CAR_ID)
                            AND START_DATE <= date('2022-11-30')
                            AND END_DATE >= date('2022-11-01'))
    AND CAR.CAR_TYPE IN ('세단', 'SUV')
    AND PLAN.DURATION_TYPE = '30일 이상'
HAVING FEE BETWEEN 500000 AND 1999999    
ORDER BY FEE DESC, CAR.CAR_TYPE, CAR.CAR_ID DESC 