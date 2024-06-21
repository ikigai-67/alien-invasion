from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        #High score should never be reset.
        self.high_score = self.get_high_score()

    def get_high_score(self):
        """Get the all time high score if it exist."""
        path = Path('high_score.json')
        if path.exists():
            contents = path.read_text()
            try:
                high_score = json.loads(contents)
            except ValueError:
                high_score = 0
                contents = json.dumps(high_score)
                path.write_text(contents)
                return high_score
            else:
                return int(high_score)
            
    def store_high_score(self):
        """Store the high score."""
        path = Path('high_score.json')
        contents = json.dumps(self.high_score)
        path.write_text(contents)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1