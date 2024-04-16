$(document).ready(function () {
    $('.dropdown-trigger').dropdown({
        inDuration: 300,
        coverTrigger: false,
        hover: true,
    });

    $('.sidenav').sidenav();

    $('select').formSelect();

    $('.materialboxed').materialbox();
  
});

function submitForm() {
    document.getElementById('logout-form').submit();
}
