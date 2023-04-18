SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NOT NULL AND A.DATETIME >= B.DATETIME
ORDER BY A.DATETIME