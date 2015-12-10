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

var sort_year = function(a, b) {
  return parseInt($(b).data('year')) < parseInt($(a).data('year')) ? 1 : -1;
}

var sort_year_r = function(a, b) {
  return parseInt($(b).data('year')) > parseInt($(a).data('year')) ? 1 : -1;
}

var sort_score = function(a, b) {
  return parseInt($(b).data('rating')) < parseInt($(a).data('rating')) ? 1 : -1;
}

var sort_score_r = function(a, b) {
  return parseInt($(b).data('rating')) > parseInt($(a).data('rating')) ? 1 : -1;
}

var attachSortBooksFilter = function() {
  $('#sort-dropdown').change(function() {
    var sort = this.value
    if (sort == 'year-a') {
      $('.books a').sort(sort_year).appendTo('.books')
    } else if (sort == 'year-d') {
      $('.books a').sort(sort_year_r).appendTo('.books')
    } else if (sort == 'score-a') {
      $('.books a').sort(sort_score).appendTo('.books')
    } else if (sort == 'score-d') {
      $('.books a').sort(sort_score_r).appendTo('.books')
    }
  })
}

$(document).ready(function() {
  attachLogOutHandler()
  attachFeedbackShowHandler()
  attachSortBooksFilter()
})