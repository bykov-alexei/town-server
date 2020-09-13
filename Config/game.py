from datetime import datetime


GAME_CONFIG = {
    'people_number': 50,
    'town_number': 5,
    
    'n_interests': 2,
    'interests': ['culture', 'sport', 'entertainment'],
    'needs': ['food', 'work', 'rest'],
    
    'n_qualifications': 2,
    'qualifications': ['waiter', 'security', 'factory'],
    
    # System params
    'start_time': datetime(year=2000, month=1, day=1, hour=8, minute=30).timestamp(),
    
    'step_real_time': 1,
    'steps_in_day': 24*60,
}
