jQuery(document).ready(function($) {
  var container = $('.extensions');
  var chosen_select = $('.chosen-select');
  var $form = $('form#filters');

  // make form visible - will not work if no javascript
  $(".form-inline").removeClass("hidden");

  // triggered when the form text is changed
  $form.on('change submit', function(e) {
    e.preventDefault();

    var chosen_opts = $('.chosen-select').val();
    if (chosen_opts !== null) {
      chosen_opts = chosen_opts.join('');
    }
    doSearchAndFilter(chosen_opts);
  });

  $('.chosen-select').chosen();

  // finally, do default search (filter on featured)
  doSearchAndFilter('[data-featured*=1]');
});


function doSearchAndFilter(filterSpec) {
  var container = $('.extensions');
  container.find('.record').hide();
  if (filterSpec) {
    container.find('.record' + filterSpec).show();
  } else {
    container.find('.record').show();
  }

  var matchCount = $('.record:visible').length;
  var $count = $('.js-result-count');
  // fadeout => fadein so as to highlight the change
  $count.fadeOut(function() {
    $count.text(matchCount);
    $count.delay(100).fadeIn('slow');
  });
}


function setupFilters(){
  var container = $('.extensions');
  var filters = {type: {}, status: {}};

  container.find('.record').each(function() {
    // Find the current extension's detail URL
    var record = $(this);

    // de-duplicate filter values
    $.each(filters, function (filter_type) {
      var filter_vals = record.data(filter_type).split(';');
      $.each(filter_vals, function(ignore, filter_val) {
        k = toFilterName(filter_val);
        if (!(k in filters[filter_type]) && k !== '') {
          filters[filter_type][k] = filter_val;
        }
      });
    });
  });

  // create filter options
  $.each(filters, function(filter_type, filter) {
    var chosen_group = $('<optgroup label="' + filter_type.substr(0,1).toUpperCase() + filter_type.substr(1) + '">');
    $.each(filter, function(k, v) {
      // the '*=' here is a hack. if a filter value is a substring of
      // another (e.g. java and javascript) this will go wrong.
      chosen_group.append('<option value="[data-' + filter_type + '*=' + v + ']">' + v + '</option>');
    });
    chosen_select.append(chosen_group);
  });

  // Parse filter title
  function toFilterName(title) {
    return title.trim().toLowerCase();
  }
}

