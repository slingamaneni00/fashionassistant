import os
import pandas as pd
from flask import Flask, render_template

app = Flask(_name_)

image_dir = '/home/siddhant/Desktop/fashionassistant-master'

image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]

image_ids = [1001, 1002, 1003, 1004, 1005, 1006]

data = {"paths": image_paths, "id": image_ids}
df = pd.DataFrame(data)

print(df)

def compare(a1, a2):
    score = 0
    if a1 == 1001 and a2 == 1002:
        score = 1
    elif a1 == 1001 and a2 == 1003:
        score = 0.83
    elif a1 == 1001 and a2 == 1004:
        score = 0.5
    elif a1 == 1001 and a2 == 1005:
        score = 0.5
    elif a1 == 1001 and a2 == 1006:
        score = 0.5
    return score

@app.route('/')
def index():
    score = compare(1001, 1002)
    return render_template('createoutfit.html', score=score)

if _name_ == '_main_':
    app.run()
