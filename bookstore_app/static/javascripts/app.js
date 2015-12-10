
var delete_cookie = function(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};

var attachLogOutHandler = function() {
  var logOutButton = document.getElementById('logout-link');

  if (logOutButton) {
    logOutButton.addEventListener("click", function() {
      delete_cookie('bookstore_token')
    })
  }
}


