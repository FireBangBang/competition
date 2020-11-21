$(document).ready(function () {
    $('#answer').addClass("active");

    // 获取指派的答题人
    var userName = ""
    var type = ""
    assignedName = function () {
        userName = $("input[name='competition-radios']:checked").val();
        console.log("username: " + userName);
    }

    // 点击抢答按钮，重置指派的答题人，进入下一轮抢答
    $("#nav-competition").click(function () {
        userName = ""
        var results = document.getElementsByClassName("competition-radios");
        console.log("result: " + results[0]);
        if (results.length) {
            for (var i = 0; i < results.length; i++) {
                results[i].checked = false;
            }
        }
    });

    // 获取单选题
    getNewSingles = function () {
        type = "single";
        $.get("/get_singles", function (data, status) {
            // console.log("数据： " + data + "  状态：" + status);
            $("#single").html(data);
        });
    }

    // 获取多选题
    getNewMultiples = function () {
        type = "multiple";
        $.get("/get_multiples", function (data, status) {
            // console.log("数据： " + data + "  状态：" + status);
            $("#multiple").html(data);
        });
    }

    // 获取判断题
    getNewDetermines = function () {
        type = "determine";
        $.get("/get_determines", function (data, status) {
            // console.log("数据： " + data + "  状态：" + status);
            $("#determine").html(data);
        });
    }

    // 获取简答题
    getNewResposes = function () {
        type = "response";
        $.get("/get_responses", function (data, status) {
            // console.log("数据： " + data + "  状态：" + status);
            $("#response").html(data);
        });
    }

    // 动态生成的数据，不能用这个方法
    // $("#single_summit").click(function () {
    //     console.log("我在单选中，准备设置答案可见性")
    //     $("#text-single-select-answer").prop("visibility", "visible");
    // });
    checkSingleAnswer = function () {
        // console.log(document.getElementById("text-single-select-answer"))
        var radios = document.getElementsByClassName("single-radios");
        var index = -1
        if (radios.length) {
            for (var i = 0; i < radios; i++) {
                if (radios[i].checked) {
                    index = i;
                    break;
                }
            }
            // console.log(radios[index].val()); // 这个方法不行
            var choose = $("input[name='single-radios']:checked").val().trim();
            console.log(choose);
            var answer = document.getElementById("text-single-select-answer-corr").textContent.trim();
            console.log(answer);
            var res;
            console.log(choose.includes(answer));
            if (choose.includes(answer)) {
                res = "恭喜您答对了！";
                updateAnswerResult(1);
            } else {
                res = "回答错误！正确答案是：" + answer;
                updateAnswerResult(-1);
            }
            document.getElementById("text-single-select-answer").innerHTML = "";
            document.getElementById("text-single-select-answer").innerHTML = res;
            document.getElementById("text-single-select-answer").style.visibility = "visible";
        } else {
            document.getElementById("text-single-select-answer").innerHTML = "请选择...";
        }
    }

    checkMultipleAnswer = function() {
        var boxes = document.getElementsByClassName("multiple-checkboxes");
        if (boxes.length <= 0) {
            return ;
        }
        var chooseArray = new Array();
        for (var i = 0; i < boxes.length; i++) {
            if (boxes[i].checked) {
                // 'A' = 65
                chooseArray.push(i + 65);
                console.log(i + 65);
            }
        }
        if (chooseArray.length <= 0) {
            document.getElementById("text-multiple-select-answer").innerHTML = "请选择...";
            return ;
        }
        var choose = "";
        for (var i = 0; i < chooseArray.length; i++) {
            choose = choose + String.fromCharCode(chooseArray[i]);
            console.log(String.fromCharCode(chooseArray[i]));
        }
        console.log(choose);
        var answer = document.getElementById("text-multiple-select-answer-corr").textContent.trim();
        console.log(answer);
        var res;
        console.log(choose === answer);
        if(choose === answer) {
            res = "恭喜您答对了！";
            updateAnswerResult(2);
        } else {
            res = "回答错误！正确答案是：" + answer;
            updateAnswerResult(-2);
        }
        document.getElementById("text-multiple-select-answer").innerHTML = "";
        document.getElementById("text-multiple-select-answer").innerHTML = res;
        document.getElementById("text-multiple-select-answer").style.visibility = "visible";
    }

    checkDetermineAnswer = function() {
        var radios = document.getElementsByClassName("determine-radios");
        var index = -1
        if (radios.length) {
            for (var i = 0; i < radios; i++) {
                if (radios[i].checked) {
                    index = i;
                    break;
                }
            }
            var choose = $("input[name='determine-radios']:checked").val().trim();
            console.log(choose);
            var answer = document.getElementById("text-determine-answer-corr").textContent.trim();
            console.log(answer);
            var res;
            console.log(choose === answer);
            if (choose === answer) {
                res = "恭喜您答对了！";
                updateAnswerResult(1);
            } else {
                res = "回答错误！正确答案是：" + (answer === "T" ? "对的" : "错的");
                updateAnswerResult(-1);
            }
            document.getElementById("text-determine-answer").innerHTML = "";
            document.getElementById("text-determine-answer").innerHTML = res;
            document.getElementById("text-determine-answer").style.visibility = "visible";
        } else {
            document.getElementById("text-determine-answer").innerHTML = "请选择...";
        }
    }

    showResponseAnswer = function() {
        document.getElementById("response_summit").style.visibility = "hidden";
        document.getElementById("text-response-answer-corr").style.visibility = "visible";
        document.getElementById("text-response-score-board").style.visibility = "visible";
    }

    scoreResponseAnswer = function() {
        var score = document.getElementById("text-response-score-input").value;
        // console.log(document.getElementById("text-response-score-input").textContent);
        // console.log(document.getElementById("text-response-score-input").innerText);
        // console.log(document.getElementById("text-response-score-input").innerHTML);
        // console.log(document.getElementById("text-response-score-input").nodeValue);
        console.log(score)
        if (score) {
            updateAnswerResult(parseFloat(score));
        }
    }

    updateAnswerResult = function (score) {
        var answerResult = {
            user_name: userName,
            type: type,
            score: parseFloat(score)
        };
        $.post("/update_answer_result", JSON.stringify(answerResult), function (data, status) {
            console.log("数据： " + data + "  状态：" + status);
        });
    }

});