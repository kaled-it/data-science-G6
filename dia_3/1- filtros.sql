-- FILTROS
SELECT * FROM empleado WHERE PAIS = 'PERU';
SELECT * FROM empleado WHERE salario > 5000;
SELECT * FROM empleado WHERE salario > 5000 AND pais = 'Peru';
SELECT * from empleado
where salario >10000
and (pais = 'Peru' or pais = 'Colombia');

SELECT * from empleado
where area = 'training'
AND (pais = 'Argentina' and salario > 15000)

SELECT * from empleado
where pais in ('Colombia', 'Peru', ' Chile');

SELECT * from empleado
where salario BETWEEN 10000 and 15000
and (area in ('Legal', 'Human Resources'));DISCARD