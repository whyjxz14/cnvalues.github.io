$.ajax({
    type: "GET",
    url: "info/version.json",
    dataType: "json",
    success: (data) => {
        $("#version").html("版本号：" + data.version)
    }
})
