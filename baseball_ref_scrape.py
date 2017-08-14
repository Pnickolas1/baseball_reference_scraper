# baseball reference scraper
# tonto #4


import urllib
from BeautifulSoup import BeautifulSoup
import re
import itertools
from string import ascii_letters
import sys

STANDARD_BATTING_COLUMNS=(
'Year',
'Age',
'Team',
'League',
'Games Played or Pitched',
'Plate Appearances',
'At Bats',
'Runs Scored/Allowed',
'Hits/Hits Allowed',
'2B',
'3B',
'HR',
'RBI',
'SB',
'CS',
'BB',
'SO',
'BA',
'OBP',
'SLG',
'OPS',
'OPX+',
'TB',
'GDP',
'HBP',
'SH',
'IBB',
'Pos',
'Awards'
)

def url_to_beautiful_soup(url):
    url = urllib.urlopen(url)
    soup = BeautifulSoup(''.join(url.readlines()))
    return soup

def link_to_url(link_element, domain='baseball-reference.com'):
    href = filter(lambda attr: attr[0] =='href', link_element.attrs)[0][1]
    return ''.join(('http://', domain, href))

def find_batting_standard_table(soup):
    for table in soup.findall('table'):
        try:
            if table['id'] =='batting_standard':
                return table
        except KeyError:
            '''
            table not have an id attribute'''
            pass
        
batting_standard_re = 'batting_standard\.((18|19|20)[0-9]{2})'

def decompose_batting_table(batting_table_soup):
    '''takes the soup of batting statistics'''
    stats = []
    batting_table_body = batting_table_soup.findall('tbody')[0]
    for table_row in batting_table_body.findall('tr'):
        table_row_id = table_row.get('id')
        if not table_row_id:
            continue
        year = re.findall(batting_standard_re, table_row_id)
        row_values = {}
        values = [element.text for element in table_row.findall('td')]
        stats_keys_values = zip(STANDARD_BATTING_COLUMNS, values)
        row_values = dict(stats_keys_values)
        
        stats.append(row_values)
        
    return stats

def batting_stats_from_soup(soup):
    batting_table = find_batting_standard_table(soup)
    if batting_table:
        stats = decompose_batting_table(batting_table)
        return stats

def player_page_links(players_page_url):
    f = urllib.urlopen(players_page_url)
    soup = BeautifulSoup(''.join(f))
    page_content = soup.findAll('div', id='page_content')[0]
    player_blocks = page_content.findAll('blockquote')
    link_elements = (player_block.findAll('a') for player_block
                     in player_blocks)
    link_elements = itertools.chain(*link_elements)


    for link_element in link_elements:
        player_name = link_element.text
        player_page_url = link_to_url(link_element)
        yield player_name, player_page_url
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    