-- 완료된 중고 거래 금액이 70만원 이상 HAVING TOTAL_SALES >= 7000000
-- 회원 ID, 닉네임, 총거래금액
-- 총 거래금액 기준 오름차순 ORDER BY TOTAL_SALES
SELECT UGB.WRITER_ID, UGU.NICKNAME, SUM(UGB.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD UGB INNER JOIN USED_GOODS_USER UGU ON UGB.WRITER_ID = UGU.USER_ID
WHERE UGB.STATUS = 'DONE'
GROUP BY UGB.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES