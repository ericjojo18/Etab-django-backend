/*==================== Pour la generation de report ====================*/

function generateReport(format) {
    var dataType = document.getElementById("report").ariaValueMax;
    var url = "/generate-report/?report=" + format + "&report=" + dataType;
    window.location.href = url;
}