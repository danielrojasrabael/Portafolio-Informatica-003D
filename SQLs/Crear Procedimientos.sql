-----------------------------------------
-- Procedimientos gestion de Usuario
-----------------------------------------
-- Ingresar Usuarios
-----------------------------------------
CREATE OR REPLACE PROCEDURE insertarUsuario (pass in VARCHAR2,tipo in Varchar2, id_comu in Number, direc in VARCHAR2)
as
begin
    insert into USUARIO (contrase�a,tipo,id_comuna,direccion) VALUES (pass,tipo,id_comu,direc);
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
        open registro for select ID_USUARIO ,"CONTRASE�A" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario ORDER BY id_usuario;
    else
        open registro for select ID_USUARIO ,"CONTRASE�A" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario ORDER BY estado desc;
    end if;
end;
/

CREATE OR REPLACE PROCEDURE usuario_PORID (registro out SYS_REFCURSOR, idUsr in NUMBER)
as
begin
    open registro for select ID_USUARIO ,"CONTRASE�A" ,TIPO ,ID_COMUNA ,DIRECCION ,ESTADO  from usuario where id_usuario = idUsr;
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

CREATE OR REPLACE PROCEDURE actualizarUsuario(id_usr in number, contrase�a in varchar2, tipo in varchar2, IdComuna in number, direccion in varchar2, estado in number)
as
    vid number := id_usr;
    vpass varchar(999) := contrase�a;
    vtipo varchar2(20) := tipo;
    vcomuna number := IdComuna;
    vdireccion varchar2(100) := direccion;
    vestado number := estado;
begin
    update usuario set CONTRASE�A = vpass, TIPO = vtipo, ID_COMUNA = vcomuna, DIRECCION = vdireccion, ESTADO = vestado where ID_USUARIO = id_usr;
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

create or replace PROCEDURE insertarCapacitacion (nom in VARCHAR2,ubi in VARCHAR2, estado in VARCHAR2, fecha in DATE, id_cont in NUMBER, id_com in NUMBER)
as
begin

    insert into capacitacion (nombre,ubicacion,estado,fecha,id_contrato,id_comuna) VALUES (nom,ubi,estado,fecha,id_cont,id_com);
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