Municipalities = ['Alkmaar',
                  'Bergen (NH.)',
                  'Castricum',
                  'Den Helder',
                  'Drechterland',
                  'Enkhuizen',
                  'Heiloo',
                  'Hollands Kroon',
                  'Hoorn',
                  'Koggenland',
                  'Medemblik',
                  'Opmeer',
                  'Schagen',
                  'Stede Broec',
                  'Texel',
                  'Uitgeest'
                  ]

DB_config = {'host': 'localhost',
             'database': 'NHN',
             'user': 'root',
             'password': '0525'
             }

Path_to_raw_data = 'Databases/csv/raw_csv'
Path_to_clean_data = 'Databases/csv/clean_csv'
Path_to_sql_database = 'Databases/sql/dump.sql'

Name_young_professionals_data_file = 'Arbeidsmarktsituatie jongeren (15 tot 27 jaar) (85820NED_01).csv'
Table_plan_young_professionals = {'name': 'jongeren',
                                  'columns': {'id': 'INT PRIMARY KEY AUTO_INCREMENT',
                                              'Jaar': 'INT NOT NULL',
                                              'Regio': 'VARCHAR(100) NOT NULL',
                                              'Aantal_jongeren': 'INT NOT NULL',
                                              'Totaal_aantal_jongeren': 'INT NOT NULL'
                                              }
                                  }