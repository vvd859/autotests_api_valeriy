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

--
-- TOC entry 203 (class 1259 OID 16388)
-- Name: station_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.station_types (
    id_station_type integer NOT NULL,
    name character varying,
    descr character varying
);


ALTER TABLE public.station_types OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16386)
-- Name: station_types_id_station_type_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.station_types_id_station_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.station_types_id_station_type_seq OWNER TO postgres;

--
-- TOC entry 2913 (class 0 OID 0)
-- Dependencies: 202
-- Name: station_types_id_station_type_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.station_types_id_station_type_seq OWNED BY public.station_types.id_station_type;


--
-- TOC entry 2778 (class 2604 OID 16391)
-- Name: station_types id_station_type; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.station_types ALTER COLUMN id_station_type SET DEFAULT nextval('public.station_types_id_station_type_seq'::regclass);


--
-- TOC entry 2780 (class 2606 OID 16396)
-- Name: station_types station_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.station_types
    ADD CONSTRAINT station_types_pkey PRIMARY KEY (id_station_type);


-- Completed on 2021-12-15 09:21:09 UTC

--
-- PostgreSQL database dump complete
--
