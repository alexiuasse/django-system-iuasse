$(document).ready(function () {
    $('#id_clientform-occupation').select2({
        dropdownParent: $('#modal-client'),
        theme: 'bootstrap',
    });

    if (hasError) {
        var myModal = new bootstrap.Modal(document.getElementById('modal-client'));
        myModal.show();
    }
});