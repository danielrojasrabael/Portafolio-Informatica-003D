--------------------------------------------------------
-- Archivo creado  - miércoles-septiembre-14-2022   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table ADMINISTRADORES
--------------------------------------------------------

  CREATE TABLE "ADMINISTRADORES" 
   ("ID_USUARIO" NUMBER(13,0), 
	"RUT_ADMIN" VARCHAR2(13 BYTE), 
	"NOMBRE" VARCHAR2(200 BYTE)
   );
--------------------------------------------------------
--  DDL for Table ASESORIA
--------------------------------------------------------
  CREATE TABLE "ASESORIA" 
   (	"ID_ASESORIA" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"FECHA_PUBLICACION" DATE, 
	"MOTIVO" CLOB, 
	"FECHA_RESPUESTA" DATE, 
	"RESPUESTA" CLOB, 
	"ID_SOLICITUD" NUMBER(13,0), 
	"ARCHIVO" VARCHAR2(200 BYTE)
   );
   ALTER TABLE "ASESORIA" ADD "TIPO_ASESORIA" VARCHAR2(200);
   
--------------------------------------------------------
--  DDL for Table CAPACITACION
--------------------------------------------------------

  CREATE TABLE "CAPACITACION" 
   (	"ID_CAPACITACION" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"NOMBRE" VARCHAR2(200 BYTE), 
	"UBICACION" VARCHAR2(200 BYTE), 
	"ESTADO" VARCHAR2(200 BYTE),
    "DURACION" NUMBER(13,0) NOT NULL,
	"FECHA" DATE, 
	"ID_CONTRATO" NUMBER(13,0), 
	"ID_COMUNA" NUMBER(10,0)
   );
   
--------------------------------------------------------
--  DDL for Table CHECKLIST
--------------------------------------------------------

  CREATE TABLE "CHECKLIST" 
   (	"ID_CHECKLIST" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"ELEMENTOS" CLOB, 
	"ID_CONTRATO" NUMBER(13,0)
   );
   
--------------------------------------------------------
--  DDL for Table CIUDAD
--------------------------------------------------------

  CREATE TABLE "CIUDAD" 
   (	"ID_CIUDAD" NUMBER(10,0), 
	"NOMBRE" VARCHAR2(100 BYTE), 
	"ID_REGION" NUMBER(10,0)
   ); 
   
--------------------------------------------------------
--  DDL for Table CLIENTES
--------------------------------------------------------

  CREATE TABLE "CLIENTES" 
   (	"ID_USUARIO" NUMBER(13,0), 
	"RUT_CLIENTE" VARCHAR2(13 BYTE), 
	"NOMBRE_EMPRESA" VARCHAR2(200 BYTE), 
	"RUBRO_EMPRESA" VARCHAR2(200 BYTE), 
	"CANT_TRABAJADORES" NUMBER(10,0) NOT NULL,
    "CONTADOR_SOLICITUD" NUMBER(10,0)
   );
   
--------------------------------------------------------
--  DDL for Table COMUNA
--------------------------------------------------------

  CREATE TABLE "COMUNA" 
   (	"ID_COMUNA" NUMBER(10,0), 
	"ID_CIUDAD" NUMBER(10,0), 
	"NOMBRE" VARCHAR2(100 BYTE)
   ); 
--------------------------------------------------------
--  DDL for Table CONTRATO
--------------------------------------------------------

  CREATE TABLE "CONTRATO" 
   (	"ID_CONTRATO" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"COSTO_BASE" NUMBER(20,0), 
	"FECHA_FIRMA" DATE, 
	"ULTIMO_PAGO" DATE, 
	"RUT_CLIENTE" VARCHAR2(13 BYTE), 
	"RUT_PROFESIONAL" VARCHAR2(13 BYTE)
   );
   
--------------------------------------------------------
--  DDL for Table NOTIFICACION
--------------------------------------------------------

  CREATE TABLE "NOTIFICACION" 
   (	"ID_NOTIFICACION" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"TITULO" VARCHAR2(200 BYTE), 
	"DESCRIPCION" CLOB, 
	"FECHA" DATE, 
	"RUT_CLIENTE" VARCHAR2(13 BYTE)
   ); 
   
