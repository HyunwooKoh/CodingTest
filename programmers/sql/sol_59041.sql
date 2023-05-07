-- 코드를 입력하세요
-- 이름이 2개 이상 -> count에 대해 groupBy, Having
-- 이름이 빈 경우는 제외
-- 이름순으로 정렬 order by

SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT >= 2
ORDER BY NAME