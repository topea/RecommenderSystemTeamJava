
# RecommenderSystem
we listed out all the data and cleaned them to get the important data needed for the recommendation project.
we selected our data based on 
1. content of each user in the data set
2. similiarities between posts among the users.


## Content Based Recommender System
We built a content based recommender that computes similarity between posts based on its content and suggests posts that are similar. To test you pass in a post title to the function and you will get similar posts as the output. An example is shown below:

```get_article_recommendations_for_user('What i have learnt so far on HTML')```


## Follower Based Recommender System
We built a follower based recommender that computes similarity between users based on their bio and recommends similar users. To test you pass in a user id to the function and you will get similar users as the output. An example is shown below:

```get_followers(23)```


## Testing our model
You can test our model using colab at this link https://colab.research.google.com/drive/1FKGFQpPyw6dPxCaFSpnm00p1SnMqguy5#scrollTo=OeZi6U2spauu

You can download the csv data from https://drive.google.com/open?id=1G3w4nU85iUGvMyScA6iMdooygTo3jmig and then upload to a google drive

Run the colab file. Instructions on how to mount your google drive to read the data will be outline.
