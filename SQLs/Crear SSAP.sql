alter session set "_oracle_script"=TRUE;

-------------------
--SAAP
-------------------
drop user SSAP CASCADE;
create user SSAP identified by 123456;
grant connect, resource to SSAP;
grant unlimited tablespace to SSAP;
grant create job to SSAP;

-------------------
--SAAP_TEST
-------------------
drop user SSAP_TEST CASCADE;
create user SSAP_TEST identified by 123456;
grant connect, resource to SSAP_TEST;
grant unlimited tablespace to SSAP_TEST;
grant create job to SSAP_TEST;