--select * from mage.green_taxi limit 10

--select convert(date,lpep_pickup_date) from mage.green_taxi where EXTRACT(MONTH FROM lpep_pickup_date)=11 limit 100
--select TO_CHAR(lpep_pickup_date, 'YYYY-MM-DD')
--from mage.green_taxi where EXTRACT(MONTH FROM lpep_pickup_date)=12 limit 100

--SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'green_taxi';

--SELECT TO_CHAR(lpep_pickup_datetime, 'YYYY-MM-DD HH24:MI:SS') AS fecha_hora FROM mage.green_taxi;

--select count(*) from mage.green_taxi


--RESPUESTAS

--Numero de vendorIds
select distinct vendorid from mage.green_taxi
