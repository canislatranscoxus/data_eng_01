

class Transformer:
    table = None

    def get_clean_values(self, line):
        try:
            values = line.split( ',' )
            if self.table == 'hired_employees':
                # clean date time
                values[2] = values[2].upper().replace('Z', '')

            return values

        except Exception as e:
            print( 'Transformer.get_clean_values(), error: {}'.format(e) )

    def __init__(self, table):
        self.table = table