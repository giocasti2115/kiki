
$(document).ready(function () {
  $('#contactForm').on('submit', function (e) {
    e.preventDefault();
    var loc = window.location.pathname;
    var dir = loc.substring(0, loc.lastIndexOf('/'));
    $.ajax({
      url: 'code.php',
      type: 'POST',
      data: new FormData(this),
      contentType: false,
      cache: false,
      processData: false,
      beforeSend: function () {
        $(".fa-spin").css("display", "block");
      },
      success: function (result) {
        console.log(result);
        result = $.parseJSON(result);
        $(".fa-spin").css("display", "none");
        if (result.success == false) {
          $('#error_message').html(result.message);
          $('.toast').toast('show');
        } else {
          $("#add-brand")[0].reset();
          $('#error_message').html(result.message);
          $('.toast').toast('show');
          setTimeout(function () {
            location.reload();
          }, 200);
        }
      }
    });
  });
});