--------------------------------------------------------
--  DDL for Table PAGO_MENSUALIDAD
--------------------------------------------------------

  CREATE TABLE "PAGO_MENSUALIDAD" 
   (	"ID_MENSUALIDAD" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"FECHA_LIMITE" DATE, 
	"ESTADO" NUMBER(10,0), 
	"COSTO" NUMBER(20,0), 
	"ID_CONTRATO" NUMBER(13,0)
   );
   ALTER TABLE "PAGO_MENSUALIDAD" ADD("FECHA_PAGO" DATE, "BOLETA" VARCHAR2(255));
--------------------------------------------------------
--  DDL for Table PROFESIONALES
--------------------------------------------------------

  CREATE TABLE "PROFESIONALES" 
   (	"ID_USUARIO" NUMBER(13,0), 
	"RUT_PROF" VARCHAR2(13 BYTE), 
	"NOMBRE" VARCHAR2(200 BYTE)
   ); 
   
--------------------------------------------------------
--  DDL for Table REGION
--------------------------------------------------------

  CREATE TABLE "REGION" 
   (	
    "ID_REGION" NUMBER(10,0), 
	"NOMBRE" VARCHAR2(100 BYTE)
   ); 
   
--------------------------------------------------------
--  DDL for Table REPORTE_ACCIDENTE
--------------------------------------------------------

  CREATE TABLE "REPORTE_ACCIDENTE" 
   (	"ID_REPORTE_ACCIDENTE" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"FECHA" DATE, 
	"DESCRIPCION" CLOB, 
	"ID_CONTRATO" NUMBER(13,0)
   ); 
   
--------------------------------------------------------
--  DDL for Table REPORTE_FINAL
--------------------------------------------------------

  CREATE TABLE "REPORTE_FINAL" 
   (	"ID_REPORTE_FINAL" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"ARCHIVO" VARCHAR2(200 BYTE), 
	"FECHA_GENERACION" DATE, 
	"RUT_CLIENTE" VARCHAR2(13 BYTE)
   ); 
   
--------------------------------------------------------
--  DDL for Table SOLICITUD
--------------------------------------------------------

  CREATE TABLE "SOLICITUD" 
   (	"ID_SOLICITUD" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"ESTADO" VARCHAR2(20 BYTE), 
	"TIPO" VARCHAR2(20 BYTE), 
	"ID_CONTRATO" NUMBER(13,0)
   ); 
   
--------------------------------------------------------
--  DDL for Table SOLICITUD_CAPACITACION
--------------------------------------------------------

  CREATE TABLE "SOLICITUD_CAPACITACION" 
   (	"ID_SOLI_CAPACITACION" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"FECHA_PUBLICACION" DATE, 
	"MOTIVO" CLOB, 
	"ARCHIVO" VARCHAR2(200 BYTE), 
	"ID_SOLICITUD" NUMBER(13,0)
   ); 
   
--------------------------------------------------------
--  DDL for Table USUARIO
--------------------------------------------------------

  CREATE TABLE "USUARIO" 
   (	"ID_USUARIO" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1), 
	"CONTRASEÑA" VARCHAR2(999), 
	"TIPO" VARCHAR2(20 BYTE), 
	"ID_COMUNA" NUMBER(13,0), 
	"DIRECCION" VARCHAR2(200 BYTE),
    "CORREO" VARCHAR2(200 BYTE) NOT NULL,
    "ESTADO" NUMBER(13,0) DEFAULT 1
   ); 
   
--------------------------------------------------------
--  DDL for Table VISITA
--------------------------------------------------------

  CREATE TABLE "VISITA" 
   (	"ID_VISITA" NUMBER(13,0) GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) , 
	"FECHA" DATE, 
	"ESTADO" NUMBER(13,0), 
	"UBICACION" VARCHAR2(200 BYTE), 
	"REPORTE_FINAL" VARCHAR2(200 BYTE), 
    "PERIODO" DATE,
	"ID_CONTRATO" NUMBER(13,0), 
	"ID_COMUNA" NUMBER(13,0)
   ); 

