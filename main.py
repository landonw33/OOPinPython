from user import User
from post import Post

# creating info for class
app_user_one = User("tom@gmail.com", "Tom", "password123", "EE Engineer I")
app_user_one.get_user_info()

# changing job title
app_user_one.change_job_title("EE Engineer II")
app_user_one.get_user_info()

# another user
app_user_two = User("stacy@yahoo.com", "Stacy", "pword", "Accountant I")
app_user_two.get_user_info()

new_post = Post("I went on Vacation!", app_user_one.name)
new_post.get_post_info()