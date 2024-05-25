from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Dummy data for user preferences and fashion items
user_preferences = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
fashion_items = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

def get_recommendations(user_id):
    user_vector = user_preferences[user_id]
    similarities = cosine_similarity([user_vector], fashion_items)
    recommended_items = np.argsort(similarities[0])[::-1]
    return recommended_items
