--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: organization; Type: TABLE; Schema: public; Owner: umohio
--

CREATE TABLE public.organization (
    organization_id integer NOT NULL,
    name character varying(100) NOT NULL,
    tagline character varying(250),
    website character varying(100),
    email character varying(30)
);


ALTER TABLE public.organization OWNER TO umohio;

--
-- Name: organization_organization_id_seq; Type: SEQUENCE; Schema: public; Owner: umohio
--

CREATE SEQUENCE public.organization_organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organization_organization_id_seq OWNER TO umohio;

--
-- Name: organization_organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: umohio
--

ALTER SEQUENCE public.organization_organization_id_seq OWNED BY public.organization.organization_id;


--
-- Name: organization organization_id; Type: DEFAULT; Schema: public; Owner: umohio
--

ALTER TABLE ONLY public.organization ALTER COLUMN organization_id SET DEFAULT nextval('public.organization_organization_id_seq'::regclass);


--
-- Data for Name: organization; Type: TABLE DATA; Schema: public; Owner: umohio
--

COPY public.organization (organization_id, name, tagline, website, email) FROM stdin;
1	The Corporation	Here is our tagline	https://web.com	info@web.com
2	The Second Corporation	The second tagline	http://web2.com	info@web2.com
\.


--
-- Name: organization_organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: umohio
--

SELECT pg_catalog.setval('public.organization_organization_id_seq', 2, true);


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: umohio
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (organization_id);


--
-- PostgreSQL database dump complete
--

