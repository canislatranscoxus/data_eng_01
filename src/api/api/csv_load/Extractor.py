
class Extractor:

    def get_lines(self, csv_data ):
        try:
            lines = csv_data.replace('\r', '').split('\n')

            for i in lines:
                if (len(i) == 0):
                    lines.remove(i)

            return lines
        except Exception as e:
            print('Extractor.get_lines(), error: {}'.format(e))

