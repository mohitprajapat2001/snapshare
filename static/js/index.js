$(document).ready(() => {

    $("#copy-link-btn").on("click", () => {
        const link = $("#post-link").val()
        // update data-tip attribute text
        $("#copy-link-btn").attr("data-tip", "Copied")
        setTimeout(() => {
            $("#copy-link-btn").attr("data-tip", "Copy Link")
        }, 2000)
        navigator.clipboard.writeText(link)
        $("#copy-link-btn").text("Copied")
        setTimeout(() => {
            $("#copy-link-btn").text("Copy Link")
        }, 2000)
    })


})