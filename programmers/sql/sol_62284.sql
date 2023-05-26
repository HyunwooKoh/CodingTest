-- 코드를 입력하세요
-- 우유와 요거트가 담긴 카트 -> 서브쿼리로 둘 중 하나가 있는 카트 찾기
-- 출력 : 장바구니 ID
-- ORDER BY ID
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk'
AND CART_ID IN (SELECT CART_ID
               FROM CART_PRODUCTS
               WHERE NAME = 'Yogurt')
ORDER BY CART_ID