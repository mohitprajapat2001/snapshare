$(document).ready(() => {
    const selectTheme = $("#theme-select")
    const themeSelected = window.localStorage.getItem("theme");
    if (themeSelected) {
        bodyTheme(themeSelected)
        selectTheme.val(themeSelected)
    }
    selectTheme.on("change", () => {
        window.localStorage.setItem("theme", selectTheme.val())
        bodyTheme(selectTheme.val())
    })
})

function bodyTheme(theme) {
    const body = document.querySelector("body");
    theme && body.setAttribute("data-theme", theme)
}