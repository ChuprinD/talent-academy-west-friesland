from src.cleaning.young_professionals import clean_young_professionals

class App:
    def __init__(self, name_young_professionals_data_file):
        
        self.name_young_professionals_data_file = name_young_professionals_data_file
        self.path_to_raw_data = 'Databases/csv/raw_csv'
        self.path_to_clean_data = 'Databases/csv/clean_csv'
        
        self.municipalities = ['Alkmaar',
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
                              'Uitgeest'] 
    
    def run(self):
        self.clean_all_data()
    
    def clean_all_data(self):
        clean_young_professionals(self.path_to_raw_data, self.path_to_clean_data,
                                  self.name_young_professionals_data_file, self.municipalities)
        
        