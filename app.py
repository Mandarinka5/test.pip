from flask import Flask
import json

with open('candidates.json', encoding='utf-8') as fh:
    content_py = json.load(fh)

print(content_py)

app = Flask(__name__)


@app.route('/')
def page_profile():
    def get_info(info):
        candidates_name = info['name']
        candidates_position = info['position']
        candidates_skills = info['skills']
        one_candidates_info = f"Имя кандидата - {candidates_name}<br>Позиция кандидата - {candidates_position}<br>Навыки через запятую - {candidates_skills}<br><br>"

        return one_candidates_info

    candidates_info = []
    for info in content_py:
        candidates_info += get_info(info)

    candidates_info_str = "".join(candidates_info)

    return f'<pre>{candidates_info_str}<pre>'


@app.route('/candidates/<int:uid>')
def page_candidate_uid(uid):
    for candidates in content_py:
        if candidates["id"] == uid:
            picture_src = candidates['picture']
            candidates_name = candidates['name']
            candidates_position = candidates['position']
            candidates_skills = candidates['skills']
        else:
            print("candidate is not found")

    candidate_x_result = f"<img src={picture_src}><br><br><pre>Имя кандидата - {candidates_name}<br>Позиция кандидата - {candidates_position}<br>Навыки через запятую - {candidates_skills}<br><br><pre>"

    return candidate_x_result


@app.route("/skills/<int:uid>")
def page_messages(uid):
    for skill in content_py:
        if len(skill['skills'].split(',')) == 1:
            candidates_name = skill['name']
            candidates_position = skill['position']
            candidates_skills = skill['skills']
            candidates_data = f'<pre>Имя кандидата - {candidates_name}<br>Позиция кандидата - {candidates_position}<br>Навыки через запятую - {candidates_skills}<pre>'

    return candidates_data


app.run()



