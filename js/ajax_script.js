function ajaxScript() {
    var story_tag = $("#story_tag").val();
    var keyword_tag = $("#keyword_tag").val();
    var comment_tag = $("#comment_tag").val();
    $.ajax({
        type: "POST",
        url: "/MyProfile",
        data: JSON.stringify({
            "story_tag": story_tag,
            "keyword_tag": keyword_tag,
            "comment_tag": comment_tag
        }),
        dataType: "json"
    })
        .done(function (jsonResponse) {
            $("#error").html(jsonResponse.message);
        });
}
