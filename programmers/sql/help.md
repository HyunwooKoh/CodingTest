# 숫자 함수
절대값 ABS
SELECT -10, ABS(-10) "-10 절대값" FROM DUAL;


소수점 n자리 버리기 FLOOR
SELECT 34.5678, FLOOR(34.5678)
FROM DUAL;


반올림 ROUND
SELECT 34.5678, ROUND(34.5678)
FROM DUAL;


지정 자리수 자르기 TRUNC
TRUNC 는 반올림X, 그냥 잘라냄O.
SELECT TRUNC(12.3456, 2), TRUNC(12.3456, -1), TRUNC(12.3456) FROM DUAL;


나머지 리턴 MOD
MOD 함수는 나누기 연산을 한 후에 구한 몫이 아닌 나머지를 결과로 되돌려주는 함수
SELECT MOD(27,2)"27%2 값", MOD(27,5)"27%5 값", MOD(27,7)"27%7 값" FROM DUAL;


-- 1. 사번(EMPNO)이 홀수인 사람들을 검색
SELECT * FROM EMP WHERE MOD(EMPNO,2) = 1;


# 문자 처리 함수
대소문자 변환 UPPER LOWER
SELECT 'Welcome to Oracle' "입력된 문자열", UPPER('Welcome to Oracle') "문자열UPPER" FROM DUAL;
SELECT 'Welcome to Oracle' "입력된 문자열", LOWER('Welcome to Oracle') "문자열LOWER" FROM DUAL;

-- 2. 다음과 같이 쿼리문을 구성하면 과연 직급이 'manager'인 사원을 검색하시오.
SELECT '그냥찾음',EMPNO, ENAME, JOB FROM EMP WHERE JOB = 'manager'; 
-- 출력 없음

SELECT EMPNO, ENAME, JOB FROM EMP WHERE UPPER(JOB) = UPPER('Manager');
-- 속성과 데이터 모두 같은 대소문으로 맞춤.
실무시 데이터의 대소문자 여부를 판단하기 힘듦.

찾는 데이터의 대소문 형식을 설정 후 실행할 것.


이니셜만 대문자 변환 INITCAP
SELECT 'wElCoMe tO oRaCLe' "입력된 문자열" , INITCAP('wElCoMe tO oRaCLe')"문자열INITCAP" FROM DUAL;


문자열 길이 LENGTH 바이트 LENGTHB
SELECT LENGTH('Oracle'), LENGTH('오라클') FROM DUAL;
-- 영문을 2바이트 한글은 1바이트로 인식함.


문자열 일부 추출 SUBSTR
SELECT SUBSTR('Welcom to Oracle', 4, 3) FROM DUAL; -- com
-- 4번째 문자부터 3개만 출력
SELECT SUBSTR('Welcom to Oracle', -4, 3) FROM DUAL; -- acl
-- 역행 4번째 문자부터 순행 3개 출력
[순행]
[역행]

-- 날짜데이터 월 일 단위로 출력하기.
SELECT SUBSTR(HIREDATE, 1,2) 년도,
		SUBSTR(HIREDATE, 4,2) 달 FROM EMP;


바이트 수 기준 일부 추출 SUBSTB
-- SUBSTRB 문자가 메모리에 저장되는 바이트 수를 계산함.
SELECT SUBSTR('웰컴투오라클',3,4) , SUBSTRB('웰컴투오라클', 3,4) FROM DUAL;
SELECT SUBSTR('Welcome to Oracle',3,4), SUBSTRB('Welcome to Oracle', 3,4) FROM DUAL;
SUBSTB 한글 문자열 3바이트부터 4바이트 후 위치까지 출력

한글은 한 글자를 2바이트로 인식함.
SUBSTB 영어 문자열 3바이트부터 4바이트 후 위치까지 출력

영문자는 한 글자를 1바이트로 인식함.

특정문자 위치 리턴 INSTR
SELECT INSERT('문자열', '문자', '시작위치', '찾은 문자들 중 위치')
: 문자열 N번째 시작위치에서문자를 찾기 시작해 찾은 문자들 중 위치가 n번째의 위치값 출력

--INSTR 함수는 대상 문자열이나 칼럼에서 특정 문자가 나타나는 위치
SELECT INSTR('WELCOME TO ORACLE', 'O') "O의 위치" FROM DUAL;
SELECT INSTR('WELCOME TO ORACLE', 'O', 6, 2) "6번째 이후 2번째 'O'" FROM DUAL;
문자열 순서는 1부터 카운팅 함.

