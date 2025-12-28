-- Sentencias DDL
--CRUD
-- C INSERT
-- R SELECT
-- U UPDATE
-- D DELETE

-- INSERT
INSERT INTO alumno(nro_documento, nombre) VALUES('100','Caled Lima');

-- INSERTA VARIOS REGISTROS
INSERT INTO alumno(nro_documento, nombre)

VALUES
('123','Delgado Tenorio'),
('200','Ana Martinez'),
('300','Luis Lopez'),
('400','Arturo Gonzales'),
('500','Monica Tejada'),
('600','Raul Rivera'),
('700','Andrea Valencia'),
('800','Sofia Mamani'),
('900','Carlos Perez'),
('1000','Jesus Concha');

-- Actualizar datos
UPDATE alumno set
email = 'Codigo@gmail.com';

--Update con Where
UPDATE alumno
set email = 'Caeltas@gmail.com' WHERE id = 1;

--UPDATE CON FUNCIONES
UPDATE alumno
set email = CONCAT(LOWER(replace(nombre,' ','.')),'gmail.com')WHERE id >1

select * from alumno;
select nombre,email from alumno;
select nombre from alumno where id > 5;
select * from alumno order by nombre asc;


DELETE from alumno where id=3

TRUNCATE alumno