$(document).ready(function () {
    // Calling select2 on the select input
    $('#id_clientform-occupation').select2({
        // need to put this because is inside a modal
        dropdownParent: $('#modal-client'),
        theme: 'bootstrap',
    });

    $('#id_occupation').select2({
        // need to put this for responsive
        width: '100%',
        theme: 'bootstrap',
    });

    // if creating a new client has some error, call again the modal with form
    if (showModal) {
        var myModal = new bootstrap.Modal(document.getElementById('modal-client'));
        myModal.show();
    }

});

function onClickConfirm() {
    if ($("#action_options option:selected").text() == "Edit") {
        if ($('input[name="selection"]:checked').length > 0) {
            $('#form-table').submit();
        }
    } else {
        deleteConfirm();
    }
}

function deleteConfirm() {
    if ($('input[name="selection"]:checked').length > 0) {
        var modalDelete = new bootstrap.Modal(document.getElementById('modal-delete'));
        howManyChecked();
        modalDelete.show();
    }
}

function toggle(source) {
    checkboxes = document.getElementsByName('selection');
    for (var i in checkboxes)
        checkboxes[i].checked = source.checked;
}

function howManyChecked() {
    $(".toDeleteCount").html($('input[name="selection"]:checked').length);
}