문자열에서 6번째 뒤에 오는 'O' 중에서 순서가 2번인 'O'의 문자열 위치 출력


바이트 수 기준 문자위치 리턴 INSTRB
SELECT	INSTR('데이터베이스', '이', 3, 1),
		INSTRB('데이터베이스', '이', 3, 1) 
FROM DUAL;


특정 기호 채우기 LPAD RPAD
-- LPAD : LEFT PADDING - 왼쪽 여백(테두리 사이의 여백) 
SELECT LPAD('Oracle',20,'#') FROM DUAL;
SELECT RPAD('Oracle',20,'#') FROM DUAL;


문자열 공백, 특정 문자 제거 TRIM
-- 문자열 공백 제거
SELECT TRIM('                Oracle                ') trim FROM DUAL;
SELECT LTRIM('                Oracle                ') 왼쪽trim FROM DUAL;
SELECT RTRIM('                Oracle                ') 오른쪽trim FROM DUAL;


# 날짜 함수
시스템 날짜 리턴 SYSDATE
-- SYSDATE : SYSTEM DATE - 컴퓨터에 지정된 현재날짜 출력
SELECT SYSDATE FROM DUAL;
SELECT SYSDATE-1 어제날짜, SYSDATE 오늘날짜 , SYSDATE+1 내일날짜 FROM DUAL;


--6. 각 사원들의 현재까지의 근무 일수를 구하기
SELECT (SYSDATE - HIREDATE) 근무일수 FROM EMP;


ROUND 날짜 반올림
--6. 각 사원들의 현재까지의 근무 일수를 구하기
-- 날짜 소수점 반올림
SELECT ROUND(SYSDATE - HIREDATE) 근무일수 FROM EMP;


-- 날짜 단위 기준으로 반올림하기.
-- '월'단위 기준으로 사원 입사일 출력하기.
SELECT HIREDATE "입사일", ROUND(HIREDATE, 'MONTH') "'월'단위 기준 입사일" FROM EMP;
월 단위 기준 이하 반올림

TRUNC 지정 기준 날짜 자르기
TRUNC(날짜,포멧기준)

-- '월'단위 기준으로 이하 지우기
SELECT HIREDATE "입사일" ,TRUNC(HIREDATE, 'MONTH')"'월'단위 기준 입사일" FROM EMP;
월 단위 기준 이하 포멧

날짜 사이 간격 일 수 리턴 MONTHS_BETWEEN
SELECT  ENAME 이름, 
        SYSDATE 오늘,
        HIREDATE 입사일, 
        MONTHS_BETWEEN(SYSDATE, HIREDATE) 근무일수 
FROM EMP;

SELECT  ENAME 이름, 
        SYSDATE 오늘, 
        HIREDATE 입사일, 
        ROUND(MONTHS_BETWEEN(SYSDATE, HIREDATE)) 근무일수 
FROM EMP;
SYSDATE는 시간단위까지 계산됨
날짜 연산하면 소수점 이하까지 출력됨.

ROUND로 날짜 소수점 반올림해서 출력


개월 수 구하기 ADD_MONTHS
ADD_MONTHS(날짜, '개월수')

SELECT  ENAME 이름, SYSDATE 오늘, HIREDATE 입사일, 
        ADD_MONTHS(HIREDATE, 6) 입사6개월후 
FROM EMP;


가까운 요일의 날짜 반환 NEXT_DAY
NEXT_DAY(날짜,'요일')

SELECT  SYSDATE 오늘,
        NEXT_DAY(SYSDATE,'수요일')"다음 수요일" 
FROM DUAL;
요일 한글 인식 가능

지정 월의 마지막 날을 반환 LAST_DAY
LAST_DAY(날짜)

SELECT  HIREDATE 입사일, 
        LAST_DAY(HIREDATE) "입사한 달 마지막날" 
FROM EMP;

# 형변환 함수
날짜•시간 형식 변환 출력하기 TO_CHAR
TO_CHAR (날짜, '출력형식')


-- '년-월-일' 형식으로 출력하기
SELECT SYSDATE "오늘", TO_CHAR(SYSDATE, 'YYYY-MM-DD')"날짜 형식 변형" FROM DUAL;


