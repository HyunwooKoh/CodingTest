-- 코드를 입력하세요
-- 입양을 갔음 - FROM OUTS
-- 보호기간이 가장 긴 2개 = ORDER BY 입양일 - 보호 시작일 LIMIT 2
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC
LIMIT 2