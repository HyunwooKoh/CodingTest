-- 코드를 입력하세요
-- 공간을 2개 이상 등록한 호스트
-- 정보 ID, 이름, HOST ID
-- ORDER BY ID
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE (HOST_ID) IN (SELECT HOST_ID
              FROM PLACES
              GROUP BY HOST_ID
              HAVING COUNT(*) >= 2)
ORDER BY ID