--------------------------------------------------------
--  DDL for Index PK_ADMINISTRADORES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_ADMINISTRADORES" ON "ADMINISTRADORES" ("RUT_ADMIN");
 
--------------------------------------------------------
--  DDL for Index PK_ASESORIA
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_ASESORIA" ON "ASESORIA" ("ID_ASESORIA");
  
--------------------------------------------------------
--  DDL for Index PK_CAPACITACION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CAPACITACION" ON "CAPACITACION" ("ID_CAPACITACION");
--------------------------------------------------------
--  DDL for Index PK_CHECKLIST
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CHECKLIST" ON "CHECKLIST" ("ID_CHECKLIST");
--------------------------------------------------------
--  DDL for Index PK_CIUDAD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CIUDAD" ON "CIUDAD" ("ID_CIUDAD");
--------------------------------------------------------
--  DDL for Index PK_CLIENTES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CLIENTES" ON "CLIENTES" ("RUT_CLIENTE");
--------------------------------------------------------
--  DDL for Index PK_COMUNA
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_COMUNA" ON "COMUNA" ("ID_COMUNA");
--------------------------------------------------------
--  DDL for Index PK_CONTRATO
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CONTRATO" ON "CONTRATO" ("ID_CONTRATO");
--------------------------------------------------------
--  DDL for Index PK_NOTIFICACION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_NOTIFICACION" ON "NOTIFICACION" ("ID_NOTIFICACION");
--------------------------------------------------------
--  DDL for Index PK_PAGO_MENSUALIDAD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_PAGO_MENSUALIDAD" ON "PAGO_MENSUALIDAD" ("ID_MENSUALIDAD");
--------------------------------------------------------
--  DDL for Index PK_PROFESIONAL
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_PROFESIONAL" ON "PROFESIONALES" ("RUT_PROF");
--------------------------------------------------------
--  DDL for Index PK_REGION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REGION" ON "REGION" ("ID_REGION");
--------------------------------------------------------
--  DDL for Index PK_REPORTE_ACCIDENTE
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REPORTE_ACCIDENTE" ON "REPORTE_ACCIDENTE" ("ID_REPORTE_ACCIDENTE");
--------------------------------------------------------
--  DDL for Index PK_REPORTE_FINALES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REPORTE_FINALES" ON "REPORTE_FINAL" ("ID_REPORTE_FINAL");
--------------------------------------------------------
--  DDL for Index PK_SOLICITUD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_SOLICITUD" ON "SOLICITUD" ("ID_SOLICITUD");
--------------------------------------------------------
--  DDL for Index PK_SOLICITUD_CAP
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_SOLICITUD_CAP" ON "SOLICITUD_CAPACITACION" ("ID_SOLI_CAPACITACION");
--------------------------------------------------------
--  DDL for Index PK_USUARIO
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_USUARIO" ON "USUARIO" ("ID_USUARIO");
--------------------------------------------------------
--  DDL for Index PK_VISITAS
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_VISITAS" ON "VISITA" ("ID_VISITA");
--------------------------------------------------------
--  DDL for Index PK_ADMINISTRADORES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_ADMINISTRADORES" ON "ADMINISTRADORES" ("RUT_ADMIN");
--------------------------------------------------------
--  DDL for Index PK_ASESORIA
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_ASESORIA" ON "ASESORIA" ("ID_ASESORIA");
--------------------------------------------------------
--  DDL for Index PK_CAPACITACION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CAPACITACION" ON "CAPACITACION" ("ID_CAPACITACION");
--------------------------------------------------------
--  DDL for Index PK_CHECKLIST
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CHECKLIST" ON "CHECKLIST" ("ID_CHECKLIST");
--------------------------------------------------------
--  DDL for Index PK_CIUDAD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CIUDAD" ON "CIUDAD" ("ID_CIUDAD");
--------------------------------------------------------
--  DDL for Index PK_CLIENTES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CLIENTES" ON "CLIENTES" ("RUT_CLIENTE");
--------------------------------------------------------
--  DDL for Index PK_COMUNA
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_COMUNA" ON "COMUNA" ("ID_COMUNA");
--------------------------------------------------------
--  DDL for Index PK_CONTRATO
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_CONTRATO" ON "CONTRATO" ("ID_CONTRATO");
--------------------------------------------------------
--  DDL for Index PK_NOTIFICACION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_NOTIFICACION" ON "NOTIFICACION" ("ID_NOTIFICACION");
--------------------------------------------------------
--  DDL for Index PK_PAGO_MENSUALIDAD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_PAGO_MENSUALIDAD" ON "PAGO_MENSUALIDAD" ("ID_MENSUALIDAD");
--------------------------------------------------------
--  DDL for Index PK_PROFESIONAL
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_PROFESIONAL" ON "PROFESIONALES" ("RUT_PROF");
  
