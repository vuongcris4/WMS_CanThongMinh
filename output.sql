PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2025-04-03 02:00:12.611040');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2025-04-03 02:00:12.829689');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2025-04-03 02:00:13.019236');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2025-04-03 02:00:13.140132');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2025-04-03 02:00:13.255483');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2025-04-03 02:00:13.379125');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2025-04-03 02:00:13.497529');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2025-04-03 02:00:13.637561');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2025-04-03 02:00:13.757381');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2025-04-03 02:00:13.860387');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2025-04-03 02:00:13.974275');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2025-04-03 02:00:14.079471');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2025-04-03 02:00:14.195013');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2025-04-03 02:00:14.312979');
INSERT INTO django_migrations VALUES(15,'auth','0010_alter_group_name_max_length','2025-04-03 02:00:14.424262');
INSERT INTO django_migrations VALUES(16,'auth','0011_update_proxy_permissions','2025-04-03 02:00:14.540174');
INSERT INTO django_migrations VALUES(17,'auth','0012_alter_user_first_name_max_length','2025-04-03 02:00:14.683887');
INSERT INTO django_migrations VALUES(18,'material_app','0001_initial','2025-04-03 02:00:14.847629');
INSERT INTO django_migrations VALUES(19,'sessions','0001_initial','2025-04-03 02:00:15.048268');
INSERT INTO django_migrations VALUES(20,'material_app','0002_material_inventory_level','2025-04-16 11:43:02.873665');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(1,'6','g',3,'',8,1,'2025-04-03 02:41:55.960409');
INSERT INTO django_admin_log VALUES(2,'5','g',3,'',8,1,'2025-04-03 02:42:00.202047');
INSERT INTO django_admin_log VALUES(3,'4','g',3,'',8,1,'2025-04-03 02:42:04.011950');
INSERT INTO django_admin_log VALUES(4,'9','tĂªtt',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(5,'8','123',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(6,'7','123',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(7,'6','dfs',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(8,'5','test',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(9,'4','test',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(10,'3','test',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(11,'2','bu lĂ´ng',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(12,'1','á»‘c vĂ­t',3,'',7,1,'2025-04-03 03:52:54.179715');
INSERT INTO django_admin_log VALUES(13,'16','sfsdfg',3,'',7,1,'2025-04-03 03:53:07.292750');
INSERT INTO django_admin_log VALUES(14,'15','sdgdfsg',3,'',7,1,'2025-04-03 03:53:07.293253');
INSERT INTO django_admin_log VALUES(15,'14','dfsdf',3,'',7,1,'2025-04-03 03:53:07.293253');
INSERT INTO django_admin_log VALUES(16,'13','dfsdf',3,'',7,1,'2025-04-03 03:53:07.293306');
INSERT INTO django_admin_log VALUES(17,'12','dfsdf',3,'',7,1,'2025-04-03 03:53:07.293306');
INSERT INTO django_admin_log VALUES(18,'11','abchgr',3,'',7,1,'2025-04-03 03:53:07.293306');
INSERT INTO django_admin_log VALUES(19,'10','abchgr',3,'',7,1,'2025-04-03 03:53:07.293306');
INSERT INTO django_admin_log VALUES(20,'7','á»‘c vĂ­t - tĂºi',3,'',9,1,'2025-04-03 03:55:10.666388');
INSERT INTO django_admin_log VALUES(21,'6','import - á»‘c vĂ­t - 3.0 g',2,'[{"changed": {"fields": ["Quantity"]}}]',10,1,'2025-04-16 11:55:57.930853');
INSERT INTO django_admin_log VALUES(22,'6','import - á»‘c vĂ­t - 2.5 g',2,'[{"changed": {"fields": ["Quantity"]}}]',10,1,'2025-04-16 11:56:26.694252');
INSERT INTO django_admin_log VALUES(23,'6','import - á»‘c vĂ­t - 2.5 g',2,'[{"changed": {"fields": ["Base quantity"]}}]',10,1,'2025-04-16 12:00:26.431435');
INSERT INTO django_admin_log VALUES(24,'6','import - á»‘c vĂ­t - 3.0 cĂ¡i',2,'[{"changed": {"fields": ["UnitId", "Quantity"]}}]',10,1,'2025-04-16 12:00:58.180476');
INSERT INTO django_admin_log VALUES(25,'6','import - á»‘c vĂ­t - 4.0 g',2,'[{"changed": {"fields": ["UnitId", "Quantity"]}}]',10,1,'2025-04-16 12:01:09.304896');
INSERT INTO django_admin_log VALUES(26,'6','import - á»‘c vĂ­t - 4.0 g',3,'',10,1,'2025-04-16 12:01:28.767201');
INSERT INTO django_admin_log VALUES(27,'18','bu lĂ´ng',2,'[{"changed": {"fields": ["Base unitId"]}}]',7,1,'2025-04-16 12:25:42.083813');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'material_app','material');
INSERT INTO django_content_type VALUES(8,'material_app','unit');
INSERT INTO django_content_type VALUES(9,'material_app','materialunit');
INSERT INTO django_content_type VALUES(10,'material_app','materialtransactions');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_material','Can add material');
INSERT INTO auth_permission VALUES(26,7,'change_material','Can change material');
INSERT INTO auth_permission VALUES(27,7,'delete_material','Can delete material');
INSERT INTO auth_permission VALUES(28,7,'view_material','Can view material');
INSERT INTO auth_permission VALUES(29,8,'add_unit','Can add unit');
INSERT INTO auth_permission VALUES(30,8,'change_unit','Can change unit');
INSERT INTO auth_permission VALUES(31,8,'delete_unit','Can delete unit');
INSERT INTO auth_permission VALUES(32,8,'view_unit','Can view unit');
INSERT INTO auth_permission VALUES(33,9,'add_materialunit','Can add material unit');
INSERT INTO auth_permission VALUES(34,9,'change_materialunit','Can change material unit');
INSERT INTO auth_permission VALUES(35,9,'delete_materialunit','Can delete material unit');
INSERT INTO auth_permission VALUES(36,9,'view_materialunit','Can view material unit');
INSERT INTO auth_permission VALUES(37,10,'add_materialtransactions','Can add material transactions');
INSERT INTO auth_permission VALUES(38,10,'change_materialtransactions','Can change material transactions');
INSERT INTO auth_permission VALUES(39,10,'delete_materialtransactions','Can delete material transactions');
INSERT INTO auth_permission VALUES(40,10,'view_materialtransactions','Can view material transactions');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$870000$4ue7GuPoTplYdO01ec0n0f$KLjMJaOPCLxnHFE35eLPGjlbQYlUguIx5oM3fPeqWJ4=','2025-04-03 02:40:13.911331',1,'vuong','','',1,1,'2025-04-03 02:40:01.973401','');
CREATE TABLE IF NOT EXISTS "material_app_unit" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
INSERT INTO material_app_unit VALUES(1,'kg');
INSERT INTO material_app_unit VALUES(2,'cĂ¡i');
INSERT INTO material_app_unit VALUES(3,'g');
INSERT INTO material_app_unit VALUES(7,'tĂºi');
INSERT INTO material_app_unit VALUES(8,'há»™p');
CREATE TABLE IF NOT EXISTS "material_app_materialunit" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "conversion_factor" real NOT NULL, "materialId_id" bigint NOT NULL REFERENCES "material_app_material" ("id") DEFERRABLE INITIALLY DEFERRED, "unitId_id" bigint NOT NULL REFERENCES "material_app_unit" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO material_app_materialunit VALUES(4,1.0,17,2);
INSERT INTO material_app_materialunit VALUES(5,0.5,17,3);
INSERT INTO material_app_materialunit VALUES(6,0.00050000000000000001,17,1);
INSERT INTO material_app_materialunit VALUES(8,1.0,18,2);
INSERT INTO material_app_materialunit VALUES(9,50.0,18,3);
INSERT INTO material_app_materialunit VALUES(10,1.0,19,2);
INSERT INTO material_app_materialunit VALUES(11,1.0,20,2);
CREATE TABLE IF NOT EXISTS "material_app_materialtransactions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" real NOT NULL, "base_quantity" real NOT NULL, "transaction_type" varchar(10) NOT NULL, "created_at" datetime NOT NULL, "materialId_id" bigint NOT NULL REFERENCES "material_app_material" ("id") DEFERRABLE INITIALLY DEFERRED, "unitId_id" bigint NOT NULL REFERENCES "material_app_unit" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO material_app_materialtransactions VALUES(7,4.0,8.0,'import','2025-04-16 12:05:21.608257',17,3);
INSERT INTO material_app_materialtransactions VALUES(8,2.0,2.0,'export','2025-04-16 12:05:32.113736',17,2);
INSERT INTO material_app_materialtransactions VALUES(9,2.0,4.0,'import','2025-04-17 01:54:34.402786',17,3);
INSERT INTO material_app_materialtransactions VALUES(10,2.0,2.0,'import','2025-04-19 14:10:05.471251',17,2);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('edqqo8arqebidsza6fp4srhjk7me5p8x','.eJxVjMsOwiAQAP-FsyHQlcd69N5vIAsLUjVtUtqT8d-VpAe9zkzmJQLtWw17y2uYWFyEFqdfFik98twF32m-LTIt87ZOUfZEHrbJceH8vB7t36BSq33LpQAAQaRsEJwjKpZhSI6T0pC_wJIuCgmVVxY8mVLOiDh4RHZGvD_zije5:1u0AV4:hNtF8e5FJXTLEiLYOOMDb2afCUGqQluTGaEgRstCRGM','2025-04-17 02:40:14.022149');
CREATE TABLE IF NOT EXISTS "material_app_material" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "base_unitId_id" bigint NOT NULL REFERENCES "material_app_unit" ("id") DEFERRABLE INITIALLY DEFERRED, "inventory_level" real NOT NULL);
INSERT INTO material_app_material VALUES(17,'á»‘c vĂ­t',2,12.0);
INSERT INTO material_app_material VALUES(18,'bu lĂ´ng',3,0.0);
INSERT INTO material_app_material VALUES(19,'tĂºi zip',2,0.0);
INSERT INTO material_app_material VALUES(20,'bĂ¬ nilon',2,0.0);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',20);
INSERT INTO sqlite_sequence VALUES('django_admin_log',27);
INSERT INTO sqlite_sequence VALUES('django_content_type',10);
INSERT INTO sqlite_sequence VALUES('auth_permission',40);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('material_app_unit',8);
INSERT INTO sqlite_sequence VALUES('material_app_materialunit',11);
INSERT INTO sqlite_sequence VALUES('material_app_materialtransactions',10);
INSERT INTO sqlite_sequence VALUES('material_app_material',20);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "material_app_materialunit_materialId_id_3b150f9c" ON "material_app_materialunit" ("materialId_id");
CREATE INDEX "material_app_materialunit_unitId_id_c1815c05" ON "material_app_materialunit" ("unitId_id");
CREATE INDEX "material_app_materialtransactions_materialId_id_19d26e7f" ON "material_app_materialtransactions" ("materialId_id");
CREATE INDEX "material_app_materialtransactions_unitId_id_d55d8c13" ON "material_app_materialtransactions" ("unitId_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "material_app_material_base_unitId_id_9a5ed5e3" ON "material_app_material" ("base_unitId_id");
COMMIT;
