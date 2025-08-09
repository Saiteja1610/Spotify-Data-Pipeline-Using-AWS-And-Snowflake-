Create database spotify_db;

create or replace storage integration s3_init
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN ='arn:aws:iam::588642315234:role/snowflake_spotify_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://spotify-etl-saiteja')
  COMMENT = 'Creating s3 connection'

  desc integration s3_init


  create or replace file format csv_file
  type = csv
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  field_delimiter = ','
  skip_header = 1
  null_if = ('NULL' , 'null')
  empty_field_as_null = true
  ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE

  create or replace stage spotify_stage
  URL = 's3://spotify-etl-saiteja/Transformation_data/'
  STORAGE_INTEGRATION = s3_init
  FILE_FORMAT = csv_file
  


  list @spotify_stage

  CREATE OR REPLACE TABLE album_tbl (
    album_id STRING,
    album_name STRING,
    release_date DATE,
    total_tracks INT,
    url STRING
);

  
  create or replace table artist_tbl(
       artist_id  STRING,
       name  STRING,
       url STRING
  );

  
  create or replace table song_tbl(
       song_id  STRING,
       song_name  STRING,
       duration_ms  DATE,
       url STRING,
       popularity INT,
       sond_added DATE,
       album_id STRING,
       artist_id STRING
  )

  copy into song_tbl
  from @spotify_stage/songs/songs_transformed_2025-08-09/run-1754744024969-part-r-00000

  copy into artist_tbl
  from @spotify_stage/artist/artist_transformed_2025-08-09/run-1754744020737-part-r-00000

  copy into album_tbl
  from @spotify_stage/album/album_transformed_2025-08-09/run-1754744008985-part-r-00000
FILE_FORMAT = (FORMAT_NAME = csv_file)
ON_ERROR = 'ABORT_STATEMENT';

create or replace schema pipe;

create or replace pipe spotify_db.pipe.song_tbl_pipe
auto_ingest = true
AS 
COPY into spotify_db.public.song_tbl from @spotify_stage/songs/

create or replace pipe spotify_db.pipe.artist_tbl_pipe
auto_ingest = true
AS 
COPY into spotify_db.public.artist_tbl from @spotify_stage/artist/

create or replace pipe spotify_db.pipe.album_tbl_pipe
auto_ingest = true
AS 
COPY into spotify_db.public.album_tbl from @spotify_stage/album/

DESC pipe pipe.artist_tbl_pipe

select SYSTEM$PIPE_STATUS('pipe album_tbl_pipe')


  
  