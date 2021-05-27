jQuery(function () {
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
    if (showModal == "True") {
        jQuery('#modal-client').modal('show')
    }

});

function onClickConfirm(action) {
    $("#actions").val(action);
    if ($('input[name="selection"]:checked').length > 0) {
        if (action == "edit") {
            $('#form-table').trigger('submit');
        }
        if (action == "delete") {
            deleteConfirm();
        }
    }
}

function deleteConfirm() {
    howManyChecked();
    jQuery('#modal-delete').modal('show');
}

function toggle(source) {
    checkboxes = document.getElementsByName('selection');
    for (var i in checkboxes)
        checkboxes[i].checked = source.checked;
}

function howManyChecked() {
    $(".toDeleteCount").html($('input[name="selection"]:checked').length);
}