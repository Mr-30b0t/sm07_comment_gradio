import json
import os
from collections import defaultdict

class CommentCounter:
    def __init__(self, stats_file="comment_stats.json"):
        self.stats_file = stats_file
        self.total_comments = 0
        self.nurse_portals = defaultdict(set)  # nurse_initials -> set of portal_ids
        self.load_stats()
    
    def load_stats(self):
        """Load existing statistics from file."""
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r') as f:
                    data = json.load(f)
                    self.total_comments = data.get('total_comments', 0)
                    # Convert portal lists back to sets
                    nurse_data = data.get('nurse_portals', {})
                    for nurse, portals in nurse_data.items():
                        self.nurse_portals[nurse] = set(portals)
        except Exception as e:
            print(f"Warning: Could not load stats: {e}")
    
    def save_stats(self):
        """Save current statistics to file."""
        try:
            data = {
                'total_comments': self.total_comments,
                'nurse_portals': {nurse: list(portals) for nurse, portals in self.nurse_portals.items()}
            }
            with open(self.stats_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save stats: {e}")
    
    def increment(self, portal_id, nurse_initials):
        """Increment total comment counter and track nurse-portal relationship."""
        self.total_comments += 1
        if portal_id.strip() and nurse_initials.strip():
            self.nurse_portals[nurse_initials.strip()].add(portal_id.strip())
        self.save_stats()
    
    def get_stats(self, current_nurse_initials=None):
        """Get current statistics as a formatted string."""
        stats = f"📊 **Comment Statistics**\n\n"
        stats += f"**Total Comments Generated:** {self.total_comments}\n\n"
        
        if current_nurse_initials and current_nurse_initials.strip():
            # Show only current nurse's stats
            nurse = current_nurse_initials.strip()
            if nurse in self.nurse_portals:
                stats += f"**Your Distinct Portals:** {len(self.nurse_portals[nurse])} portal(s)\n"
            else:
                stats += f"**Your Distinct Portals:** 0 portal(s)\n"
        else:
            # Show overall stats without revealing individual nurse data
            total_nurses = len(self.nurse_portals)
            total_portals = sum(len(portals) for portals in self.nurse_portals.values())
            stats += f"**Total Nurses:** {total_nurses}\n"
            stats += f"**Total Distinct Portals:** {total_portals}\n"
        
        return stats
    
    def reset_stats(self):
        """Reset all statistics."""
        self.total_comments = 0
        self.nurse_portals.clear()
        self.save_stats()
