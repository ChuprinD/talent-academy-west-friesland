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

COROP = ['Kop van Noord-Holland (C)', 'Alkmaar en omgeving (C)']

DB_config = {'host': 'localhost',
             'database': 'NHN',
             'user': 'root',
             'password': '0525'
             }

Path_to_raw_data = 'Databases/csv/raw_csv'
Path_to_clean_data = 'Databases/csv/clean_csv'
Path_to_sql_database = 'Databases/sql/dump.sql'

Name_young_professionals_data_file = 'Arbeidsmarktsituatie jongeren (15 tot 27 jaar) (85820NED_01).csv'
Name_young_professionals_living_working_region_2018_2020_data_file = 'Banen van werknemers; naar geslacht, leeftijd, woon- en werkregio\'s (83658NED).csv'
Name_young_professionals_living_working_region_2021_2022_data_file = 'Woon_werkafstand_werknemers__leeftijd_26052024_185436.csv'
Name_young_professionals_living_working_region_2018_2022_data_file = 'Banen van werknemers; woon- en werkregio'
Table_plan_young_professionals = {'name': 'jongeren',
                                  'columns': {'id': 'INT PRIMARY KEY AUTO_INCREMENT',
                                              'Jaar': 'INT NOT NULL',
                                              'Regio': 'VARCHAR(100) NOT NULL',
                                              'Aantal_jongeren': 'INT NOT NULL',
                                              'Totaal_aantal_jongeren': 'INT NOT NULL'
                                              }
                                  }

Table_plan_young_professionals_work_live_region = {'name': 'jongeren_woon_en_werkregio',
                                                   'columns': {'id': 'INT PRIMARY KEY AUTO_INCREMENT',
                                                               'Jaar': 'INT NOT NULL',
                                                               'Woonregio': 'VARCHAR(100) NOT NULL',
                                                               'Werkregio': 'VARCHAR(100) NOT NULL',
                                                               'Banen': 'INT NOT NULL'
                                                               }
                                                   }