-- '날짜+요일'형식으로 출력하기
SELECT HIREDATE 오늘, TO_CHAR(HIREDATE, 'YYYY/MM/DD DAY') "입사일, 요일" FROM EMP;


TO_CHAR (날짜, '시간형식')



-- '날짜+시간'형식으로 출력하기
SELECT TO_CHAR(SYSDATE, 'YYY/MM/DD, HH12:MI:SS')"날짜+12시간" FROM DUAL;
SELECT TO_CHAR(SYSDATE, 'YYY/MM/DD, HH24:MI:SS')"날짜+24시간" FROM DUAL;


숫자 형식 변형 출력하기 TO_CHAR
TO_CHAR(숫자, '변형형식')


-- 원화(\)로 출력하기.
SELECT ENAME 이름 , SAL 연봉, TO_CHAR(SAL, 'L999,999') FROM EMP;
SELECT ENAME 이름 , SAL 연봉, TO_CHAR(SAL, 'L000,000') FROM EMP;
L999,999 L000,000

L : 통화(원화)출력을 의미함

999,999 : 자리수와 ,의 위치를 지정하고, 빈자리는 비워서 출력함.

000,000 : 자리수와 ,의 위치를 지정하고, 빈자리는 0으로 채워서 출력함.


문자형 날짜형 변환 TO_DATE
TO_DATE(‘문자’, ‘날짜형식')

-- 문자를 날짜형식으로 변환해 데이터 찾기.
SELECT ENAME , HIREDATE FROM EMP 
WHERE HIREDATE = TO_DATE(19810220, 'YYYYMMDD');


-- 문자형 날짜형으로 변환해 날짜연산하기
SELECT SYSDATE-TO_DATE('2008/01/01', 'YYYY/MM/DD') "08년1월1일 ~ 현재" FROM DUAL;
SELECT TRUNC(SYSDATE-TO_DATE('2008/01/01', 'YYYY/MM/DD')) "TRUNC(08년1월1일 ~ 현재)" FROM DUAL;


문자형 숫자 형 변환 TO_NUMBER
SELECT TO_NUMBER('20,000','99,999') - TO_NUMBER('10,000', '99,999') 
FROM DUAL;

++ NULL값 변환 NVL 함수
SELECT ENAME "직원명", SAL "월급", COMM "성과급", SAL*12+COMM "NULL연봉", NVL(COMM , 0) , SAL*12+NVL(COMM, 0)"NVL연봉" FROM EMP ORDER BY JOB;
-- NVL(COMM , 0) : NULL값을 0으로 변환
-- 연산시  NULL 값이 문제가 됨.


--7. 상사(MANAGER)이 없는 사원만 출력하되 MGR 칼럼 값 NULL 대신 CEO로 출력
SELECT EMPNO ,ENAME , NVL(TO_CHAR(MGR, '9999'), 'C E O') MANAGER FROM EMP WHERE MGR IS NULL;
-- TO_CHAR(MGR, '999') 
-- MGR는 NUMBER 타입으로 선언됨.
-- CHAR 타입으로 형변환 후, CHAR 타입의 '9999' 비워둠.


++ DECODE 함수(switch case)
SELECT ENAME, DEPTNO, DECODE(DEPTNO, 10, 'ACCONUNTING',
                                    20, 'RESERCH',
                                    30, 'SALES',
                                    40, 'OPERATIONS') AS DNAME
FROM EMP;


/*
8. 직급에 따라 급여를 인상하도록 하자. 직급이 'ANAlYST'인 사원은 5%,
'SALESMAN'인 사원은 10%, 'MANAGER'인 사원은 15%, 'CLERK'인 사원
은 20%인 인상한다.
*/
SELECT EMPNO, JOB, SAL, DECODE(JOB, 'ANALYST', ROUND(SAL*1.05),
                                    'SALESMAN', ROUND(SAL*1.1),
                                    'MANAGER', ROUND(SAL*1.15),
                                    'CLERK', ROUND(SAL*1.2),
                                    'PRESIDENT', SAL) AS UPSAL 
FROM EMP;


++ CASE 함수(if -else if -else)
SELECT ENAME , DEPTNO, CASE WHEN DEPTNO = 10 THEN 'ACCOUNTING'
                            WHEN DEPTNO = 20 THEN 'RESERCH'
                            WHEN DEPTNO = 30 THEN 'SALES'
                            WHEN DEPTNO = 40 THEN 'OPERATION'
                        END AS DNAME
FROM EMP;
