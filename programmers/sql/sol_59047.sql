-- 코드를 입력하세요
-- lower함수로 이름 소문자화
-- 개인지 확인
-- like로 문자열 비교
-- order by NAME

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE "%el%" AND
    ANIMAL_TYPE = "Dog"
ORDER BY NAME