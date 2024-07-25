
# Cria a tabela artists se não existir
create_pipeline_db_table_query = '''CREATE TABLE IF NOT EXISTS artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    surname VARCHAR(255),
    artist_id BIGINT,
    link VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);'''