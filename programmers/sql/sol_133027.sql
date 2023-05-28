-- 코드를 입력하세요
-- 7월 아이스크립 + 상반기의 아이스크림 총 주문량
-- 합 상위 3개 LIMIT 3
-- GROUP BY 맛
SELECT J.FLAVOR
FROM JULY J LEFT JOIN FIRST_HALF H ON J.FLAVOR = H.FLAVOR
GROUP BY J.FLAVOR
ORDER BY SUM(J.TOTAL_ORDER + H.TOTAL_ORDER) DESC
LIMIT 3