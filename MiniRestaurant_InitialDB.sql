PGDMP     4                    {            MiniRestaurant    14.7    14.7                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16558    MiniRestaurant    DATABASE     t   CREATE DATABASE "MiniRestaurant" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
     DROP DATABASE "MiniRestaurant";
                postgres    false            �            1259    16574    bahan    TABLE     �   CREATE TABLE public.bahan (
    id integer NOT NULL,
    nama_bahan character varying(128) NOT NULL,
    satuan character varying(64) NOT NULL
);
    DROP TABLE public.bahan;
       public         heap    postgres    false            �            1259    16573    bahan_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bahan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.bahan_id_seq;
       public          postgres    false    212                       0    0    bahan_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.bahan_id_seq OWNED BY public.bahan.id;
          public          postgres    false    211            �            1259    16592    bahan_resep    TABLE     �   CREATE TABLE public.bahan_resep (
    resep_id integer NOT NULL,
    bahan_id integer NOT NULL,
    jumlah numeric(10,4) NOT NULL
);
    DROP TABLE public.bahan_resep;
       public         heap    postgres    false            �            1259    16567    kategori    TABLE     h   CREATE TABLE public.kategori (
    id integer NOT NULL,
    nama_kat character varying(128) NOT NULL
);
    DROP TABLE public.kategori;
       public         heap    postgres    false            �            1259    16566    kategori_id_seq    SEQUENCE     �   CREATE SEQUENCE public.kategori_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.kategori_id_seq;
       public          postgres    false    210                       0    0    kategori_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.kategori_id_seq OWNED BY public.kategori.id;
          public          postgres    false    209            �            1259    16581    resep    TABLE     �   CREATE TABLE public.resep (
    id integer NOT NULL,
    nama_resep character varying(256) NOT NULL,
    kategori_id integer NOT NULL
);
    DROP TABLE public.resep;
       public         heap    postgres    false            �            1259    16580    resep_id_seq    SEQUENCE     �   CREATE SEQUENCE public.resep_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.resep_id_seq;
       public          postgres    false    214                       0    0    resep_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.resep_id_seq OWNED BY public.resep.id;
          public          postgres    false    213            k           2604    16577    bahan id    DEFAULT     d   ALTER TABLE ONLY public.bahan ALTER COLUMN id SET DEFAULT nextval('public.bahan_id_seq'::regclass);
 7   ALTER TABLE public.bahan ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    212    212            j           2604    16570    kategori id    DEFAULT     j   ALTER TABLE ONLY public.kategori ALTER COLUMN id SET DEFAULT nextval('public.kategori_id_seq'::regclass);
 :   ALTER TABLE public.kategori ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210            l           2604    16584    resep id    DEFAULT     d   ALTER TABLE ONLY public.resep ALTER COLUMN id SET DEFAULT nextval('public.resep_id_seq'::regclass);
 7   ALTER TABLE public.resep ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    214    214                      0    16574    bahan 
   TABLE DATA           7   COPY public.bahan (id, nama_bahan, satuan) FROM stdin;
    public          postgres    false    212   �        	          0    16592    bahan_resep 
   TABLE DATA           A   COPY public.bahan_resep (resep_id, bahan_id, jumlah) FROM stdin;
    public          postgres    false    215   �!                 0    16567    kategori 
   TABLE DATA           0   COPY public.kategori (id, nama_kat) FROM stdin;
    public          postgres    false    210   "                 0    16581    resep 
   TABLE DATA           <   COPY public.resep (id, nama_resep, kategori_id) FROM stdin;
    public          postgres    false    214   :"                  0    0    bahan_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.bahan_id_seq', 14, true);
          public          postgres    false    211                       0    0    kategori_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.kategori_id_seq', 2, true);
          public          postgres    false    209                       0    0    resep_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.resep_id_seq', 5, true);
          public          postgres    false    213            p           2606    16579    bahan bahan_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.bahan
    ADD CONSTRAINT bahan_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.bahan DROP CONSTRAINT bahan_pkey;
       public            postgres    false    212            t           2606    16596    bahan_resep bahan_resep_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.bahan_resep
    ADD CONSTRAINT bahan_resep_pkey PRIMARY KEY (resep_id, bahan_id);
 F   ALTER TABLE ONLY public.bahan_resep DROP CONSTRAINT bahan_resep_pkey;
       public            postgres    false    215    215            n           2606    16572    kategori kategori_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.kategori
    ADD CONSTRAINT kategori_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.kategori DROP CONSTRAINT kategori_pkey;
       public            postgres    false    210            r           2606    16586    resep resep_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.resep
    ADD CONSTRAINT resep_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.resep DROP CONSTRAINT resep_pkey;
       public            postgres    false    214            w           2606    16602 %   bahan_resep bahan_resep_bahan_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bahan_resep
    ADD CONSTRAINT bahan_resep_bahan_id_fkey FOREIGN KEY (bahan_id) REFERENCES public.bahan(id) ON DELETE RESTRICT;
 O   ALTER TABLE ONLY public.bahan_resep DROP CONSTRAINT bahan_resep_bahan_id_fkey;
       public          postgres    false    3184    215    212            v           2606    16597 %   bahan_resep bahan_resep_resep_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bahan_resep
    ADD CONSTRAINT bahan_resep_resep_id_fkey FOREIGN KEY (resep_id) REFERENCES public.resep(id) ON DELETE CASCADE;
 O   ALTER TABLE ONLY public.bahan_resep DROP CONSTRAINT bahan_resep_resep_id_fkey;
       public          postgres    false    214    3186    215            u           2606    16587    resep resep_kategori_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.resep
    ADD CONSTRAINT resep_kategori_id_fkey FOREIGN KEY (kategori_id) REFERENCES public.kategori(id) ON DELETE RESTRICT;
 F   ALTER TABLE ONLY public.resep DROP CONSTRAINT resep_kategori_id_fkey;
       public          postgres    false    214    3182    210               �   x�5��
�@���>�OM��2[�!زͭ���h2z	�>-�>�9��i�p�^R��ȥ�B�)A�n\���/��c{=�B{����k�@[�<h��,��8Y�B;��[tϚ��8��)�%J�t�2�mz�x���S;������bߕ�>J���_� SϿ|[�e{AK      	   q   x�M��1��bN�I���_G�t��� #q�~#�Ha!)^N%|��T��1��l;eg7!�����=���*��N��b9(�ڼ��yZ�]x$��_�ޞޞ�{�1~�c1l         %   x�3��M��Sp�/-*N�2�tI-.N-*����� �B"         N   x�3��K,�Tp�/J�K�4�2�t�L�UpO-(J��9JS2����sK8��L8]�BR3�LS�f���=... �{O     