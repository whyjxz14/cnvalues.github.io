$.ajax({
    type: "GET",
    url: "info/version.json",
    dataType: "json",
    success: (data) => {
        if (![data.hostname, "localhost", "127.0.0.1"].some((value) => {
            return window.location.hostname === value
        })) {
            let url = "https://" + data.hostname
            alert("项目已迁移至 " + url)
            window.location.href = url
        }
    }
})
