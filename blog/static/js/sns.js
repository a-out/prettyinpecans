function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
   // these HTTP methods do not require CSRF protection
   return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ajaxSend(function(e, xhr, settings) {
   if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
   }
});

$(document).ready(function() {
   $('#subscribe-form').submit(function(event) {
      submitEmail();
      event.preventDefault();
   });
});

function recipe_browser_clear() {
    window.location.href = '/recipes/browser';
};

function isValidEmail(email) {
   // not a perfect validation, but it'll have to do
   var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
   return re.test(email);
};

function submitEmail() {
   var email = $('#subscribe-input').val();

   if (!isValidEmail(email)) {
      $('#subscribe-messages').html('Please enter a valid email.');
      return;
   }

   var postData = {
      'email': email
   };

   console.log(postData);

   $.ajax({
      type: 'POST',
      url: 'newsletter/subscribe/',
      data: JSON.stringify(postData),
      contentType: "application/json; charset=utf-8",
      success: function() {
         $('#subscribe-messages').html('Welcome!');
         $('#subscribe-input').hide();
      },
      error: function(r, s, e) {
         
      }
   });
};