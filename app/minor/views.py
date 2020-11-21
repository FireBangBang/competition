from flask import render_template, redirect, request, url_for, flash
from flask_wtf import CSRFProtect
from flask import jsonify
import json
from structlog import get_logger

from app.constant import const
from app import csrf
from app.database.db_helper import db

from app.minor import minor
from app.database.user_model import UserModel


@minor.route('/get_score', methods=['GET', 'POST'])
def get_score():
    """
    获取成绩
    """
    data = {
        "headers": const.EXCEL_HEADERS,
        "users": [
                list(user.__dict__.values()) for user in db.fetch_users()
            ]
    }
    # get_logger().info(data)
    return render_template('minor/score.html', **data)


@csrf.exempt
@minor.route('/update_score', methods=['POST'])
def update_score():
    data = request.get_data()
    dic = json.loads(data)

    user = UserModel()
    try:
        user.user_id = dic["user_id"]
        user.user_name = dic["user_name"]
        user.score = dic["score"]
        user.rank = dic["rank"]
        user.single_count = dic["single_count"]
        user.single_correct = dic["single_correct"]
        user.single_score = dic["single_score"]
        user.multiple_count = dic["multiple_count"]
        user.multiple_correct = dic["multiple_correct"]
        user.multiple_score = dic["multiple_score"]
        user.deter_count = dic["deter_count"]
        user.deter_corr = dic["deter_corr"]
        user.deter_score = dic["deter_score"]
        user.resp_count = dic["resp_count"]
        user.resp_corr = dic["resp_corr"]
        user.resp_score = dic["resp_score"]
    except ValueError:
        return jsonify({"status": "value error"})

    db.update_users(user)
    get_logger().info(user.rank)

    return jsonify({"status": "ok"})
