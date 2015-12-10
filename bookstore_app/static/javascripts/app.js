var delete_cookie = function(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;'
};

var attachLogOutHandler = function() {
  $('#logout-link').click(function() {
    delete_cookie('bookstore_token')
  })
}

var attachFeedbackShowHandler = function() {
  $('#feedback-number-show').keyup(function() {
    var input = parseInt(this.value);
    if (input) {
      $('div.feedback').hide()
      $('div.feedback:lt(' + input + ')').show()
    }
  })
}


$(document).ready(function() {
  attachLogOutHandler()
  attachFeedbackShowHandler()
})