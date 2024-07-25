from collections import namedtuple

# model para os dados de conexão com banco de dados.
ArtistModel = namedtuple("Artist", "id, first_name, second_name, surname, artist_id,"
                "link, created_at")
