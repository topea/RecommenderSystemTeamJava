import pandas as pd
import math

interactions_df = pd.read_csv('data/notifications.csv')

# from notifications.csv there are 5 reactions
event_type_strength = {
    'Followed': 1.0,
    'Like': 1.0,
    'Love': 2.0,
    'Commented': 4.0,
    'Replied': 4.0
}
interactions_df['eventStrength'] = interactions_df['action'].apply(lambda x: event_type_strength[x])
print(interactions_df.head(10))
users_interactions_count_df = interactions_df.groupby(['user_id', 'post_id']).size().groupby('user_id').size()
print('# users: %d' % len(users_interactions_count_df))
users_with_enough_interactions_df = users_interactions_count_df[users_interactions_count_df >= 2].reset_index()[['user_id']]
print('# users with at least 2 interactions: %d' % len(users_with_enough_interactions_df))

print('# of interactions: %d' % len(interactions_df))
interactions_from_selected_users_df = interactions_df.merge(users_with_enough_interactions_df, how='right',
                                                            left_on='user_id', right_on='user_id')
print('# of interactions from users with at least 2 interactions: %d' % len(interactions_from_selected_users_df))


def smooth_user_preference(x):
    return math.log(1 + x, 2)


interactions_full_df = interactions_from_selected_users_df \
    .groupby(['user_id', 'post_id'])['eventStrength'].sum() \
    .apply(smooth_user_preference).reset_index()
print('# of unique user/item interactions: %d' % len(interactions_full_df))
print(interactions_full_df.head(10))

item_popularity_df = interactions_full_df.groupby('post_id')['eventStrength'].sum().sort_values(ascending=False).reset_index()
print(item_popularity_df.head(10))
