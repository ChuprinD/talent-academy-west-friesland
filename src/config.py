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
Path_to_forecast_data = 'Databases/csv/forecast_csv'
Path_to_sql_database = 'Databases/sql/dump.sql'

Name_young_professionals_data_file = 'Arbeidsmarktsituatie jongeren (15 tot 27 jaar) (85820NED_01).csv'
Name_professionals_living_working_region_2018_2020_data_file = 'Banen van werknemers; naar geslacht, leeftijd, woon- en werkregio\'s (83658NED).csv'
Name_professionals_living_working_region_2021_2022_data_file = 'Woon_werkafstand_werknemers__leeftijd_26052024_185436.csv'
Name_young_professionals_living_working_region_2018_2022_data_file = 'Jongeren van werknemers; woon- en werkregio.csv'
Name_adult_professionals_living_working_region_2018_2022_data_file = 'Volwassene van werknemers; woon- en werkregio.csv'
Name_students_living_region_data_file = 'HBO_WO studenten; naar CROHO onderdeel (BBOROM_00003_01).csv'
Name_students_work_live_region_data_file = 'Woon-werk situatie (SSB_00031NED_02) - uitgaand.csv'
Name_forecast_young_and_adult_professionals = 'Jongeren en Volwassene professionals'
Name_forecast_students = 'HBO en WO professionals'

Table_plan_young_professionals = {'name': 'jongeren',
                                  'columns': ['id',
                                              'Jaar',
                                              'Niveau_regio',
                                              'Regio_id',
                                              'Werkende_jongeren',
                                              'Totaal_jongeren'
                                              ]
                                  }

Table_plan_young_professionals_work_live_region = {'name': 'jongeren_woon_en_werkregio',
                                                   'columns': ['id',
                                                               'Jaar',
                                                               'Niveau_regio',
                                                               'Woonregio_id',
                                                               'Werkregio_id',
                                                               'Werkende_jongeren'
                                                               ]
                                                   }

Table_plan_adult_professionals_work_live_region = {'name': 'volwassene_woon_en_werkregio',
                                                   'columns': ['id',
                                                               'Jaar',
                                                               'Niveau_regio',
                                                               'Woonregio_id',
                                                               'Werkregio_id',
                                                               'Werkende_volwassene'
                                                               ]
                                                   }

Table_plan_students_live_region = {'name': 'studenten_woonregio',
                                   'columns': ['id',
                                               'Schooljaar',
                                               'Niveau_regio',
                                               'Regio_id',
                                               'Soort_hoger_onderwijs_id',
                                               'Opleidingssector_id',
                                               'Aantal'
                                               ]
                                   }  

Table_plan_students_work_live_region = {'name': 'studenten_woon_en_werkregio',
                                        'columns': ['id',
                                                    'Diplomajaar',
                                                    'Werkregio',
                                                    'peilmoment',
                                                    'Aantal'
                                                    ]
                                        } 

Table_plan_forecast_professionals = {'name': 'prognoses_professionals',
                                     'columns': ['id',
                                                 'Jaar',
                                                 'Banen',
                                                 'Werk_in_NHN',
                                                 'Leeftijd'
                                                 ]
                                     }

Table_plan_forecast_students = {'name': 'prognoses_studenten',
                                'columns': ['id',
                                            'Schooljaar',
                                            'Aantal',
                                            'Soort_hoger_onderwijs_id'
                                            ]
                                }