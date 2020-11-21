$(document).ready(function () {
    $('#score').addClass("active");

    var ob;
    $(".table td").dblclick(function () {
        if (ob != null && $(this).getElementsByTagName("input") != null){
            return;
        }
        var row = $(this).parent().parent().find("tr").index($(this).parent()[0]);
        var col = $(this).parent().find("td").index($(this)[0]);
        var arr = new Array();
        for (var i = 0; i < 16; i++) {
                var ele = $(this).parent().find("td").eq(i).text();
                arr[i]= ele;
                console.log(ele);
        }
        ob = $(this);
        var val = $(this).html();
        var texts = document.createElement("input");
        texts.setAttribute("id", "input");
        texts.setAttribute("type", "text");
        texts.setAttribute("width", "3em");
        texts.setAttribute("text-align", "left");
        texts.setAttribute("value", $(this).html());
        texts.removeAttribute("ondblclick");
        $(this).html("");
        $(this).append(texts);
        texts.addEventListener("focusout", function () {
            if ($(this) != null) {
                fun($(this));
            }
        });
        texts.addEventListener("keypress", function (event) {
            if (event.key === "Enter" && $(this) != null) {
                fun($(this));
            }
        });
        function fun(b) {
            var re = new RegExp(/[^0-9+-]*/);
            var one = texts.value.replace(re, "");
            var strs = one.match(/[+|-]?[1-9][0-9]*/);
            if (strs != null && strs[0] != null) {
                b.parent().html(strs[0]);
                arr[col] = strs[0];
            }else {
                b.parent().html(val);
                arr[col] = val;
            }
            b.parent().remove(b);

            ob = null;
            var reqData = {
                user_id: parseInt(arr[0]),
                user_name: arr[1],
                score: parseFloat(arr[2]),
                rank: parseInt(arr[3]),
                single_count: parseInt(arr[4]),
                single_correct: parseInt(arr[5]),
                single_score: parseFloat(arr[6]),
                multiple_count: parseInt(arr[7]),
                multiple_correct: parseInt(arr[8]),
                multiple_score: parseFloat(arr[9]),
                deter_count: parseInt(arr[10]),
                deter_corr: parseInt(arr[11]),
                deter_score: parseFloat(arr[12]),
                resp_count: parseInt(arr[13]),
                resp_corr: parseInt(arr[14]),
                resp_score: parseFloat(arr[15])
            }
            console.log(JSON.stringify(reqData));
            $.post("/update_score", JSON.stringify(reqData), function(data, status) {
                console.log("数据： " + data + "  状态：" + status);
            });
        }
    });
});