--------------------------------------------------------
--  DDL for Index PK_REGION
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REGION" ON "REGION" ("ID_REGION");
--------------------------------------------------------
--  DDL for Index PK_REPORTE_ACCIDENTE
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REPORTE_ACCIDENTE" ON "REPORTE_ACCIDENTE" ("ID_REPORTE_ACCIDENTE");
  
--------------------------------------------------------
--  DDL for Index PK_REPORTE_FINALES
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_REPORTE_FINALES" ON "REPORTE_FINAL" ("ID_REPORTE_FINAL");
--------------------------------------------------------
--  DDL for Index PK_SOLICITUD
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_SOLICITUD" ON "SOLICITUD" ("ID_SOLICITUD");
  
--------------------------------------------------------
--  DDL for Index PK_SOLICITUD_CAP
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_SOLICITUD_CAP" ON "SOLICITUD_CAPACITACION" ("ID_SOLI_CAPACITACION");
--------------------------------------------------------
--  DDL for Index PK_USUARIO
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_USUARIO" ON "USUARIO" ("ID_USUARIO");
--------------------------------------------------------
--  DDL for Index PK_VISITAS
--------------------------------------------------------

  CREATE UNIQUE INDEX "PK_VISITAS" ON "VISITA" ("ID_VISITA");

--------------------------------------------------------
--  Constraints for Table ADMINISTRADORES
--------------------------------------------------------

  ALTER TABLE "ADMINISTRADORES" MODIFY ("ID_USUARIO" NOT NULL ENABLE);
  ALTER TABLE "ADMINISTRADORES" MODIFY ("RUT_ADMIN" NOT NULL ENABLE);
  ALTER TABLE "ADMINISTRADORES" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "ADMINISTRADORES" ADD CONSTRAINT "PK_ADMINISTRADORES" PRIMARY KEY ("RUT_ADMIN");
  
--------------------------------------------------------
--  Constraints for Table ASESORIA
--------------------------------------------------------

  ALTER TABLE "ASESORIA" MODIFY ("ID_ASESORIA" NOT NULL ENABLE);
  ALTER TABLE "ASESORIA" MODIFY ("FECHA_PUBLICACION" NOT NULL ENABLE);
  ALTER TABLE "ASESORIA" MODIFY ("MOTIVO" NOT NULL ENABLE);
  ALTER TABLE "ASESORIA" MODIFY ("ID_SOLICITUD" NOT NULL ENABLE);
  ALTER TABLE "ASESORIA" ADD CONSTRAINT "PK_ASESORIA" PRIMARY KEY ("ID_ASESORIA");
