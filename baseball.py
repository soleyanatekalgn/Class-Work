import re
import sys
from collections import defaultdict

class Player:
    def __init__(self, name):
        self.name = name
        self.at_bats = 0
        self.hits = 0

    def update_stats(self, at_bats, hits):
        self.at_bats += at_bats
        self.hits += hits

    def batting_average(self):
        if self.at_bats > 0:
            return self.hits / self.at_bats
        return 0.0

def main():
    if len(sys.argv) != 2:
        print("Usage: python baseball.py <path_to_input_file>")
        return

    input_file = sys.argv[1]
    
    
    pattern = re.compile(r'^(.*) batted (\d+) times with (\d+) hits and (\d+) runs$')

    players = defaultdict(lambda: Player(name=''))  

    with open(input_file, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                name = match.group(1)
                at_bats = int(match.group(2))
                hits = int(match.group(3))
                
                
                if name not in players:
                    players[name] = Player(name)  
                players[name].update_stats(at_bats, hits)

    
    averages = [(player.name, player.batting_average()) for player in players.values()]
    
    
    averages.sort(key=lambda x: x[1], reverse=True)

    
    for name, avg in averages:
        print(f"{name}: {avg:.3f}")

if __name__ == "__main__":
    main()
