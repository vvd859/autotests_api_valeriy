CREATE USER vvd WITH PASSWORD 'qweasdzxc' SUPERUSER;

CREATE DATABASE nvgr WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';

ALTER DATABASE nvgr OWNER TO vvd;
\connect nvgr

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

SET default_tablespace = '';

SET default_table_access_method = heap;

CREATE TABLE public.station_types (
    id_station_type integer NOT NULL,
    name character varying,
    descr character varying
);

ALTER TABLE public.station_types OWNER TO postgres;

CREATE SEQUENCE public.station_types_id_station_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.station_types_id_station_type_seq OWNER TO postgres;

ALTER SEQUENCE public.station_types_id_station_type_seq OWNED BY public.station_types.id_station_type;

ALTER TABLE ONLY public.station_types ALTER COLUMN id_station_type SET DEFAULT nextval('public.station_types_id_station_type_seq'::regclass);

INSERT INTO public.station_types (id_station_type, name, descr) VALUES (1, 'SI2000', 'SI2000');
INSERT INTO public.station_types (id_station_type, name, descr) VALUES (2, 'EWSD', 'EWSD');
INSERT INTO public.station_types (id_station_type, name, descr) VALUES (3, 'Kvant', 'Kvant');
INSERT INTO public.station_types (id_station_type, name, descr) VALUES (4, 'Analog', 'Analog');
INSERT INTO public.station_types (id_station_type, name, descr) VALUES (5, 'SI3000', 'SI3000');

SELECT pg_catalog.setval('public.station_types_id_station_type_seq', 5, true);

ALTER TABLE ONLY public.station_types
    ADD CONSTRAINT station_types_name_name1_key UNIQUE (name) INCLUDE (name);

ALTER TABLE ONLY public.station_types
    ADD CONSTRAINT station_types_pkey PRIMARY KEY (id_station_type);

