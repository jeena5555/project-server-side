--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-10-15 10:40:59 +07

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3750 (class 0 OID 18945)
-- Dependencies: 222
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'Manager');
INSERT INTO public.auth_group (id, name) VALUES (2, 'Cashier');


--
-- TOC entry 3752 (class 0 OID 18953)
-- Dependencies: 224
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (1, 2, 36);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (2, 2, 41);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (3, 2, 44);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (4, 2, 45);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (5, 2, 48);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (6, 1, 13);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (7, 1, 14);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (8, 1, 15);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (9, 1, 16);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (10, 1, 25);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (11, 1, 26);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (12, 1, 27);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (13, 1, 28);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (14, 1, 29);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (15, 1, 30);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (16, 1, 31);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (17, 1, 32);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (18, 1, 33);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (19, 1, 34);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (20, 1, 35);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (21, 1, 36);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (22, 1, 40);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (23, 1, 44);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (24, 1, 48);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (25, 1, 49);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (26, 1, 50);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (27, 1, 51);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (28, 1, 52);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (29, 2, 40);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (30, 2, 37);


--
-- TOC entry 3748 (class 0 OID 18939)
-- Dependencies: 220
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add employee', 7, 'add_employee');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change employee', 7, 'change_employee');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete employee', 7, 'delete_employee');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view employee', 7, 'view_employee');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add category', 8, 'add_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change category', 8, 'change_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete category', 8, 'delete_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view category', 8, 'view_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add menu', 9, 'add_menu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change menu', 9, 'change_menu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete menu', 9, 'delete_menu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view menu', 9, 'view_menu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add order', 10, 'add_order');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change order', 10, 'change_order');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete order', 10, 'delete_order');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view order', 10, 'view_order');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add order menu', 11, 'add_ordermenu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change order menu', 11, 'change_ordermenu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete order menu', 11, 'delete_ordermenu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view order menu', 11, 'view_ordermenu');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add payment', 12, 'add_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change payment', 12, 'change_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete payment', 12, 'delete_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view payment', 12, 'view_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add category', 13, 'add_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change category', 13, 'change_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete category', 13, 'delete_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view category', 13, 'view_category');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add schedule', 14, 'add_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change schedule', 14, 'change_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete schedule', 14, 'delete_schedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view schedule', 14, 'view_schedule');


--
-- TOC entry 3754 (class 0 OID 18959)
-- Dependencies: 226
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (17, 'pbkdf2_sha256$870000$psTCHd2jYSbas4DWcP2Bu0$gi2YDlR8LiahR6009ljZ4mfh3fDUiRYaTTFBKkV0gXw=', '2024-10-12 17:17:50.068874+07', true, 'admin', '', '', '', true, true, '2024-10-06 23:06:25.736382+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (16, 'pbkdf2_sha256$870000$a2gruYEH9spTXF7ED0QOSJ$EEXNfrV7LqcxI+s+TMRwCorYPFRuIw6V8tiXBPJ1JTA=', NULL, false, 'Punch', '', '', '', false, true, '2024-10-06 20:50:46.394856+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (18, 'pbkdf2_sha256$870000$1JS1OvJqalNMjsayaqQYBo$HyqkQ9ALc3oj1SkdkqtrTNGLe3nBkLzTFp2Og0wF6vI=', NULL, false, 'Drakrit', '', '', '', false, true, '2024-10-14 17:43:27.685537+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (15, 'pbkdf2_sha256$870000$82dv5LGj7WyyiLfvknRpud$SpcwDV8THI41M3jCFWymCH+z2ofF+oQunbZ26Ss6gdo=', '2024-10-14 22:14:48.617888+07', false, 'Tanggy', '', '', '', false, true, '2024-10-05 15:20:56+07');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (14, 'pbkdf2_sha256$870000$LjRIXOjuINDdLw9e3jQKUL$nIK+qxKxGFt5BJUqBpA9hLJgn+a3ulDzRWmV4cyM/Eg=', '2024-10-15 00:53:49.40617+07', false, 'jeena', '', '', '', false, true, '2024-10-05 15:19:00.270382+07');


--
-- TOC entry 3756 (class 0 OID 18967)
-- Dependencies: 228
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (11, 14, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (12, 15, 2);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (14, 16, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (15, 18, 2);


--
-- TOC entry 3758 (class 0 OID 18973)
-- Dependencies: 230
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3760 (class 0 OID 19031)
-- Dependencies: 232
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2024-10-06 23:07:24.186807+07', '3', 'Customer', 3, '', 3, 17);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2024-10-06 23:11:16.567847+07', '2', 'Cashire', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 17);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2024-10-06 23:13:10.727411+07', '1', 'Manager', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 17);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (4, '2024-10-07 00:00:11.410653+07', '2', 'Cashire', 2, '[{"changed": {"fields": ["Permissions"]}}]', 3, 17);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (5, '2024-10-08 01:48:42.757538+07', '15', 'Tanggy', 2, '[]', 4, 17);


--
-- TOC entry 3746 (class 0 OID 18931)
-- Dependencies: 218
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'employees', 'employee');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'menu', 'category');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'menu', 'menu');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'order', 'order');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'order', 'ordermenu');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'order', 'payment');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'inventory', 'category');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'schedule', 'schedule');


