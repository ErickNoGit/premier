#
#   Python 3.12.1
#

import os
import pandas as pd
from treat import Treat

SRC = str(os.path.dirname(__file__))
_LEAGUE = str(os.path.join(SRC, 'league'))
_TXT_TEST = str(os.path.join(_LEAGUE, 'testOutput.txt'))
_CLUBS_ = str(os.path.join(_LEAGUE, 'clubs.txt'))
# _TABLES_TEST_ = str(os.path.join(SRC, 'league', '_tables_test'))
# _TABLES_TEST_ = str(os.path.join(SRC, 'league', '_tables_test', '2023_test.html'))
_TABLES_HTML_ = str(os.path.join(SRC, 'league', 'tables_html'))

if __name__ == '__main__':
    treat = Treat()
    dados = treat.read_dir_html(_TABLES_HTML_)
    # dados = treat.read_html(_TABLES_TEST_)
    dados = treat.clean_text(dados)
    dados = treat.modif(dados, ' Previous Position ', ' position_')
    alvo = ' Visit Club Page Compare against another team '
    dados = treat.get_part_text(dados, ' More 1 ', '*')
    dados = treat.modif(dados, alvo, ' | ')
    dados = treat.modif(dados, 'More ', ' | ')
    dados = treat.modif(dados, '*', '')
    dados = treat.modif(dados, ' | ', '\n')
    dados = treat.modif(dados, 'Latest Result:', 'ultimo_resultado')
    dados = treat.modif(dados, 'Latest Result : ', 'ultimo_resultado ')
    dados = treat.re_replace(dados, r'\s(\d)\s-\s(\d)\s', r' \1-\2 ')

    with open(_CLUBS_, 'r', encoding='utf-8') as file:
        clubs = treat.modif(file.readlines(), '\n', '')
    
    def modif_time(s: str) -> str:
        for c in clubs:
            s = s.replace(c, c.replace(' ', '_'))
        return s
    
    dados = list(map(modif_time, dados))
    dados = treat.modif(dados, ' ', ',')
    dados = treat.modif(dados, 'Competition,Explained,', '')

    with open(_TXT_TEST, 'w', encoding='utf-8') as file:
        file.writelines(dados)

col = [
    'index',
    'position',
    'club',
    'acronym_club',
    'played',
    'won',
    'drawn',
    'lost',
    'scored_goals',
    'conceded_goals',
    'goal_difference',
    'points',
    'first_status_house',
    'week_first_status',
    'day_first_status',
    'month_first_status',
    'year_first_status',
    'first_acronym_home',
    'first_score',
    'acronym_first_adversary',
    'second_status_house',
    'week_second_status',
    'day_second_status',
    'month_second_status',
    'year_second_status',
    'second_acronym_home',
    'second_score',
    'acronym_second_adversary',
    'third_status_house',
    'week_third_status',
    'day_third_status',
    'month_third_status',
    'year_third_status',
    'third_acronym_home',
    'third_score',
    'acronym_third_adversary',
    'fourth_status_house',
    'week_fourth_status',
    'day_fourth_status',
    'month_fourth_status',
    'year_fourth_status',
    'fourth_acronym_home',
    'fourth_score',
    'acronym_fourth_adversary',
    'fifth_status_house',
    'week_fifth_status',
    'day_fifth_status',
    'month_fifth_status',
    'year_fifth_status',
    'fifth_acronym_home',
    'fifth_score',
    'acronym_fifth_adversary',
    'last_club_analyzed',
    'last_result',
    'last_week',
    'last_day',
    'last_month',
    'last_year',
    'last_acronym_club',
    'last_scored',
    'last_acronym_adversary'
]