--------------------------------------------------------
--  Constraints for Table CAPACITACION
--------------------------------------------------------

  ALTER TABLE "CAPACITACION" MODIFY ("ID_CAPACITACION" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("UBICACION" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("ESTADO" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("FECHA" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" MODIFY ("ID_COMUNA" NOT NULL ENABLE);
  ALTER TABLE "CAPACITACION" ADD CONSTRAINT "PK_CAPACITACION" PRIMARY KEY ("ID_CAPACITACION");
--------------------------------------------------------
--  Constraints for Table CHECKLIST
--------------------------------------------------------

  ALTER TABLE "CHECKLIST" MODIFY ("ID_CHECKLIST" NOT NULL ENABLE);
  ALTER TABLE "CHECKLIST" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "CHECKLIST" ADD CONSTRAINT "PK_CHECKLIST" PRIMARY KEY ("ID_CHECKLIST");
  
--------------------------------------------------------
--  Constraints for Table CIUDAD
--------------------------------------------------------

  ALTER TABLE "CIUDAD" MODIFY ("ID_CIUDAD" NOT NULL ENABLE);
  ALTER TABLE "CIUDAD" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "CIUDAD" MODIFY ("ID_REGION" NOT NULL ENABLE);
  ALTER TABLE "CIUDAD" ADD CONSTRAINT "PK_CIUDAD" PRIMARY KEY ("ID_CIUDAD");
--------------------------------------------------------
--  Constraints for Table CLIENTES
--------------------------------------------------------

  ALTER TABLE "CLIENTES" MODIFY ("ID_USUARIO" NOT NULL ENABLE);
  ALTER TABLE "CLIENTES" MODIFY ("RUT_CLIENTE" NOT NULL ENABLE);
  ALTER TABLE "CLIENTES" MODIFY ("NOMBRE_EMPRESA" NOT NULL ENABLE);
  ALTER TABLE "CLIENTES" MODIFY ("RUBRO_EMPRESA" NOT NULL ENABLE);
  ALTER TABLE "CLIENTES" MODIFY ("CANT_TRABAJADORES" NOT NULL ENABLE);
  ALTER TABLE "CLIENTES" ADD CONSTRAINT "PK_CLIENTES" PRIMARY KEY ("RUT_CLIENTE");
  
--------------------------------------------------------
--  Constraints for Table COMUNA
--------------------------------------------------------

  ALTER TABLE "COMUNA" MODIFY ("ID_COMUNA" NOT NULL ENABLE);
  ALTER TABLE "COMUNA" MODIFY ("ID_CIUDAD" NOT NULL ENABLE);
  ALTER TABLE "COMUNA" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "COMUNA" ADD CONSTRAINT "PK_COMUNA" PRIMARY KEY ("ID_COMUNA");
  
--------------------------------------------------------
--  Constraints for Table CONTRATO
--------------------------------------------------------

  ALTER TABLE "CONTRATO" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" MODIFY ("COSTO_BASE" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" MODIFY ("FECHA_FIRMA" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" MODIFY ("ULTIMO_PAGO" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" MODIFY ("RUT_CLIENTE" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" MODIFY ("RUT_PROFESIONAL" NOT NULL ENABLE);
  ALTER TABLE "CONTRATO" ADD CONSTRAINT "PK_CONTRATO" PRIMARY KEY ("ID_CONTRATO");
--------------------------------------------------------
--  Constraints for Table NOTIFICACION
--------------------------------------------------------

  ALTER TABLE "NOTIFICACION" MODIFY ("ID_NOTIFICACION" NOT NULL ENABLE);
  ALTER TABLE "NOTIFICACION" MODIFY ("TITULO" NOT NULL ENABLE);
  ALTER TABLE "NOTIFICACION" MODIFY ("DESCRIPCION" NOT NULL ENABLE);
  ALTER TABLE "NOTIFICACION" MODIFY ("FECHA" NOT NULL ENABLE);
  ALTER TABLE "NOTIFICACION" MODIFY ("RUT_CLIENTE" NOT NULL ENABLE);
  ALTER TABLE "NOTIFICACION" ADD CONSTRAINT "PK_NOTIFICACION" PRIMARY KEY ("ID_NOTIFICACION");
--------------------------------------------------------
--  Constraints for Table PAGO_MENSUALIDAD
--------------------------------------------------------

  ALTER TABLE "PAGO_MENSUALIDAD" ADD CONSTRAINT "PK_PAGO_MENSUALIDAD" PRIMARY KEY ("ID_MENSUALIDAD");
  ALTER TABLE "PAGO_MENSUALIDAD" MODIFY ("ID_MENSUALIDAD" NOT NULL ENABLE);
  ALTER TABLE "PAGO_MENSUALIDAD" MODIFY ("FECHA_LIMITE" NOT NULL ENABLE);
  ALTER TABLE "PAGO_MENSUALIDAD" MODIFY ("ESTADO" NOT NULL ENABLE);
  ALTER TABLE "PAGO_MENSUALIDAD" MODIFY ("COSTO" NOT NULL ENABLE);
  ALTER TABLE "PAGO_MENSUALIDAD" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table PROFESIONALES
--------------------------------------------------------

  ALTER TABLE "PROFESIONALES" MODIFY ("ID_USUARIO" NOT NULL ENABLE);
  ALTER TABLE "PROFESIONALES" MODIFY ("RUT_PROF" NOT NULL ENABLE);
  ALTER TABLE "PROFESIONALES" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "PROFESIONALES" ADD CONSTRAINT "PK_PROFESIONAL" PRIMARY KEY ("RUT_PROF");
  
--------------------------------------------------------
--  Constraints for Table REGION
--------------------------------------------------------

  ALTER TABLE "REGION" MODIFY ("ID_REGION" NOT NULL ENABLE);
  ALTER TABLE "REGION" MODIFY ("NOMBRE" NOT NULL ENABLE);
  ALTER TABLE "REGION" ADD CONSTRAINT "PK_REGION" PRIMARY KEY ("ID_REGION");
--------------------------------------------------------
--  Constraints for Table REPORTE_ACCIDENTE
--------------------------------------------------------

  ALTER TABLE "REPORTE_ACCIDENTE" MODIFY ("ID_REPORTE_ACCIDENTE" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_ACCIDENTE" MODIFY ("FECHA" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_ACCIDENTE" MODIFY ("DESCRIPCION" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_ACCIDENTE" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_ACCIDENTE" ADD CONSTRAINT "PK_REPORTE_ACCIDENTE" PRIMARY KEY ("ID_REPORTE_ACCIDENTE");
--------------------------------------------------------
--  Constraints for Table REPORTE_FINAL
--------------------------------------------------------

  ALTER TABLE "REPORTE_FINAL" MODIFY ("ID_REPORTE_FINAL" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_FINAL" MODIFY ("ARCHIVO" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_FINAL" MODIFY ("FECHA_GENERACION" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_FINAL" MODIFY ("RUT_CLIENTE" NOT NULL ENABLE);
  ALTER TABLE "REPORTE_FINAL" ADD CONSTRAINT "PK_REPORTE_FINALES" PRIMARY KEY ("ID_REPORTE_FINAL");
  
--------------------------------------------------------
--  Constraints for Table SOLICITUD
--------------------------------------------------------

  ALTER TABLE "SOLICITUD" MODIFY ("ID_SOLICITUD" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD" MODIFY ("ESTADO" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD" MODIFY ("TIPO" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD" ADD CONSTRAINT "PK_SOLICITUD" PRIMARY KEY ("ID_SOLICITUD");
  
--------------------------------------------------------
--  Constraints for Table SOLICITUD_CAPACITACION
--------------------------------------------------------

  ALTER TABLE "SOLICITUD_CAPACITACION" MODIFY ("ID_SOLI_CAPACITACION" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD_CAPACITACION" MODIFY ("FECHA_PUBLICACION" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD_CAPACITACION" MODIFY ("MOTIVO" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD_CAPACITACION" MODIFY ("ID_SOLICITUD" NOT NULL ENABLE);
  ALTER TABLE "SOLICITUD_CAPACITACION" ADD CONSTRAINT "PK_SOLICITUD_CAP" PRIMARY KEY ("ID_SOLI_CAPACITACION");
--------------------------------------------------------
--  Constraints for Table USUARIO
--------------------------------------------------------

-- Error: Ya es not null  ALTER TABLE "USUARIO" MODIFY ("ID_USUARIO" NOT NULL ENABLE);
  ALTER TABLE "USUARIO" MODIFY ("CONTRASEÑA" NOT NULL ENABLE);
  ALTER TABLE "USUARIO" MODIFY ("TIPO" NOT NULL ENABLE);
  ALTER TABLE "USUARIO" MODIFY ("ID_COMUNA" NOT NULL ENABLE);
  ALTER TABLE "USUARIO" MODIFY ("DIRECCION" NOT NULL ENABLE);
  ALTER TABLE "USUARIO" ADD CONSTRAINT "PK_USUARIO" PRIMARY KEY ("ID_USUARIO");
  
--------------------------------------------------------
--  Constraints for Table VISITA
--------------------------------------------------------

  ALTER TABLE "VISITA" MODIFY ("ID_VISITA" NOT NULL ENABLE);
  ALTER TABLE "VISITA" MODIFY ("ESTADO" NOT NULL ENABLE);
  ALTER TABLE "VISITA" MODIFY ("ID_CONTRATO" NOT NULL ENABLE);
  ALTER TABLE "VISITA" MODIFY ("ID_COMUNA" NOT NULL ENABLE);
  ALTER TABLE "VISITA" ADD CONSTRAINT "PK_VISITAS" PRIMARY KEY ("ID_VISITA");
--------------------------------------------------------
--  Ref Constraints for Table ADMINISTRADORES
--------------------------------------------------------

  ALTER TABLE "ADMINISTRADORES" ADD CONSTRAINT "FK_USUARIO" FOREIGN KEY ("ID_USUARIO")
	  REFERENCES "USUARIO" ("ID_USUARIO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table ASESORIA
--------------------------------------------------------

  ALTER TABLE "ASESORIA" ADD CONSTRAINT "FK_SOLICITUD_ASE" FOREIGN KEY ("ID_SOLICITUD")
	  REFERENCES "SOLICITUD" ("ID_SOLICITUD") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table CAPACITACION
--------------------------------------------------------

  ALTER TABLE "CAPACITACION" ADD CONSTRAINT "FK_CONTRATO_CAPACITACION" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
  ALTER TABLE "CAPACITACION" ADD CONSTRAINT "FK_COMUNA_CAPACITACION" FOREIGN KEY ("ID_COMUNA")
	  REFERENCES "COMUNA" ("ID_COMUNA") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table CHECKLIST
--------------------------------------------------------

  ALTER TABLE "CHECKLIST" ADD CONSTRAINT "FK_CONTRATO_CHECKLIST" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table CIUDAD
--------------------------------------------------------

  ALTER TABLE "CIUDAD" ADD CONSTRAINT "FK_REGION" FOREIGN KEY ("ID_REGION")
	  REFERENCES "REGION" ("ID_REGION") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table CLIENTES
--------------------------------------------------------

  ALTER TABLE "CLIENTES" ADD CONSTRAINT "FK_USUARIO_CLIENTE" FOREIGN KEY ("ID_USUARIO")
	  REFERENCES "USUARIO" ("ID_USUARIO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table COMUNA
--------------------------------------------------------

  ALTER TABLE "COMUNA" ADD CONSTRAINT "FK_CIUDAD" FOREIGN KEY ("ID_CIUDAD")
	  REFERENCES "CIUDAD" ("ID_CIUDAD") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table CONTRATO
--------------------------------------------------------

  ALTER TABLE "CONTRATO" ADD CONSTRAINT "FK_CLIENTE_CONTRATO" FOREIGN KEY ("RUT_CLIENTE")
	  REFERENCES "CLIENTES" ("RUT_CLIENTE") ENABLE;
  ALTER TABLE "CONTRATO" ADD CONSTRAINT "FK_PROFESIONAL_CONTRATO" FOREIGN KEY ("RUT_PROFESIONAL")
	  REFERENCES "PROFESIONALES" ("RUT_PROF") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table NOTIFICACION
--------------------------------------------------------

  ALTER TABLE "NOTIFICACION" ADD CONSTRAINT "FK_CLIENTE" FOREIGN KEY ("RUT_CLIENTE")
	  REFERENCES "CLIENTES" ("RUT_CLIENTE") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PAGO_MENSUALIDAD
--------------------------------------------------------

  ALTER TABLE "PAGO_MENSUALIDAD" ADD CONSTRAINT "FK_CONTRATO_PAGO" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PROFESIONALES
--------------------------------------------------------

  ALTER TABLE "PROFESIONALES" ADD CONSTRAINT "FK_USUARIO_PROF" FOREIGN KEY ("ID_USUARIO")
	  REFERENCES "USUARIO" ("ID_USUARIO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table REPORTE_ACCIDENTE
--------------------------------------------------------

  ALTER TABLE "REPORTE_ACCIDENTE" ADD CONSTRAINT "FK_CONTRATO_REPORTE" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table REPORTE_FINAL
--------------------------------------------------------

  ALTER TABLE "REPORTE_FINAL" ADD CONSTRAINT "FK_CLIENTE_REPORTE" FOREIGN KEY ("RUT_CLIENTE")
	  REFERENCES "CLIENTES" ("RUT_CLIENTE") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SOLICITUD
--------------------------------------------------------

  ALTER TABLE "SOLICITUD" ADD CONSTRAINT "FK_CONTRATO" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table SOLICITUD_CAPACITACION
--------------------------------------------------------

  ALTER TABLE "SOLICITUD_CAPACITACION" ADD CONSTRAINT "FK_SOLICITUD" FOREIGN KEY ("ID_SOLICITUD")
	  REFERENCES "SOLICITUD" ("ID_SOLICITUD") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table USUARIO
--------------------------------------------------------

  ALTER TABLE "USUARIO" ADD CONSTRAINT "FK_COMUNA" FOREIGN KEY ("ID_COMUNA")
	  REFERENCES "COMUNA" ("ID_COMUNA") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table VISITA
--------------------------------------------------------

  ALTER TABLE "VISITA" ADD CONSTRAINT "FK_CONTRATO_VISITA" FOREIGN KEY ("ID_CONTRATO")
	  REFERENCES "CONTRATO" ("ID_CONTRATO") ENABLE;
  ALTER TABLE "VISITA" ADD CONSTRAINT "FK_COMUNA_VISITA" FOREIGN KEY ("ID_COMUNA")
	  REFERENCES "COMUNA" ("ID_COMUNA") ENABLE;

-------------------------
-- Inert Into de prueba
--------------------------

INSERT INTO "REGION" (ID_REGION, NOMBRE) VALUES (1,'RM');
INSERT INTO "REGION" (ID_REGION, NOMBRE) VALUES (2, 'COQUIMBO');

INSERT INTO "CIUDAD" (ID_CIUDAD, NOMBRE, ID_REGION) VALUES (1,'SANTIAGO',1);
INSERT INTO "CIUDAD" (ID_CIUDAD, NOMBRE, ID_REGION) VALUES (2,'MAIPO',1);
INSERT INTO "CIUDAD" (ID_CIUDAD, NOMBRE, ID_REGION) VALUES (3,'ELQUI',2);
INSERT INTO "CIUDAD" (ID_CIUDAD, NOMBRE, ID_REGION) VALUES (4,'LIMARÍ',2);

INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (1,1,'RENCA');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (2,1,'CERRO NAVIA');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (3,2,'BUIN');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (4,2,'SAN BERNARDO');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (5,3,'COQUIMBO');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (6,3,'ANDACOLLO');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (7,4,'OVALLE');
INSERT INTO "COMUNA" (ID_COMUNA, ID_CIUDAD, NOMBRE) VALUES (8,4,'MONTE PATRIA');


INSERT INTO "USUARIO"("CONTRASEÑA", TIPO, ID_COMUNA, DIRECCION, CORREO) VALUES ('1C602AA3C3F983028BB28297EA6083ADD14A71A76A5BE4DEF0ADCA43FCEF00C6CEF1C0D8E2F0B85B6B42EC527F015177EBA6F085F698121F0D3417FF49DFB35F', 'ADMINISTRADOR', 1, 'Calle Falsa', 'correo.default@correo.com');
INSERT INTO "ADMINISTRADORES" VALUES (1,'11.222.333-4','Admin Default');