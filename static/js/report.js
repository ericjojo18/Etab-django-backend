/*==================== Pour la generation de rapport ====================*/

function generateReport(format) {
    var dataType = document.getElementById("rapport").ariaValueMax;
    var url = "/generate-report/?report=" + format + "&rapport=" + dataType;
    window.location.href = url;
}