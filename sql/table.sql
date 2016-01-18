--                                         Table "public.doctor_bound_info"
--      Column      |            Type             |                           Modifiers
-- -----------------+-----------------------------+----------------------------------------------------------------
--  id              | integer                     | not null default nextval('doctor_bound_info_id_seq'::regclass)
--  doctor_id       | integer                     | not null
--  phone_num       | character varying(50)       | not null
--  password        | character varying(200)      | not null
--  pwd_update_time | timestamp(6) with time zone |
--  is_login        | boolean                     | not null
--  create_time     | timestamp(6) with time zone | not null
--  is_deleted      | boolean                     | not null


insert into doctor_bound_info (doctor_id, phone_num, password, create_time, is_login, is_deleted)
select id, phone_num, password, now(), 'f', 'f'
from doctor d
where d.id = 41108;

--                                              Table "public.doctor"
--            Column           |            Type             |                      Modifiers
-- ----------------------------+-----------------------------+-----------------------------------------------------
--  id                         | integer                     | not null default nextval('doctor_id_seq'::regclass)
--  user_type                  | character varying(3)        | not null
--  sex                        | character varying(1)        |
--  password                   | character varying(200)      |
--  phone_num                  | character varying(50)       | not null default '18612345678'::character varying
--  real_name                  | character varying(200)      |
--  header_pic                 | character varying(100)      |
--  register_time              | timestamp(6) with time zone | not null
--  title_aca                  | character varying(4)        |
--  title_med                  | character varying(4)        |
--  specialty_id               | integer                     |
--  feature                    | character varying(1000)     |
--  department_id              | integer                     |
--  last_update_time           | timestamp(6) with time zone | not null
--  pwd_update_time            | timestamp(6) with time zone |
--  pwd_create_time            | timestamp(6) with time zone |
--  account_status             | character varying(3)        | not null
--  bio                        | text                        |
--  device_token               | character varying(200)      |
--  push_user_id               | character varying(200)      |
--  push_channel_id            | character varying(200)      |
--  tools                      | smallint                    |
--  hospital_id                | integer                     |
--  dept_phone                 | character varying(20)       |
--  referer                    | character varying(10)       |
--  internal_remark            | text                        |
--  phone_fee                  | smallint                    |
--  phone_fee_unit             | smallint                    |
--  registered                 | boolean                     | not null
--  link_to_id                 | integer                     |
--  last_login_time            | timestamp(6) with time zone |
--  app_version                | character varying(20)       |
--  device_type                | character varying(20)       |
--  device_id                  | character varying(50)       |
--  os                         | character varying(10)       |
--  os_version                 | character varying(10)       |
--  channel                    | character varying(10)       |
--  is_login                   | boolean                     | not null
--  last_verified_time         | timestamp(6) with time zone |
--  extra                      | character varying(10)       | not null
--  wx_openid                  | character varying(50)       | not null
--  auth_pic                   | character varying(100)      |
--  sales_id                   | integer                     |
--  auth_pic_status            | character varying(3)        | not null
--  membership_level           | character varying(3)        | not null
--  continuous_login_day_count | integer                     | not null


insert into user_gift(user_type, user_id, gift_id, amount, create_time, update_time, history_amount)
  values('PAT', 21, 1, 10, now(), now(), 0)

update user_gift set amount = 10 where id = 8;
