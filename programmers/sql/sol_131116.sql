-- 코드를 입력하세요
-- 분류, 가격, 아름
-- '과자', '국' ,'김치', '식용유' 인 경우만 포함 WHERE
-- 식품 분류 별로 가격이 제일 비싼 것
-- 가격을 기준으로 DESC

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT CATEGORY, MAX(PRICE) AS PRICE 
              FROM FOOD_PRODUCT 
              WHERE CATEGORY = '과자' OR CATEGORY = '국' OR CATEGORY = '김치' OR CATEGORY = '식용유'
              GROUP BY CATEGORY)
ORDER BY PRICE DESC