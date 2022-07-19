from chessdotcom import get_player_game_archives, get_player_stats, get_player_games_by_month_pgn, ChessDotComError
import requests
import sys
from typing import Optional, Union

class Chessdotcom():
    def __init__(self, username):
        self._username = username
    
    def __str__(self):
        return self._username
    
    @property
    def achieves(self):
        data = get_player_game_archives(self._username).json
        #This url give us access to a list, in which every index represents information about games played in a certain month, from less to most recent
        url = data['archives']
        return url
    
    @property
    def stats(self):
        return get_player_stats(self._username).json
    
    def games_by_month(self, year: Optional[Union[str, int]], month: Optional[Union[str, int]]):
        try:
            data = get_player_games_by_month_pgn(self._username, year, month).json['pgn']['pgn'] 
            if data:
                return data
            else:
                sys.exit("No json returned")
        
        except ChessDotComError:
            sys.exit("Invalid input")
    
    def games_by_class(self, time):
        ...
    
    def game_links(self):
        ...
    
    def games_by_color(self, color):
        ...

def main():
    username = input("Username: ")
    option = input("Choose which option do you want to execute: ")
    if option == 'games_by_month':
        year = input("Year: ")
        month = input("Month: ")
        write_games_by_month(username, year, month)
    elif option == 'all_games':
        write_all_games(username)
    elif option == 'games_by_year':
        year = input("Year: ")
        games_by_year(username, year)
    else:
        sys.exit("No option found")

def write_all_games(username):
        username = Chessdotcom(username)
        url = username.achieves
        #The first for loop will itarate over the months, the second over the games in each month
        for i in range(len(url)):
            games = requests.get(url[i]).json()
            for j in range(len(games['games'])):
                with open(f'database-{username}.pgn', 'a') as file:
                    file.write(f"{games['games'][j]['pgn']}")

def write_games_by_month(username, year, month):
    username = Chessdotcom(username)
    data = username.games_by_month(year, month)
    with open(f'database-{username}-{year}-{month}.pgn', 'a') as file:
        file.write(data)

def games_by_year(username, year):
    username = Chessdotcom(username)
    for _ in range(1, 13):
        tempdata = username.games_by_month(year, _)
        with open(f'database-{username}-{year}.pgn', 'a') as file:
            file.write(tempdata)




if __name__ == "__main__":
    main()