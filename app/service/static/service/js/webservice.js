jQuery(function () {
    // Calling select2 on the select input
    $('#id_webserviceform-contract').select2({
        // need to put this because is inside a modal
        dropdownParent: $('#modal-form'),
        theme: 'bootstrap',
    });

    $('#id_webserviceform-client').select2({
        // need to put this because is inside a modal
        dropdownParent: $('#modal-form'),
        theme: 'bootstrap',
    });

    $('#id_webserviceform-type_of_service').select2({
        // need to put this because is inside a modal
        dropdownParent: $('#modal-form'),
        theme: 'bootstrap',
    });

    $('#id_webserviceform-domain').select2({
        // need to put this because is inside a modal
        dropdownParent: $('#modal-form'),
        theme: 'bootstrap',
    });

    // $('#id_contract').select2({
    //     // need to put this for responsive
    //     width: '100%',
    //     theme: 'bootstrap',
    // });

    $('#id_client').select2({
        // need to put this for responsive
        width: '100%',
        theme: 'bootstrap',
    });

    $('#id_type_of_service').select2({
        // need to put this for responsive
        width: '100%',
        theme: 'bootstrap',
    });

    $('#id_domain').select2({
        // need to put this for responsive
        width: '100%',
        theme: 'bootstrap',
    });

    // if creating a new client has some error, call again the modal with form
    if (showModal == "True") {
        jQuery('#modal-form').modal('show')
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