import sqlite3

def initialize_database():
    try:
        with sqlite3.connect('listaanime.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE Anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                title_japanese TEXT,
                title_synonyms TEXT,
                title_english TEXT,
                type TEXT,
                episodes INTEGER,
                status TEXT,
                aired TEXT,
                airing TEXT,
                approved TEXT,
                background TEXT,
                broadcast TEXT,
                demographics TEXT,     
                explicit_genres TEXT,             
                genres TEXT,
                images TEXT,
                licensors TEXT,
                members INTEGER,
                producers TEXT,
                rank INTEGER,
                season TEXT,
                source TEXT,
                studios TEXT,
                themes TEXT,
                titles TEXT,
                trailer TEXT,
                url TEXT,
                year INTEGER,
                aired_from TEXT,
                aired_to TEXT,
                duration TEXT,
                rating TEXT,
                synopsis TEXT,
                trailer_url TEXT,
                image_url TEXT,
                large_image_url TEXT,
                small_image_url TEXT,
                mal_id INTEGER,
                popularity INTEGER,
                score REAL,
                scored_by INTEGER,
                favorites INTEGER,
                is_watched BOOLEAN
            )''')        
        conn.commit()
    except Exception as e:
        print(f"Erro ao criar a tabela no banco: {e}")

if __name__ == '__main__':
    initialize_database()