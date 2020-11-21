from flask import request, render_template
from flask import jsonify
import random
import json
from structlog import get_logger
from app.main import main
from app import csrf
from app.constant import const
from app.database.db_helper import db


@main.route('/', methods=['GET', 'POST'])
def init():
    if request.method == 'GET':
        data = form_singles_dict()
        data.update(form_multiple_dict())
        data.update(form_determines_dict())
        data.update(form_responses_dict())
        data.update(form_assign_names_dict())
        get_logger().info(data)
        return render_template("main/answer.html", **data)
    else:
        return render_template("main/answer.html")


@main.route("/get_singles", methods=["GET", "POST"])
def get_singles():
    data = form_singles_dict()
    return render_template("main/single.html", **data)
    # if request.method is ["GET", "POST"]:
    #     data = json.dumps(form_singles_dict())
    #     return jsonify(json.dumps(data))
    # return jsonify({})


@main.route("/get_multiples", methods=["GET", "POST"])
def get_multiples():
    data = form_multiple_dict()
    return render_template("main/multiple.html", **data)


@main.route("/get_determines", methods=["GET", "POST"])
def get_determines():
    data = form_determines_dict()
    return render_template("main/determine.html", **data)


@main.route("/get_responses", methods=["GET", "POST"])
def get_responses():
    data = form_responses_dict()
    return render_template("main/response.html", **data)


@csrf.exempt
@main.route("/update_answer_result", methods=["POST"])
def update_answer_result():
    data = request.get_data()
    dic = json.loads(data)
    update_db_from_net(dic)

    return jsonify({"status": "ok"})


def form_singles_dict():
    topics = db.fetch_data()
    table_singles = topics[0]
    length = len(table_singles)

    while True:
        global rand
        rand = random.randint(1, length - 1)
        if not db.check_have_been_selected(0, rand):
            break

    singles = table_singles[rand]
    data = {
        "single_topic": singles[2],
        "singles": singles[3:7],
        "single_answer": singles[7]
    }
    return data


def form_multiple_dict():
    topics = db.fetch_data()
    table_singles = topics[1]
    length = len(table_singles)

    while True:
        global rand
        rand = random.randint(1, length - 1)
        if not db.check_have_been_selected(1, rand):
            break

    singles = table_singles[rand]
    data = {
        "multiple_topic": singles[2],
        "multiples": singles[3:7],
        "multiple_answer": singles[7]
    }
    return data


def form_determines_dict():
    topics = db.fetch_data()
    table_singles = topics[2]
    length = len(table_singles)

    while True:
        global rand
        rand = random.randint(1, length - 1)
        if not db.check_have_been_selected(2, rand):
            break

    singles = table_singles[rand]
    data = {
        "determine_topic": singles[2],
        "determine_answer": singles[7]
    }
    return data


def form_responses_dict():
    topics = db.fetch_data()
    table_singles = topics[3]
    length = len(table_singles)

    while True:
        global rand
        rand = random.randint(1, length - 1)
        if not db.check_have_been_selected(3, rand):
            break

    singles = table_singles[rand]
    data = {
        "response_topic": singles[2],
        "response_answer": singles[7]
    }
    return data


def form_assign_names_dict():
    names = list(const.USER_NAMES)
    data = {
        "names": names
    }
    return data


def update_db_from_net(dic):
    get_logger().info(dic)
    user = db.get_one_user(dic["user_name"])
    get_logger().info(user)
    if dic["type"] == "single":
        user.score += dic["score"]
        user.single_score += dic["score"]
        user.single_count += 1
        if dic["score"] > 0:
            user.single_correct += 1
    elif dic["type"] == "multiple":
        user.score += dic["score"]
        user.multiple_score += dic["score"]
        user.multiple_count += 1
        if dic["score"] > 0:
            user.multiple_correct += 1
    elif dic["type"] == "determine":
        user.score += dic["score"]
        user.deter_score += dic["score"]
        user.deter_count += 1
        if dic["score"] > 0:
            user.deter_corr += 1
    else:
        dic["type"] == "response"
        user.score += dic["score"]
        user.resp_score += dic["score"]
        user.resp_count += 1
        if dic["score"] > 0:
            user.deter_corr += 1

    db.update_users(user)