--
-- TOC entry 3744 (class 0 OID 18923)
-- Dependencies: 216
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2024-09-24 15:02:20.056031+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2024-09-24 15:02:20.129101+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2024-09-24 15:02:20.143547+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-09-24 15:02:20.146552+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-09-24 15:02:20.149709+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2024-09-24 15:02:20.155339+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2024-09-24 15:02:20.157902+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2024-09-24 15:02:20.160681+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'auth', '0004_alter_user_username_opts', '2024-09-24 15:02:20.163116+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2024-09-24 15:02:20.165871+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2024-09-24 15:02:20.166351+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2024-09-24 15:02:20.168456+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2024-09-24 15:02:20.188693+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2024-09-24 15:02:20.191912+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2024-09-24 15:02:20.195142+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'auth', '0011_update_proxy_permissions', '2024-09-24 15:02:20.197526+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2024-09-24 15:02:20.20029+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'employees', '0001_initial', '2024-09-24 15:02:20.208109+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'inventory', '0001_initial', '2024-09-24 15:02:20.211025+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'menu', '0001_initial', '2024-09-24 15:02:20.219539+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'order', '0001_initial', '2024-09-24 15:02:20.252221+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'sessions', '0001_initial', '2024-09-24 15:02:20.261664+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'menu', '0002_menu_category', '2024-09-25 10:16:14.924807+07');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'schedule', '0001_initial', '2024-10-14 22:24:30.15301+07');


