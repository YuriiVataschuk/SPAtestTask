$(document).ready(function() {
  $('#comment-form').on('submit', function(event) {
    event.preventDefault();

    var commentText = $('#id_text').val();

    $.ajax({
      url: '/validate_comment/',
      data: {
        text: commentText,
        csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      success: function(response) {
        if (response.valid) {
          $('#comment-form').unbind('submit').submit();
        } else {
          $('#validation-message').text(response.error);
        }
      }
    });
  });
});
