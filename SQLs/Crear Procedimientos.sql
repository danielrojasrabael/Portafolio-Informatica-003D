-----------------------------------------
-- Procedimientos gestion de Usuario
-----------------------------------------
-- Ingresar Usuarios
-----------------------------------------
CREATE OR REPLACE PROCEDURE insertarUsuario (pass in VARCHAR2,tipo in Varchar2, id_comu in Number, direc in VARCHAR2)
as
begin
    insert into USUARIO (contraseña,tipo,id_comuna,direccion) VALUES (pass,tipo,id_comu,direc);
end;
/


CREATE OR REPLACE PROCEDURE insertarCliente (id_usu in NUMBER,rutCli in VARCHAR2,nomEmpre in Varchar2, rubroEmpre in Varchar2, cant in number)
as
begin

    insert into CLIENTES (id_usuario,rut_cliente,nombre_empresa,rubro_empresa,cant_trabajadores) VALUES (id_usu,rutCli,nomEmpre,rubroEmpre,cant);
end;
/


CREATE OR REPLACE PROCEDURE insertarProfesional (id_usu in NUMBER,rutProf in VARCHAR2,nombre in Varchar2)
as
begin

    insert into profesionales (id_usuario,rut_prof,nombre) VALUES (id_usu,rutProf,nombre);
end;
/

CREATE OR REPLACE PROCEDURE insertarAdministrador(id_usu in NUMBER,rutAdm in VARCHAR2,nombre in Varchar2)
as
begin

    insert into administradores(id_usuario,rut_admin,nombre) VALUES (id_usu,rutAdm,nombre);
end;
/

-----------------------------------------
-- Seleccionar Usuarios
-----------------------------------------
CREATE OR REPLACE PROCEDURE seleccionarUsuarios (registro out SYS_REFCURSOR, order_id in BOOLEAN)
as
begin
    if order_id then
        open registro for select ID_USUARIO ,"CONTRASEÑA" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario ORDER BY id_usuario;
    else
        open registro for select ID_USUARIO ,"CONTRASEÑA" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario ORDER BY estado desc;
    end if;
end;
/

CREATE OR REPLACE PROCEDURE usuario_PORID (registro out SYS_REFCURSOR, idUsr in NUMBER)
as
begin
    open registro for select ID_USUARIO ,"CONTRASEÑA" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario where id_usuario = idUsr;
end;
/

-----------------------------------------
-- Seleccionar Clientes
-----------------------------------------
CREATE OR REPLACE PROCEDURE seleccionarClientes (registro out SYS_REFCURSOR)
as
begin
    
    open registro for select ID_USUARIO ,RUT_CLIENTE ,NOMBRE_EMPRESA ,RUBRO_EMPRESA ,CANT_TRABAJADORES  from Clientes;

end;
/