--
-- TOC entry 3775 (class 0 OID 19137)
-- Dependencies: 247
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('q9lun2ibmyzap74hegxpwb8k8k56ena4', 'e30:1st8kZ:TvdClNPKUUuTudOhJ5uXRLeK78COjBP8EwpV7wVy7Y0', '2024-10-08 23:50:55.279507+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('cfefg97x7wtyha1an552djdezup7ozs0', 'e30:1st8mX:1YvRpfhVx7HnX-Ht1vTOAdxIlzcY7yOuoLDHzduY5a4', '2024-10-08 23:52:57.502806+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('hm4rxixhra3kgnfb1xdq57jll1jxv4sb', '.eJxVjEEOwiAQRe_C2hCGghSX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERYMTpdySMj1R3wnestyZjq-syk9wVedAup8bpeT3cv4OCvXxrBcYOxjtPSaMH7weIXuVR28xotMrZDshn48ZIQAqBHWIkdqxztATi_QHujDhX:1t0MpK:9H3k1LT97pvNBFGuzkJQ5d6xhxW3mWbhF1Of67xGp2M', '2024-10-28 22:17:42.91494+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('crqaeltodsxahb0h0i96rixavbhgapp5', '.eJxVjEEOwiAQRe_C2hCGghSX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERYMTpdySMj1R3wnestyZjq-syk9wVedAup8bpeT3cv4OCvXxrBcYOxjtPSaMH7weIXuVR28xotMrZDshn48ZIQAqBHWIkdqxztATi_QHujDhX:1sxqC6:Sz2xOL2_KMdMZ4JLgOzdKFHPgfnAJaq10t_FQDkdXQs', '2024-10-21 23:02:46.193929+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('j242rgl753zvs4flm1ee45q7xxp7tlml', '.eJxVjEEOwiAQRe_C2hCGghSX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERYMTpdySMj1R3wnestyZjq-syk9wVedAup8bpeT3cv4OCvXxrBcYOxjtPSaMH7weIXuVR28xotMrZDshn48ZIQAqBHWIkdqxztATi_QHujDhX:1t0PGP:W0q_jFaKGhiMHt2y2bQBsBY9K_F3G2VxZ3uNlucCFJc', '2024-10-29 00:53:49.420226+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('zf09fdkofc54awynfq5yjffq9zawyj6u', '.eJxVjEEOwiAQRe_C2pAZCFRcuvcMZBgGqRqalHZlvLtt0oVu33v_v1Wkdalx7TLHMauLQnX6ZYn4KW0X-UHtPmme2jKPSe-JPmzXtynL63q0fweVet3WxnPCYAN5cVggezkXG7h4cCBcKFAyqRiy1gTnIA_IGzGIwDA4S-rzBe3TN-M:1st8vZ:LfM9RCc1cTt1OxsMqLM_zglLCrvckdGDDx0mOMvDjIQ', '2024-10-09 00:02:17.169303+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('jujghwocdyjy25pi73kyslptov4apxs1', '.eJxVjEEOwiAQRe_C2pAZCFRcuvcMZBgGqRqalHZlvLtt0oVu33v_v1Wkdalx7TLHMauLQnX6ZYn4KW0X-UHtPmme2jKPSe-JPmzXtynL63q0fweVet3WxnPCYAN5cVggezkXG7h4cCBcKFAyqRiy1gTnIA_IGzGIwDA4S-rzBe3TN-M:1suVeY:MO16XAeNCr6AMCHqWX2Ax7X2ObseNDOte0f8jsbphuI', '2024-10-12 18:30:22.859403+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('kjlihseqpc8uuxgb1hawkabeoa3sq4i5', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1sxssW:Yo9mxBKhCw8z5WIj6mr87jySj_n9ojFgi7z2M2g99sM', '2024-10-22 01:54:44.23698+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('xi9g0wx9ts7kpg6lpcasaq6rw8bk4n80', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1syZFP:FDNAA0BR4ygrjtoOK9nrrCVbY9G2ySLL2fD04Jgo__E', '2024-10-23 23:09:11.547824+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('nrj5zeprjzjp5iqpgzwqm94q9w7g3qcb', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1szZCn:XgsotMO957QZcaCWHxI6mzSyT7N89ZPeXGRYuUXZINU', '2024-10-26 17:18:37.901531+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('zp68fnt9c1de2j17laq7s4vem9ispqvk', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1szZHM:5IfANYCQud66jOqov7DlM8n9DHlPfQsQsrPbVTJeDlA', '2024-10-26 17:23:20.990543+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('f0w9jrt7hsff4ox5sscsqs7zrdz8aq5s', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1szeGo:10LWBPV3eOA2ZiW9kswQ1dWDXyal9jUjtsDc6mNBB9w', '2024-10-26 22:43:06.676879+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('zyrcc6qm57fq62268nugt6w447eyllh8', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1t01TN:ej8SH4WaVop7OBcT0Wi5820ri4mAjh-7eMemZ7L3O0E', '2024-10-27 23:29:37.829085+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('alctpdu86jm2ukrqo408t8qdebcszlek', '.eJxVjEEOwiAQRe_C2hCGghSX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERYMTpdySMj1R3wnestyZjq-syk9wVedAup8bpeT3cv4OCvXxrBcYOxjtPSaMH7weIXuVR28xotMrZDshn48ZIQAqBHWIkdqxztATi_QHujDhX:1t0Gqy:zHFZLfQ40gh13doeUlTG-YswEPLST1_9xmM-kmArLFk', '2024-10-28 15:55:00.294787+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('mwjw75d1vfdh8z4nm3po2xsnlzkey7hl', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1t01Zq:jM8lXjeevS6wkcSP-2qIEcs-cRS9ctrN82X7JGJTUl0', '2024-10-27 23:36:18.630974+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('40gy7bfcss2k2adpeydipv052p4pd8b6', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1t01yU:gwp5I-fiMi4eyTKaAWmCgAVQjEFY0Lr03BVnN3uCV5E', '2024-10-28 00:01:46.846738+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('k4gfoxjld82gopshpul952ee9fyqz4ll', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1t0CZ7:yNJNPV3BagpBA2Lft8e8rm8ST4WwUV-5ZYVluXQf9-Y', '2024-10-28 11:20:17.317105+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('x3rmouln42ekvtvwqwo7fq6pxp6l3vxj', '.eJxVjMsOwiAQRf-FtSEMDqXj0n2_oQFmkKqBpI-V8d-1SRe6veec-1Jj2NYybovM48TqosCp0-8YQ3pI3QnfQ701nVpd5ynqXdEHXfTQWJ7Xw_07KGEp39pmj-i9i50PRNKTiDFEbA0yGwuIQOK6M0abHQROUQCt6QEzGcis3h_mTzdL:1t0D7X:_wpiFgY-4A1f_5NtVz326FlwRs6JQkQXEMxmBgz6lls', '2024-10-28 11:55:51.045552+07');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('m7n4y78sq3y4he1dqpgsbxllu1neu3f5', '.eJxVjDsOwjAQBe_iGllZ2-sPJX3OYK0_wQFkS3FSIe5OIqWA9s3MezNP21r81vPi58SuDJBdfsdA8ZnrQdKD6r3x2Oq6zIEfCj9p52NL-XU73b-DQr3stUqBnFBOC2GdFRJRYFQQJ4pKIiSQCgzINCFFpwYLKNEIbezeDEEH9vkC0uY2VQ:1sxVai:L8ALC9FUOX1JSAZyYmiQxog81bac8PFOo36tias-HT8', '2024-10-21 01:02:48.588459+07');


--
-- TOC entry 3762 (class 0 OID 19060)
-- Dependencies: 234
-- Data for Name: employees_employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.employees_employee (id, first_name, last_name, gender, birth_date, hire_date, contact_number, salary, account_id) VALUES (13, 'Tanggy', 'Haaha', 'M', '2024-10-01', '2024-10-02', '0952513965', 100000.00, 15);
INSERT INTO public.employees_employee (id, first_name, last_name, gender, birth_date, hire_date, contact_number, salary, account_id) VALUES (1, 'Jeena', 'Kerdakaerw', 'F', '2003-08-05', '2024-10-04', '0920736870', 100000.00, 14);
INSERT INTO public.employees_employee (id, first_name, last_name, gender, birth_date, hire_date, contact_number, salary, account_id) VALUES (14, 'Peam', 'Kerdkaew', 'Female', '2024-10-03', '2024-10-03', '0952513965', 100000.00, 16);
INSERT INTO public.employees_employee (id, first_name, last_name, gender, birth_date, hire_date, contact_number, salary, account_id) VALUES (15, 'Drakrit', 'North', 'M', '2024-10-01', '2024-10-14', '0981127654', 100000.00, 18);

-- Schedule ตารางเวลา
INSERT INTO public.schedule_schedule (id, employee_id, date, status, created_at)
VALUES
(1, 13, '2024-10-15', 'OPEN', NOW()),
(2, 1, '2024-10-15', 'FULL', NOW()),
(3, 14, '2024-10-17', 'CLOSED', NOW()),
(4, 15, '2024-10-18', 'OPEN', NOW()),
(5, 1, '2024-10-19', 'FULL', NOW());


--
-- TOC entry 3764 (class 0 OID 19073)
-- Dependencies: 236
-- Data for Name: inventory_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.inventory_category (id, name, price, quantity) VALUES (3, 'water', 100.00, 2);
INSERT INTO public.inventory_category (id, name, price, quantity) VALUES (1, 'mlik', 100.00, 3);
INSERT INTO public.inventory_category (id, name, price, quantity) VALUES (2, 'Cup', 80.00, 3);
INSERT INTO public.inventory_category (id, name, price, quantity) VALUES (4, 'Lemon', 5.00, 30);


--
-- TOC entry 3766 (class 0 OID 19079)
-- Dependencies: 238
-- Data for Name: menu_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.menu_category (id, name) VALUES (1, 'Hot Coffee');
INSERT INTO public.menu_category (id, name) VALUES (2, 'Iced Coffee');
INSERT INTO public.menu_category (id, name) VALUES (3, 'Hot Tea');
INSERT INTO public.menu_category (id, name) VALUES (4, 'Iced Tea');
INSERT INTO public.menu_category (id, name) VALUES (5, 'Smoothies');
INSERT INTO public.menu_category (id, name) VALUES (6, 'Frappe');
INSERT INTO public.menu_category (id, name) VALUES (7, 'Juices');
INSERT INTO public.menu_category (id, name) VALUES (8, 'Sodas');
INSERT INTO public.menu_category (id, name) VALUES (9, 'Other Hot Baverage');
INSERT INTO public.menu_category (id, name) VALUES (10, 'Other Cold Baverage');
INSERT INTO public.menu_category (id, name) VALUES (11, 'Dessert');


--
-- TOC entry 3768 (class 0 OID 19085)
-- Dependencies: 240
-- Data for Name: menu_menu; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (1, 'Americano', 'Espresso with hot water, a classic choice for coffee lovers.', 80.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (2, 'Cappuccino', 'Espresso with steamed milk and a layer of foam on top.', 90.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (3, 'Latte', 'A smooth blend of espresso and steamed milk.', 95.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (4, 'Mocha', 'A delicious combination of espresso, chocolate, and steamed milk.', 100.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (5, 'Caramel Macchiato', 'Espresso with steamed milk and caramel drizzle.', 110.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (6, 'Matcha Latte', 'A creamy blend of premium matcha and milk.', 120.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (8, 'Iced Latte', 'Espresso with cold milk, served over ice.', 95.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (9, 'Iced Matcha Latte', 'Premium matcha blended with cold milk and ice.', 125.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (10, 'Hot Chocolate', 'Rich and creamy hot chocolate, perfect for a cozy day.', 90.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (11, 'Iced Chocolate', 'Cold, refreshing chocolate drink, served over ice.', 95.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (14, 'Mango Smoothie', 'Fresh mango blended with ice and a touch of honey.', 120.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (16, 'Blueberry Smoothie', 'Rich and creamy blueberry smoothie.', 135.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (18, 'Thai Milk Tea', 'Traditional Thai milk tea with a hint of spice and sweetness.', 75.00, 1);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (7, 'Iced Americano', 'Espresso with cold water, served over ice.', 85.00, 3);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (12, 'Lemon Tea', 'Refreshing lemon tea with a hint of sweetness.', 70.00, 6);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (13, 'Peach Iced Tea', 'Sweet and refreshing peach iced tea.', 80.00, 2);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (15, 'Strawberry Smoothie', 'Delicious strawberry smoothie with a hint of sweetness.', 130.00, 5);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (17, 'Green Tea Frappe', 'Blended green tea with milk and ice, topped with whipped cream.', 140.00, 4);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (19, 'Iced Thai Milk Tea', 'Chilled Thai milk tea, perfect for a hot day.', 80.00, 7);
INSERT INTO public.menu_menu (id, name, description, price, category_id) VALUES (20, 'Chai Latte', 'Spiced tea latte with a blend of aromatic spices.', 100.00, 8);


--
-- TOC entry 3770 (class 0 OID 19093)
-- Dependencies: 242
-- Data for Name: order_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (41, 180.00, '2024-10-06', '07:04:10.042367', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (42, 180.00, '2024-10-06', '07:07:23.037339', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (43, 80.00, '2024-10-06', '07:08:13.644428', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (44, 170.00, '2024-10-06', '07:11:31.277843', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (45, 140.00, '2024-10-06', '14:16:02.335884', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (46, 80.00, '2024-10-06', '14:16:55.846746', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (47, 240.00, '2024-10-06', '14:47:54.464312', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (48, 100.00, '2024-10-06', '16:37:11.020753', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (40, 100.00, '2024-10-05', '11:55:10.198209', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (49, 90.00, '2024-10-06', '22:46:22.710984', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (50, 180.00, '2024-10-08', '10:54:54.304702', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (51, 100.00, '2024-10-12', '17:23:41.450185', 14);
INSERT INTO public.order_order (id, amount, order_date, order_time, employee_id) VALUES (52, 180.00, '2024-10-12', '17:24:02.376209', 14);


--
-- TOC entry 3772 (class 0 OID 19099)
-- Dependencies: 244
-- Data for Name: order_ordermenu; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (53, 1, 4, 40);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (54, 2, 2, 41);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (55, 2, 2, 42);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (56, 1, 1, 43);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (57, 1, 17, 45);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (58, 1, 1, 46);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (59, 1, 1, 47);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (60, 1, 7, 47);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (61, 1, 18, 47);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (62, 1, 20, 48);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (63, 1, 2, 49);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (64, 1, 1, 50);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (65, 1, 4, 50);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (66, 1, 4, 51);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (67, 1, 4, 52);
INSERT INTO public.order_ordermenu (id, quantity, menu_id, order_id) VALUES (68, 1, 1, 52);


--
-- TOC entry 3774 (class 0 OID 19105)
-- Dependencies: 246
-- Data for Name: order_payment; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (26, 100.00, 'Card', '2024-10-06', '06:55:10.242269', 40);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (27, 180.00, 'QR Code', '2024-10-06', '07:04:10.058588', 41);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (28, 180.00, 'Card', '2024-10-06', '07:07:23.048638', 42);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (29, 80.00, 'Cash', '2024-10-06', '07:08:13.655891', 43);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (30, 140.00, 'Card', '2024-10-06', '14:16:02.335884', 45);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (31, 80.00, 'Card', '2024-10-06', '14:16:55.846746', 46);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (32, 240.00, 'Card', '2024-10-06', '14:47:54.464312', 47);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (33, 100.00, 'Card', '2024-10-06', '16:37:11.020753', 48);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (34, 90.00, 'Cash', '2024-10-06', '22:46:22.710984', 49);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (35, 180.00, 'Cash', '2024-10-08', '01:54:54.304702', 50);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (36, 100.00, 'QR Code', '2024-10-12', '17:23:41.450185', 51);
INSERT INTO public.order_payment (id, amount, payment_method, payment_date, payment_time, order_id) VALUES (37, 180.00, 'Cash', '2024-10-12', '17:24:02.376209', 52);


--
-- TOC entry 3777 (class 0 OID 20032)
-- Dependencies: 249
-- Data for Name: schedule_schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3783 (class 0 OID 0)
-- Dependencies: 221
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3784 (class 0 OID 0)
-- Dependencies: 223
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 30, true);


--
-- TOC entry 3785 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);


--
-- TOC entry 3786 (class 0 OID 0)
-- Dependencies: 227
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 15, true);


--
-- TOC entry 3787 (class 0 OID 0)
-- Dependencies: 225
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 18, true);


--
-- TOC entry 3788 (class 0 OID 0)
-- Dependencies: 229
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3789 (class 0 OID 0)
-- Dependencies: 231
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 5, true);


--
-- TOC entry 3790 (class 0 OID 0)
-- Dependencies: 217
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- TOC entry 3791 (class 0 OID 0)
-- Dependencies: 215
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);


--
-- TOC entry 3792 (class 0 OID 0)
-- Dependencies: 233
-- Name: employees_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employees_employee_id_seq', 15, true);


--
-- TOC entry 3793 (class 0 OID 0)
-- Dependencies: 235
-- Name: inventory_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventory_category_id_seq', 4, true);


--
-- TOC entry 3794 (class 0 OID 0)
-- Dependencies: 237
-- Name: menu_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.menu_category_id_seq', 11, true);


--
-- TOC entry 3795 (class 0 OID 0)
-- Dependencies: 239
-- Name: menu_menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.menu_menu_id_seq', 20, true);


--
-- TOC entry 3796 (class 0 OID 0)
-- Dependencies: 241
-- Name: order_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_order_id_seq', 52, true);


--
-- TOC entry 3797 (class 0 OID 0)
-- Dependencies: 243
-- Name: order_ordermenu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_ordermenu_id_seq', 68, true);


--
-- TOC entry 3798 (class 0 OID 0)
-- Dependencies: 245
-- Name: order_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_payment_id_seq', 37, true);


--
-- TOC entry 3799 (class 0 OID 0)
-- Dependencies: 248
-- Name: schedule_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.schedule_schedule_id_seq', 1, false);


-- Completed on 2024-10-15 10:40:59 +07

--
-- PostgreSQL database dump complete
--

