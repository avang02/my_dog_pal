$(document).ready(function () {
    $('.dropdown-trigger').dropdown({
        inDuration: 300,
        coverTrigger: false,
        belowOrigin: true,
        hover: true,
        alignment: 'bottom'
    });
    
    $('.sidenav').sidenav();
});

function submitForm() {
    document.getElementById('logout-form').submit();
}
