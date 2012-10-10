#!/usr/env/python

class MedalTable(object):
    def generate(self, results):
        """
        Return list of medal counts
        """
        #MEDAL_MAP = ['gold', 'silver', 'bronze']
        countries = {}
        for result in results:
            standings = result.split(' ')
            for pos, country in enumerate(standings):
                #medal = MEDAL_MAP[pos]
                if not country in countries:
                    #countries[country] = {
                    #        'gold': 0,
                    #        'silver': 0,
                    #        'bronze': 0,
                    #        }
                    countries[country] = [0,0,0]
                countries[country][pos] += 1

        medal_table = []
        for country, medals in countries.items():
            entry = str(country)
            for medal in medals:
                entry += ' %s' % medal
            medal_table.append(entry)

        return medal_table

