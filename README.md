#  ![movvie-icon](https://github.com/Ravdar/bloggin/assets/97836782/af6c0859-fe0a-4ac6-a2da-071de1cedf7b) movvie - AI movie recommender





movvie is web application developed using Django and integrated with the OpenAI API, that delivers personalized movie recommendations. Upon receiving a user's prompt, it suggests five curated films. Additionally, the application features a function to generate random movie selections. Each recommendation includes the movie’s poster, title, production year, TMDB rating, duration, streaming availability, and a concise description, utilizing data from TMDB and JustWatch APIs.


[bloggin Intro.webm](https://github.com/Ravdar/bloggin/assets/97836782/84c13d45-4875-4642-8205-2a33ee2dbff8)


For a more detailed video with my commentary, click (video no added yet) [here.](https://www.youtube.com/watch?v=VewCNybNQKE)

# Features

Bloggin offers a variety of features including:

### 1. Account creation
Users can create accounts, selecting their nicknames and profile pictures
### 2. Reading articles
Users can read articles of other users
### 3. Writing articles
Logged user can write their own article, which will be available for other users to read
### 4. Adding comments and subcomments
Logged users can add comments under each article, they can also reply to other users comments
### 5. Checking other users profiles
Users can check profiles of other users to follow their activity

# Screenshots
![bloggin-homepage](https://github.com/Ravdar/bloggin/assets/97836782/214be85b-d01b-49c7-84f0-35366463b779)
![bloggin-article](https://github.com/Ravdar/bloggin/assets/97836782/e0474381-2219-4f93-be2d-851e92104bd9)
![bloggin-![bloggin-new-article](https://github.com/Ravdar/bloggin/assets/97836782/c88505e4-2e89-466b-b918-50a61a92c101)
profile](https://github.com/Ravdar/bloggin/assets/97836782/492abb04-b31e-49f1-a4fb-36ad23687ece)
![bloggin-login](https://github.com/Ravdar/bloggin/assets/97836782/2c3765b5-0ecd-424f-afdf-73b8a9269021)

# Techstack
* Django
* django.contrib.auth
* django models
* django forms
* RichTextField
* python decorators

# Installation
1. Clone the repository:
```git clone https://github.com/Ravdar/bloggin```
2. Install the required libraries:
```pip install -r requirements.txt```
3. Run the application:
```python main.py```
4. Access the app in your web browser via your local server
