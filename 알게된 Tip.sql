/* sql 표현 */

-- <> 는 != 와 같음.
select * from test_table where id <> 2;

-- LEFT(문자열, 길이)
select LEFT(name, 2) from test_table;

-- CASE ? WHEN condition then value else defaultvalue end as '--'
select CASE COUNTRY_ID WHEN 'AR' THEN '아르헨티나' ELSE '그외' END AS "국가명"