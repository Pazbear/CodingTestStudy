/* sql 표현 */

-- <> 는 != 와 같음.
select * from test_table where id <> 2;

-- LEFT(문자열, 길이)
select LEFT(name, 2) from test_table;

-- CASE ? WHEN condition then value else defaultvalue end as '--'
select CASE COUNTRY_ID WHEN 'AR' THEN '아르헨티나' ELSE '그외' END AS "국가명"

--ex) update와 case when 도 가능
update Salary set sex = case sex when 'f' then 'm' else 'f' end;


-- Delete 시 두개의 테이블에서 조건에 맞는 한 테이블의 값만 지우기가 가능
Delete a from A as a, A as b where a < b

--LCASE:소문자로, UCASE : 대문자로
--CONCAT(a, b) = a + b : 문자열 합치기
select user_id, CONCAT(UCASE(LEFT(name,1)), LCASE(SUBSTRING(name, 2))) as 'name' from Users order by user_id;