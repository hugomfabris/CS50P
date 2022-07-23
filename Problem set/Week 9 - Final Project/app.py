from chessdotcom import get_player_game_archives, get_player_stats, get_player_games_by_month_pgn, get_random_daily_puzzle, ChessDotComError
from typing import Optional, Union
from datetime import date
import requests, sys, re

#The Chessdotcom class will contain the properties, functions and methods that deal directly with the chessdotcom library and its fuctions 
class Chessdotcom():
    #All validations inside the class will consider ChessDotComError as exception and all API functions return a ChessDotComResponse
    def __init__(self, username):
        try:
            self._username = username
        except ChessDotComError:
            sys.exit("Invalid input")

    def __str__(self):
        return str(self._username)

    #With this property we'll access all time players archieves, using chessdotcom get_player_game_archives function
    @property
    def archives(self):
        try:
            data = get_player_game_archives(self._username).json
            #This url give us access to a list, in which every index represents information about games played in a certain month, from less to most recent
            if data:
                return data['archives']
            else:
                sys.exit("No archeives available")

        except ChessDotComError:
            sys.exit("Invalid username")


    @property
    def stats(self):
        try: 
            #Here we use these try and if blocks to ensure that the player exists and has stats available
            if get_player_stats(self._username).json:
                return get_player_stats(self._username).json
            else: 
                return 'No stats found'

        except ChessDotComError:
            sys.exit("Invalid username")


    def acess_all_games(self):
         try:
            data = get_player_game_archives(self._username).json
            #Again, access to a list of monthly games information
            url = data['archives']
            #The first for loop will itarate over the months, the second over the games in each month
            all_games = ''
            if data:
                for i in range(len(url)):
                    games = requests.get(url[i]).json()
                    for j in range(len(games['games'])):
                        all_games += f"{games['games'][j]['pgn']}"
                return all_games
            else:
                return 'No JSON returned'
         except ChessDotComError:
            sys.exit("Invalid input")
        

    def games_by_month(self, year: Optional[Union[str, int]], month: Optional[Union[str, int]]):
        try:
            #Access to direct PGN (chess notation) games information 
            data = get_player_games_by_month_pgn(self._username, year, month).json['pgn']['pgn']
            if data:
                return data
            else:
                return 'No JSON returned'
        
        except ChessDotComError:
            sys.exit("Invalid input")
    
    #This method return a random daily puzzle from chess.com
    @classmethod
    def random_puzzle(cls):
        return get_random_daily_puzzle()


#The main function prompts the user for information needed in each case, dependend on user's demand
def main():
    option = input("Choose an option: ")
    if option == 'archives':
        input_username = input("Username: ")
        input_username = Chessdotcom(input_username)
        print(input_username.archives)
    elif option == 'stats':
        input_username = input("Username: ")
        input_username = Chessdotcom(input_username)
        print(input_username.stats)
    elif option == 'games_by_month':
        input_username = input("Username: ")
        year = input("Year: ")
        month = input("Month: ")
        write_games_by_month(input_username, year, month)
    elif option == 'all_games':
        input_username = input("Username: ")
        write_all_games(input_username)
    elif option == 'games_by_year':
        input_username = input("Username: ")
        year = input("Year: ")
        write_games_by_year(input_username, year)
    elif option == 'games_by_class':
        input_username = input("Username: ")
        time_class = input("Time class: ")
        if time_class in ['rapid', 'bullet', 'blitz']:
            write_games_by_class(input_username, time_class)
        else:
            return 'Invalid class'
    elif option == 'games_by_color':
        input_username = input("Username: ")
        write_games_by_color(input_username, color)
    elif option == 'game_links':
        database = input('Choose an existing database: ')
        write_game_links(database)
        color = input("Color: ")
    elif option == 'opening_links':
        database = input('Choose an existing database: ')
        write_opening_links(database)
    elif option == 'random_puzzle':
        write_random_puzzle()
    else:
        sys.exit("No option found")


def write_all_games(username):
    username = Chessdotcom(username)
    with open(f'database-{username}.pgn', 'a') as file:
        file.write(username.acess_all_games())


def write_games_by_month(username, year, month):
    username = Chessdotcom(username)
    data = username.games_by_month(year, month)
    if data == 'No JSON returned':
        sys.exit('No JSON returned')
    else:
        with open(f'database-{username}-{year}-{month}.pgn', 'a') as file:
            file.write(data)


def write_games_by_year(username, year):
    username = Chessdotcom(username)
    for _ in range(1, 13):
        tempdata = username.games_by_month(year, _)
        if tempdata == 'No JSON returned':
            pass
        else: 
            with open(f'database-{username}-{year}.pgn', 'a') as file:
                file.write(tempdata)


def write_games_by_class(username, time_class):
    username = Chessdotcom(username)
    url = username.archives
    #The first for loop will itarate over the months, the second over the games in each month
    for i in range(len(url)):
        games = requests.get(url[i]).json()
        for j in range(len(games['games'])):
            with open(f'database-{username}-{time_class}-{date.today()}.pgn', 'a') as file:
                if f"{games['games'][j]['time_class']}" == time_class:
                    file.write(f"{games['games'][j]['pgn']}")


def write_games_by_color(username, color):
    username = Chessdotcom(username)
    url = username.archives
    for i in range(len(url)):
        games = requests.get(url[i]).json()
        for j in range(len(games['games'])):
            with open(f'database-{username}-{color}-games-{date.today()}.pgn', 'a') as file: 
                if color in ['white', 'black']:
                    if color == 'white':
                        if f"{games['games'][j]['white']['username']}" == str(username):
                            file.write(f"{games['games'][j]['pgn']}")
                    else:
                        if f"{games['games'][j]['black']['username']}" == str(username):
                            file.write(f"{games['games'][j]['pgn']}")
                else:
                    sys.exit('Invalid color')


def write_game_links(database):
    with open(database, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date = re.match(r'\[Date \"\d\d\d\d\.\d\d\.\d\d\"\]', line)
            link = re.match(r'\[Link \"https\:\/\/www\.chess\.com\/game\/live\/[\d]+\"\]', line)
            with open(f'{database}-links-{date.today()}', 'a') as output:
                if date:
                    output.write(f'{date.group()}\n')
                elif link:
                    output.write(f'{link.group()}\n')


def write_opening_links(database):
    with open(database, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date = re.match(r'\[Date\s\"\d\d\d\d\.\d\d\.\d\d\"\]', line)
            opening = re.match(r'\[ECOUrl \"https\:\/\/www\.chess\.com\/openings\/.+"\]', line)
            with open(f'{database}-openings-{date.today()}', 'a') as output:
                if date:
                    output.write(f'{date.group()}\n')
                elif opening:
                    output.write(f'{opening.group()}\n')


def write_random_puzzle():
    with open(f'random-puzzle-{date.today()}.txt', 'a') as file:
        random_puzzle = str(Chessdotcom.random_puzzle())
        title = re.search(r"title=[\'\"](.+?)[\'\"]", random_puzzle)
        fen = re.search(r"\[FEN \"(.+?)\'", random_puzzle)
        file.write(f'{title.group()}\n')
        file.write(f'{fen.group()}\n')


if __name__ == "__main__":
    main()