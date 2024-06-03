Last_year = 2022

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

NHN_COROP = ['Kop van Noord-Holland (C)', 'Alkmaar en omgeving (C)']
ALL_COROP = ['Alkmaar en omgeving (C)',
             'Achterhoek (C)',
             'Agglomeratie \'s-Gravenhage (C)',
             'Agglomeratie Haarlem (C)',
             'Agglomeratie Leiden en Bollenstreek (C)',
             'Alkmaar en omgeving (C)',
             'Arnhem/Nijmegen (C)',
             'Delft en Westland (C)',
             'Delfzijl en omgeving (C)',
             'Flevoland (C)',
             'Groot-Amsterdam (C)',
             'Groot-Rijnmond (C)',
             'Het Gooi en Vechtstreek (C)',
             'IJmond (C)',
             'Kop van Noord-Holland (C)',
             'Midden-Limburg (C)',
             'Midden-Noord-Brabant (C)',
             'Noord-Drenthe (C)',
             'Noord-Friesland (C)',
             'Noord-Limburg (C)',
             'Noord-Overijssel (C)',
             'Noordoost-Noord-Brabant (C)',
             'Oost-Groningen (C)',
             'Oost-Zuid-Holland (C)',
             'Overig Groningen (C)',
             'Overig Zeeland (C)',
             'Twente (C)',
             'Utrecht (C)',
             'Veluwe (C)',
             'West-Noord-Brabant (C)',
             'Zaanstreek (C)',
             'Zeeuwsch-Vlaanderen (C)',
             'Zuid-Limburg (C)',
             'Zuidoost-Drenthe (C)',
             'Zuidoost-Friesland (C)',
             'Zuidoost-Noord-Brabant (C)',
             'Zuidoost-Zuid-Holland (C)',
             'Zuidwest-Drenthe (C)',
             'Zuidwest-Friesland (C)',
             'Zuidwest-Gelderland (C)',
             'Zuidwest-Overijssel (C)'
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
Name_professionals_living_working_region_2018_2020_data_file = 'Banen van werknemers; naar geslacht, leeftijd, woon- en werkregio\'s (83658NED).csv'
Name_professionals_living_working_region_2021_2022_data_file = 'Woon_werkafstand_werknemers__leeftijd_26052024_185436.csv'
Name_young_professionals_living_working_region_2018_2022_data_file = 'Jongeren van werknemers; woon- en werkregio.csv'
Name_adult_professionals_living_working_region_2018_2022_data_file = 'Volwassene van werknemers; woon- en werkregio.csv'

Table_plan_young_professionals = {'name': 'jongeren',
                                  'columns': {'id': 'INT PRIMARY KEY AUTO_INCREMENT',
                                              'Jaar': 'INT NOT NULL',
                                              'Niveau_regio': 'ENUM(\'Gemeente\', \'Corop\') NOT NULL',                                              
                                              'Regio_id': 'INT',
                                              'Werkende_jongeren': 'INT NOT NULL',
                                              'Totaal_jongeren': 'INT NOT NULL'
                                              }
                                  }

Table_plan_young_professionals_work_live_region = {'name': 'jongeren_woon_en_werkregio',
                                                   'columns': {'id': 'INT AUTO_INCREMENT PRIMARY KEY',
                                                               'Jaar': 'INT NOT NULL',
                                                               'Niveau_regio': 'ENUM(\'Gemeente\', \'Corop\') NOT NULL',
                                                               'Woonregio_id': 'INT',
                                                               'Werkregio_id': 'INT',
                                                               'Werkende_jongeren': 'INT NOT NULL'
                                                               }
                                                   }

Table_plan_adult_professionals_work_live_region = {'name': 'volwassene_woon_en_werkregio',
                                                   'columns': {'id': 'INT AUTO_INCREMENT PRIMARY KEY',
                                                               'Jaar': 'INT NOT NULL',
                                                               'Niveau_regio': 'ENUM(\'Gemeente\', \'Corop\') NOT NULL',
                                                               'Woonregio_id': 'INT',
                                                               'Werkregio_id': 'INT',
                                                               'Werkende_volwassene': 'INT NOT NULL'
                                                               }
                                                   }