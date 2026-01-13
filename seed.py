from app import app
from models import db, Episode, Guest, Appearance
import random

def seed_data():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()
        
        # Sample episodes based on CSV dates
        episodes_data = [
            {"date": "1/11/99", "number": 1},
            {"date": "1/12/99", "number": 2},
            {"date": "1/13/99", "number": 3},
            {"date": "1/14/99", "number": 4},
            {"date": "1/18/99", "number": 5}
        ]
        
        # Sample guests based on CSV data
        guests_data = [
            {"name": "Michael J. Fox", "occupation": "actor"},
            {"name": "Sandra Bernhard", "occupation": "Comedian"},
            {"name": "Tracey Ullman", "occupation": "television actress"},
            {"name": "Gillian Anderson", "occupation": "film actress"},
            {"name": "David Alan Grier", "occupation": "actor"}
        ]
        
        # Create episodes
        for episode_data in episodes_data:
            episode = Episode(**episode_data)
            db.session.add(episode)
        
        # Create guests
        for guest_data in guests_data:
            guest = Guest(**guest_data)
            db.session.add(guest)
        
        db.session.commit()
        
        # Create appearances
        episodes = Episode.query.all()
        guests = Guest.query.all()
        
        for i, episode in enumerate(episodes):
            if i < len(guests):
                appearance = Appearance(
                    rating=random.randint(1, 5),
                    episode_id=episode.id,
                    guest_id=guests[i].id
                )
                db.session.add(appearance)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()