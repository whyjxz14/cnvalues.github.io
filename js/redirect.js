$.ajax({
    type: "GET",
    url: "info/version.json",
    dataType: "json",
    success: (data) => {
        if (window.location.href !== data.url && window.location.href !== "localhost") {
            window.location.replace(data.url)
        }
    }
})
