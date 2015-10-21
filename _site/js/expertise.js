(function() {
  var expertise;

  expertise = {
    select: function(category) {
      $('#categories a.active').removeClass('active');
      $(category).addClass('active');
      $('#skills ul').addClass('hidden');
      return $(category.dataset.target).removeClass('hidden');
    }
  };

  $(function() {
    $('#categories a').click(function(ev) {
      ev.preventDefault();
      return expertise.select(this);
    });
    return expertise.select($('#categories a')[0]);
  });

}).call(this);
