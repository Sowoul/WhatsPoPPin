from flask import Flask, render_template, request, redirect, url_for
from store import PostManager  

app = Flask(__name__)
post_manager = PostManager() 

@app.route('/')
def index():
    hashtags = ['#BiggBoss17GrandFinale', '#AbhishekKumar', '#MannaraChopra','#OjaswaSharma']
    posts = post_manager.get_all_posts() 
    user_info = {
        'username': 'Ojaswa',
        'profile_image_url': 'https://media.licdn.com/dms/image/D4D03AQGBWNHjbio17w/profile-displayphoto-shrink_800_800/0/1689695616193?e=1712188800&v=beta&t=IuJ0YkGDXsX00YvMOFtIZfrPLJlhZV6lRqUOqdfDNdY'
    }
    return render_template('temp.html', hashtags=hashtags, posts=posts, user_info=user_info)

@app.route('/upload', methods=['POST'])
def upload():
    username = request.form['username']
    image_url = request.form['image_url']
    post_manager.add_post({'username': username, 'image_url': image_url})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
