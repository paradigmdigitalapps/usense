function ajaxGetGroupname() {
    $.ajax({
        type: "POST",
        url: "/groupname",
        data: JSON.stringify(groupname),
        dataType: "json"
    })
        .done(function(jsonResponse) {
            document.getElementById("demo").innerHTML = jsonResponse.message + ' ' + loadconfirm;
        });
/*                alert("Kérlek minden szempontot értékelj");
*/

}
