/*
 *  Document   : base_ui_activity.js
 *  Author     : pixelcave
 *  Description: Custom JS code used in Activity Page
 */

var SorteoActivity = function() {
    

    // SweetAlert, for more examples you can check out https://github.com/t4t5/sweetalert
    var sweetAlert = function(){
        // Init a simple alert on button click
        jQuery('.js-swal-alert').on('click', function(){
            swal('Hi, this is a simple alert!');
        });

        // Init an success alert on button click
        jQuery('.js-swal-success').on('click', function(){
            swal('Carlo Alva', 'Es el nuevo ganador!', 'success');
        });

        // Init an error alert on button click
        jQuery('.js-swal-error').on('click', function(){
            swal('Oops...', 'Something went wrong!', 'error');
        });

        // Init an example confirm alert on button click
        jQuery('.js-swal-confirm').on('click', function(){
            swal({
                title: 'Are you sure?',
                text: 'You will not be able to recover this imaginary file!',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d26a5c',
                confirmButtonText: 'Yes, delete it!',
                closeOnConfirm: false,
                html: false
            }, function () {
                swal('Deleted!', 'Your imaginary file has been deleted.', 'success');
            });
        });
    };

    return {
        init: function() {
            // Init SweetAlert
            sweetAlert();
        }
    };
}();

// Initialize when page loads
jQuery(function(){ SorteoActivity.init(); });