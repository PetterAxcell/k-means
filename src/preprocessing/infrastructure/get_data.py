class GetData():
    def __init__(self, filename):
        self.filename = filename

    def read_data(self, filetype):
        if filetype == 'csv':
            return self.read_csv()
    
    def read_csv(self):
        '''
        This function returns a dataframe from csv file
        '''
        return pd.read_csv(self.filename, encoding='ISO-8859-1')
