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

-- STATIONS
CREATE TABLE public.stations (
    id_station integer NOT NULL,
    name character varying,
    descr character varying,
    id_station_type integer
);

ALTER TABLE public.stations OWNER TO vvd;

CREATE SEQUENCE public.stations_id_station_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.stations_id_station_seq OWNER TO vvd;

ALTER SEQUENCE public.stations_id_station_seq OWNED BY public.stations.id_station;

ALTER TABLE ONLY public.stations ALTER COLUMN id_station SET DEFAULT nextval('public.stations_id_station_seq'::regclass);

INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (1, 'EWSD 6', '6', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (2, 'EWSD 7', '7', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (3, 'SI2000', 'SI', 1);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (4, 'B1', 'B1', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (5, 'C1', 'C1', 8);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (6, 'A1', 'A1', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (7, 'B1', 'B1', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (8, 'C1', 'C1', 8);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (9, 'A1', 'A1', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (10, 'B1', 'B1', 2);
INSERT INTO public.stations (id_station, name, descr, id_station_type) VALUES (11, 'C1', 'C1', 8);

SELECT pg_catalog.setval('public.stations_id_station_seq', 12, true);

ALTER TABLE ONLY public.stations
    ADD CONSTRAINT stations_pkey PRIMARY KEY (id_station) INCLUDE (id_station);
