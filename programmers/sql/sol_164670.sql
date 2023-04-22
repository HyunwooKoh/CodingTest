-- 코드를 입력하세요
-- 중고거래 게시물 3건 이상
-- 사용자 ID, 닉네임, 전체 주소, 전화번호
-- 주소 : 시,도로명주소,상세주소가 함께 출력
-- 전화번호 : 010-12s3-123 하이폰
-- 회원 ID를 기준으로 내림차순 ORDER BY USER_ID DESC

SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소, CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO,4,4), '-', SUBSTR(TLNO,8,4)) AS 전화번호
FROM USED_GOODS_USER
WHERE (USER_ID) IN (SELECT WRITER_ID
                   FROM USED_GOODS_BOARD
                   GROUP BY WRITER_ID
                   HAVING COUNT(*) >= 3)
ORDER BY USER_ID DESC