CREATE OR REPLACE PROCEDURE cliente_PorRut (registro out SYS_REFCURSOR, rutCli in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_CLIENTE ,NOMBRE_EMPRESA ,RUBRO_EMPRESA ,CANT_TRABAJADORES  from Clientes where rut_cliente = rutCli;
end;
/

CREATE OR REPLACE PROCEDURE cliente_PorId (registro out SYS_REFCURSOR, idCli in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_CLIENTE ,NOMBRE_EMPRESA ,RUBRO_EMPRESA ,CANT_TRABAJADORES  from Clientes where ID_USUARIO = idCli;
end;
/
-----------------------------------------
-- Seleccionar Profesionales
-----------------------------------------
CREATE OR REPLACE PROCEDURE seleccionarProfesionales (registro out SYS_REFCURSOR)
as
begin
    
    open registro for select ID_USUARIO ,RUT_PROF ,NOMBRE  from profesionales;

end;
/

CREATE OR REPLACE PROCEDURE profesional_PorRut (registro out SYS_REFCURSOR, rutPro in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_PROF ,NOMBRE  from profesionales where rut_prof = rutPro;
end;
/

CREATE OR REPLACE PROCEDURE profesional_PorId (registro out SYS_REFCURSOR, idPro in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_PROF ,NOMBRE  from profesionales where ID_USUARIO = idPro;
end;
/
-----------------------------------------
-- Seleccionar Administradores
-----------------------------------------

CREATE OR REPLACE PROCEDURE seleccionarAdministradores (registro out SYS_REFCURSOR)
as
begin
    
    open registro for select ID_USUARIO ,RUT_ADMIN ,NOMBRE  from administradores;

end;
/

CREATE OR REPLACE PROCEDURE admin_PorRut (registro out SYS_REFCURSOR, rutAdm in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_ADMIN ,NOMBRE  from administradores where rut_admin = rutAdm;
end;
/

CREATE OR REPLACE PROCEDURE admin_PorId (registro out SYS_REFCURSOR, idAdm in VARCHAR2)
as
begin
    open registro for select ID_USUARIO ,RUT_ADMIN ,NOMBRE  from administradores where ID_USUARIO = idAdm;
end;
/
-----------------------------------------
-- Modificar Usuarios
-----------------------------------------

CREATE OR REPLACE PROCEDURE actualizarUsuario(id_usr in number, contraseña in varchar2, tipo in varchar2, IdComuna in number, direccion in varchar2, estado in number)
as
    vid number := id_usr;
    vpass varchar(999) := contraseña;
    vtipo varchar2(20) := tipo;
    vcomuna number := IdComuna;
    vdireccion varchar2(100) := direccion;
    vestado number := estado;
begin
    update usuario set CONTRASEÑA = vpass, TIPO = vtipo, ID_COMUNA = vcomuna, DIRECCION = vdireccion, ESTADO = vestado where ID_USUARIO = id_usr;
EXCEPTION
    WHEN NO_DATA_FOUND THEN 
        NULL;
    WHEN OTHERS then
        raise;
end actualizarUsuario;
/

CREATE OR REPLACE PROCEDURE actualizarCliente(id_usr in number, rut_usr in varchar2, nombre in varchar2, rubro in varchar2, c_trab in number)
as
    vid number := id_usr;
    vrut varchar2(13) := rut_usr;
    vnombre varchar2(200) := nombre;
    vrubro varchar2(200) := rubro;
    vctrab number := c_trab;
begin
    update clientes set ID_USUARIO = vid, RUT_CLIENTE = vrut, NOMBRE_EMPRESA = vnombre, RUBRO_EMPRESA = vrubro, CANT_TRABAJADORES = vctrab WHERE ID_USUARIO = vid;
EXCEPTION
    WHEN NO_DATA_FOUND THEN 
        NULL;
    WHEN OTHERS then
        raise;
end actualizarCliente;
/

CREATE OR REPLACE PROCEDURE actualizarProfesional(id_usr in number, rut in varchar2, nombre_pro in varchar2)
as
    vid number := id_usr;
    vrut varchar2(13) := rut;
    vnombre varchar2(200) := nombre_pro;
begin
    update profesionales set ID_USUARIO = vid, RUT_PROF = vrut, NOMBRE = vnombre WHERE ID_USUARIO = vid;
EXCEPTION
    WHEN NO_DATA_FOUND THEN 
        NULL;
    WHEN OTHERS then
        raise;
end actualizarProfesional;
/

CREATE OR REPLACE PROCEDURE actualizarAdministrador(id_usr in number, rut in varchar2, nombre_adm in varchar2)
as
    vid number := id_usr;
    vrut varchar2(13) := rut;
    vnombre varchar2(200) := nombre_adm;
begin
    update administradores set ID_USUARIO = vid, RUT_ADMIN = vrut, NOMBRE = vnombre WHERE ID_USUARIO = vid;
EXCEPTION
    WHEN NO_DATA_FOUND THEN 
        NULL;
    WHEN OTHERS then
        raise;
end actualizarAdministrador;
/

-----------------------------------------
-- Contrato
-----------------------------------------

CREATE OR REPLACE PROCEDURE insertarContrato(costo in NUMBER, fecha in VARCHAR2, rutCli in VARCHAR2, rutPro VARCHAR2)
as
begin
    insert into contrato (costo_base, fecha_firma, ultimo_pago, rut_cliente, rut_profesional) VALUES (costo, TO_DATE(fecha, 'YYYY-MM-DD'), TO_DATE(fecha, 'YYYY-MM-DD'), rutCli, rutPro);
    INSERT INTO VISITA (estado,periodo,id_contrato,id_comuna) SELECT 0,TRUNC(SYSDATE, 'MM'),id_contrato,1 FROM CONTRATO WHERE id_contrato = (select max(id_contrato) from contrato);
    INSERT INTO VISITA (estado,periodo,id_contrato,id_comuna) SELECT 0,TRUNC(SYSDATE, 'MM'),id_contrato,1 FROM CONTRATO WHERE id_contrato = (select max(id_contrato) from contrato);
end;
/

------------------------------------------
-- Notificaciones
------------------------------------------
create or replace PROCEDURE insertarNotificacion (titulo in VARCHAR2,descrip in CLOB, fecha in DATE, rutCli in VARCHAR2)
as
begin

    insert into notificacion (TITULO,DESCRIPCION,FECHA,RUT_CLIENTE) VALUES (titulo,descrip,fecha,rutCli);
end;
/

CREATE OR REPLACE PROCEDURE seleccionarNotificaciones(registro out SYS_REFCURSOR, rut in VARCHAR2)
as
begin
    open registro for select ID_NOTIFICACION ,TITULO ,DESCRIPCION ,FECHA ,RUT_CLIENTE  from notificacion WHERE rut_cliente = rut ORDER BY FECHA DESC;
end;
/

CREATE OR REPLACE PROCEDURE eliminarNotificacion(id_not number, rut_usr varchar2)
as
begin
    delete from notificacion where id_notificacion = id_not and rut_cliente=rut_usr;
end;
/

------------------------------------------
-- Capacitaciones
------------------------------------------

create or replace PROCEDURE insertarCapacitacion (nom in VARCHAR2,ubi in VARCHAR2, fecha_v in DATE, id_cont in NUMBER, id_com in NUMBER, duracion_v in NUMBER)
as
begin
    insert into capacitacion (nombre,ubicacion,estado,fecha,id_contrato,id_comuna,duracion) VALUES (nom,ubi,'PENDIENTE',fecha_v,id_cont,id_com,duracion_v);
end;
/

create or replace PROCEDURE capacitacion_PorIdContrato (registro out SYS_REFCURSOR, idCtr in NUMBER)
as
begin
    OPEN REGISTRO FOR SELECT ca.ID_CAPACITACION, ca.NOMBRE, ca.UBICACION || ', ' || co.NOMBRE, ca.ESTADO, ca.FECHA, ca.ID_CONTRATO, ca.DURACION, cli.NOMBRE_EMPRESA
    FROM CAPACITACION ca JOIN COMUNA co ON ca.id_comuna = co.id_comuna 
    JOIN CONTRATO con ON con.ID_CONTRATO = ca.ID_CONTRATO
    JOIN CLIENTES cli ON cli.RUT_CLIENTE = con.RUT_CLIENTE
    WHERE ca.ID_CONTRATO = idCtr ORDER BY ca.FECHA DESC;
end;
/

create or replace PROCEDURE capacitacion_PorId(registro out SYS_REFCURSOR, idCap in NUMBER)
as
begin
    OPEN REGISTRO FOR SELECT ca.ID_CAPACITACION, ca.NOMBRE, ca.UBICACION, ca.ESTADO, ca.DURACION, ca.FECHA, ca.ID_CONTRATO, ca.ID_COMUNA, cli.NOMBRE_EMPRESA 
    FROM CAPACITACION ca JOIN CONTRATO con ON con.ID_CONTRATO = ca.ID_CONTRATO
    JOIN CLIENTES cli ON cli.RUT_CLIENTE = con.RUT_CLIENTE
    WHERE ca.ID_CAPACITACION = idCap;
end;
/

create or replace PROCEDURE actualizarCapacitacion(estado_v in VARCHAR2, idCap in NUMBER)
as
begin
    UPDATE CAPACITACION SET ESTADO = estado_v WHERE ID_CAPACITACION = idCap;
end;
/
------------------------------------------
-- Ubicaciones
------------------------------------------

create or replace PROCEDURE seleccionarUbicacion (registro out SYS_REFCURSOR)
as
begin
    open registro for SELECT co.id_comuna, co.nombre "nombre_comuna", ci.nombre "nombre_ciudad", re.nombre "nombre_region" FROM comuna co JOIN ciudad ci ON ci.id_ciudad = co.id_ciudad JOIN region re ON ci.id_region = re.id_region;
end;
/

create or replace PROCEDURE contrato_porRutCliente (registro out SYS_REFCURSOR, rutCli in VARCHAR2)
as
begin
    open registro for select ID_CONTRATO, COSTO_BASE, FECHA_FIRMA, ULTIMO_PAGO, RUT_CLIENTE, RUT_PROFESIONAL  from contrato where RUT_CLIENTE = rutCli;
end;
/

create or replace PROCEDURE contratos_porRutProfesional (registro out SYS_REFCURSOR, rutPro in VARCHAR2)
as
begin
    open registro for select ID_CONTRATO, COSTO_BASE, FECHA_FIRMA, ULTIMO_PAGO, RUT_CLIENTE, RUT_PROFESIONAL  from contrato where RUT_PROFESIONAL = rutPro;
end;
/

------------------------------------------
-- Pagos
------------------------------------------

CREATE OR REPLACE PROCEDURE pago_PorIdContrato (registro out SYS_REFCURSOR, idCtr in VARCHAR2)
as
begin
    open registro for select ID_MENSUALIDAD, FECHA_LIMITE, ESTADO, COSTO, ID_CONTRATO, FECHA_PAGO, BOLETA from pago_mensualidad where ID_CONTRATO = idCtr order by fecha_limite desc;
end;
/

create or replace PROCEDURE pa_buscar_pagos (registro out SYS_REFCURSOR)
as
begin
    open registro for   select 
                        EXTRACT(YEAR FROM fecha_limite)AS AÑO,
                        to_char(fecha_limite, 'Month') AS MES,
                        SUM(COSTO) AS TOTAL_MENSUAL
                        from pago_mensualidad
                        WHERE ESTADO = 1
                        GROUP BY EXTRACT(MONTH FROM fecha_limite), EXTRACT(YEAR FROM fecha_limite),to_char(fecha_limite, 'Month')
                        ORDER BY EXTRACT(YEAR FROM fecha_limite) DESC,EXTRACT(MONTH FROM fecha_limite) DESC;
end;
/

CREATE OR REPLACE PROCEDURE pago_PorIdMensualidad (registro out SYS_REFCURSOR, idMen in NUMBER)
as
begin
    open registro for select ID_MENSUALIDAD, FECHA_LIMITE, ESTADO, COSTO, ID_CONTRATO, FECHA_PAGO, BOLETA from pago_mensualidad where ID_MENSUALIDAD=idMen;
end;
/

CREATE OR REPLACE PROCEDURE actualizarMensualidad(estado_v in NUMBER,fecha_pago_v in DATE,boleta_v in VARCHAR2,idMen in NUMBER)
as
begin
    UPDATE pago_mensualidad SET ESTADO = estado_v, FECHA_PAGO = fecha_pago_v, BOLETA = boleta_v WHERE ID_MENSUALIDAD = idMen;
end;
/

------------------------------------------
-- Checklist
------------------------------------------
CREATE OR REPLACE PROCEDURE insertarChecklist (idCtr in NUMBER)
as
begin
    insert into checklist (ID_CONTRATO) VALUES (idCtr);
end;
/

CREATE OR REPLACE PROCEDURE actualizarChecklist(elementos_v in CLOB, idCtr in NUMBER)
as
begin
    UPDATE CHECKLIST SET ELEMENTOS = elementos_v WHERE ID_CONTRATO = idCtr;
end;
/

CREATE OR REPLACE PROCEDURE checklist_PorIdContrato (registro out SYS_REFCURSOR, idCtr in VARCHAR2)
as
begin
    open registro for select ID_CHECKLIST, ELEMENTOS, ID_CONTRATO from checklist where ID_CONTRATO = idCtr;
end;
/

------------------------------------------
-- Visita
------------------------------------------
CREATE OR REPLACE PROCEDURE visita_PorId (registro out SYS_REFCURSOR,idVi in NUMBER)
as
begin
    OPEN registro for SELECT vi.ID_VISITA, vi.FECHA, vi.ESTADO, vi.UBICACION, vi.REPORTE_FINAL, vi.PERIODO, vi.ID_CONTRATO, vi.ID_COMUNA, cli.nombre_empresa FROM VISITA vi 
    INNER JOIN CONTRATO c
    ON c.id_contrato = vi.id_contrato
    INNER JOIN CLIENTES cli
    ON c.rut_cliente = cli.rut_cliente
    WHERE vi.ID_VISITA = idVi;
end;
/

CREATE OR REPLACE PROCEDURE seleccionarVisitas (registro out SYS_REFCURSOR)
as
begin
    OPEN registro for SELECT vi.ID_VISITA, vi.FECHA, vi.ESTADO, vi.UBICACION, vi.REPORTE_FINAL, vi.PERIODO, vi.ID_CONTRATO, vi.ID_COMUNA, cli.nombre_empresa FROM VISITA vi 
    INNER JOIN CONTRATO c
    ON c.id_contrato = vi.id_contrato
    INNER JOIN CLIENTES cli
    ON c.rut_cliente = cli.rut_cliente
    INNER JOIN USUARIO usr
    ON usr.id_usuario = cli.id_usuario
    WHERE usr.estado = 1
    ORDER BY vi.PERIODO desc;
end;
/

CREATE OR REPLACE PROCEDURE actualizarVisita (fecha_v in DATE, estado_v in NUMBER, ubicacion_v in VARCHAR2, reporte_final_v in VARCHAR2, periodo_v in DATE, idComuna_v in NUMBER, idVi in NUMBER)
as
begin
     UPDATE VISITA SET FECHA = fecha_v, ESTADO=estado_v, UBICACION = ubicacion_v, REPORTE_FINAL = reporte_final_v, PERIODO = periodo_v,ID_COMUNA = idComuna_v WHERE ID_VISITA = idVi;
end;
/
------------------------------------------
-- Solicitudes
------------------------------------------
CREATE OR REPLACE PROCEDURE insertarAsesoria(tipo_v in VARCHAR2,idCtr in NUMBER, fecha_publicacion_v in DATE, motivo_v in CLOB,archivo_v in VARCHAR2, tipo_asesoria_v in VARCHAR2)
as
begin
    INSERT INTO SOLICITUD (estado,tipo, id_contrato) VALUES ('PENDIENTE',tipo_v,idCtr);
    INSERT INTO ASESORIA (fecha_publicacion,motivo,id_solicitud,archivo,tipo_asesoria) VALUES (fecha_publicacion_v, motivo_v, (SELECT MAX(ID_SOLICITUD) FROM SOLICITUD),archivo_v,tipo_asesoria_v);
end;
/

CREATE OR REPLACE PROCEDURE insertarSolicitudCapacitacion(tipo_v in VARCHAR2,idCtr in NUMBER,fecha_publicacion_v in DATE, motivo_v in CLOB, archivo_v in VARCHAR2)
as
begin
    INSERT INTO SOLICITUD (estado,tipo, id_contrato) VALUES ('PENDIENTE',tipo_v,idCtr);
    INSERT INTO SOLICITUD_CAPACITACION (fecha_publicacion,motivo,archivo,id_solicitud) VALUES (fecha_publicacion_v, motivo_v, archivo_v, (SELECT MAX(ID_SOLICITUD) FROM SOLICITUD));
end;
/

CREATE OR REPLACE PROCEDURE solicitud_PorIdContrato(registroAs out SYS_REFCURSOR, registroCap out SYS_REFCURSOR, idCtr in NUMBER)
as
begin
    --Select Asesorias
    OPEN registroAs FOR SELECT ase.MOTIVO, sol.TIPO, ase.FECHA_PUBLICACION, sol.ESTADO, sol.ID_SOLICITUD, ase.ARCHIVO, cli.NOMBRE_EMPRESA
    FROM SOLICITUD sol INNER JOIN ASESORIA ase ON ase.ID_SOLICITUD = sol.ID_SOLICITUD
    JOIN CONTRATO con ON con.ID_CONTRATO = sol.ID_CONTRATO
    JOIN CLIENTES cli ON cli.RUT_CLIENTE = con.RUT_CLIENTE
    WHERE sol.ID_CONTRATO = idCtr;
    
    --Select Capacitaciones
    OPEN registroCap FOR SELECT sc.MOTIVO, sol.TIPO, sc.FECHA_PUBLICACION, sol.ESTADO, sol.ID_SOLICITUD, sc.ARCHIVO, cli.NOMBRE_EMPRESA
    FROM SOLICITUD sol INNER JOIN SOLICITUD_CAPACITACION sc ON sc.ID_SOLICITUD = sol.ID_SOLICITUD
    JOIN CONTRATO con ON con.ID_CONTRATO = sol.ID_CONTRATO
    JOIN CLIENTES cli ON cli.RUT_CLIENTE = con.RUT_CLIENTE
    WHERE sol.ID_CONTRATO = idCtr;
end;
/

CREATE OR REPLACE PROCEDURE asesoria_PorIdSolicitud(registro out SYS_REFCURSOR,idSlc in NUMBER)
as
begin
    OPEN registro FOR SELECT ase.MOTIVO, sol.TIPO, ase.FECHA_PUBLICACION, sol.ESTADO, sol.ID_SOLICITUD, ase.RESPUESTA, ase.FECHA_RESPUESTA, ase.ARCHIVO
    FROM SOLICITUD sol INNER JOIN ASESORIA ase ON ase.ID_SOLICITUD = sol.ID_SOLICITUD
    WHERE sol.ID_SOLICITUD = idSlc;
end;
/

CREATE OR REPLACE PROCEDURE solicitud_capacitacion_PorIdSolicitud(registro out SYS_REFCURSOR,idSlc in NUMBER)
as
begin
    OPEN registro FOR SELECT sc.MOTIVO, sol.TIPO, sc.FECHA_PUBLICACION, sol.ESTADO, sol.ID_SOLICITUD, sc.ARCHIVO 
    FROM SOLICITUD sol INNER JOIN SOLICITUD_CAPACITACION sc ON sc.ID_SOLICITUD = sol.ID_SOLICITUD
    WHERE sol.ID_SOLICITUD = idSlc;
end;
/
------------------------------------------
-- Actividades
------------------------------------------
create or replace procedure actividadProfContrato (registro out SYS_REFCURSOR, rutProf in VARCHAR2)
as
begin
    open registro for select 
    c.id_contrato ,
    c.rut_profesional,
    p.nombre AS ENCARGADO
    from contrato c
    join profesionales p on c.rut_profesional = p.rut_prof
    where c.rut_profesional = rutProf;
end;
/

create or replace procedure actividadProfAsesoria (registro out SYS_REFCURSOR, rutProf in VARCHAR2)
as
begin
    open registro for select 
    a.ID_ASESORIA AS ASESORIA,
    a.FECHA_PUBLICACION AS FECHA_CREACION,
    p.nombre AS NOMBRE_ENCARGADO,
    p.rut_prof AS RUT_ENCARGADO
    from ASESORIA a
    join SOLICITUD s on a.id_solicitud = s.id_solicitud
    join CONTRATO c on s.id_contrato = c.id_contrato
    join PROFESIONALES p on c.rut_profesional = p.rut_prof
    where p.rut_prof = rutProf;
end;
/

create or replace procedure actividadProfCapacitacion (registro out SYS_REFCURSOR, rutProf in VARCHAR2)
as
begin
    open registro for select 
    c.nombre as NOMBRE_CAPACITACION,
    c.fecha AS FECHA_CAPACITACION,
    c.ubicacion as UBICACION,
    co.nombre AS COMUNA,
    p.nombre as NOMBRE_ENCARGADO,
    p.rut_prof as RUT_ENCARGADO
    from CAPACITACION c
    join CONTRATO cn on c.id_contrato = cn.id_contrato
    join COMUNA co on c.id_comuna = co.id_comuna
    join PROFESIONALES p on cn.rut_profesional = p.rut_prof
    where p.rut_prof = rutProf;
    
end;
/

create or replace procedure actividadProfVisita (registro out SYS_REFCURSOR, rutProf in VARCHAR2)
as
begin
    open registro for select
    vi.fecha as FECHA,
    vi.ubicacion as UBICACION,
    co.nombre as COMUNA,
    prof.nombre as NOMBRE_PRO
    from VISITA vi
    join CONTRATO cn on vi.id_contrato = cn.id_contrato
    join COMUNA co on vi.id_comuna = co.id_comuna
    join PROFESIONALES prof on cn.rut_profesional = prof.rut_prof
    WHERE vi.fecha IS NOT NULL
    AND prof.rut_prof = rutProf;
end;
/
