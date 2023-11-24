# This is a sample Python script.
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import zipfile
import csv
import os
from linkpreview import link_preview
import requests
import shutil


if len(sys.argv) != 2:
    print("Usage: python main.py <reddit_zip_file>")
    exit(-1)

path_to_zip_file = sys.argv[1]
username = os.path.basename(path_to_zip_file).split("_")[1]
tmp_dir = "tmp"
data_dir = "data"
try:
    os.makedirs(tmp_dir)
except:
    pass
try:
    os.makedirs(data_dir)
except:
    pass
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(tmp_dir)


def load_template(template_name):
    with open(template_name, "r") as f:
        return f.read()


if not os.path.exists("data/users.json"):
    with open("data/users.json", "w") as f:
        f.write("{}")


def get_user_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get("https://www.reddit.com/user/amngomes/about.json", headers=headers)
    return response.json()["data"]["icon_img"]


users = json.loads(load_template("data/users.json"))
if username not in users:
    users[username] = get_user_image()
    with open("data/users.json", "w") as f:
        f.write(json.dumps(users))


def get_image(image):
    if "giphy" in image:
        image_url = image.replace("gifs", "embed")
        image_id = image_url.split("/")[-1].split("-")[-1]
        image_url = "/".join(image_url.split("/")[:-1]) + "/" + image_id
        return load_template("giphy.tmpl.html").format(src=image_url)
    else:
        try:
            preview = link_preview(image)
            return load_template("image.tmpl.html").format(src=preview.image)
        except:
            return ""


def generate_html():
    shutil.copyfile("logo.jpg", "%s/logo.jpg" % data_dir)
    shutil.copyfile("index.html", "%s/index.html" % data_dir)

    with open("data/%s.html" % username, "w") as f:
        posts_file = "%s/posts.csv" % tmp_dir
        posts = []
        with open(posts_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = dict(body=row["body"], title=row["title"], user=username, date=row["date"], subreddit=row["subreddit"],
                            image=get_image(row["url"]), user_icon=users[username])
                posts.append(load_template("post_entry.tmpl.html").format(**data))
        template_data = dict(
            username=username,
            posts="\n".join(posts).replace("{", "{{").replace("}", "}}")
        )
        f.write(load_template("main.tmpl.html").format(**template_data))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_html()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
