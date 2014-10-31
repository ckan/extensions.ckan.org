jQuery(document).ready(function($) {
  var container = $('.extensions');
  var chosen_select = $('.chosen-select');
  var $form = $('form.js-search');

  // make form visible - will not work if no javascript
  $(".form-inline").removeClass("hidden");

  // triggered when the form text is changed
  $form.on('change submit', function(e) {
    e.preventDefault();

    var q = $form.find('input[name="q"]').val();
    var chosen_opts = $('.chosen-select').val();
    if (chosen_opts !== null) {
      chosen_opts = chosen_opts.join('');
    }
    doSearchAndFilter({
      q: q,
      filters: chosen_opts
    });
  });

  $('.chosen-select').chosen();

  // finally, do default search (filter on featured)
  doSearchAndFilter({
    q: '',
    filters: ''
  });
});


function doSearchAndFilter(query) {
  var container = $('.extensions')
    cssMatch = '.record'
    $count = $('.js-result-count');
    regex = new RegExp(query.q, 'im')
    ;

  // could have a race here but guess second will take longer so we do not chain
  $count.fadeOut('slow');
  container.find(cssMatch).hide('slow', function() {
    if (query.filters) {
      cssMatch += query.filters;
    }
    container.find(cssMatch).each(function(idx, record) {
      var $record = $(record)
        , title = $record.find('h2').text()
        ;
      if (!(query.q) || title.match(regex)) {
        // can not show slow here as we get into race with count condition below
        $(record).show();
      }
    });

    var matchCount = $('.record:visible').length;
    // fadeout => fadein so as to highlight the change
    $count.text(matchCount);
    $count.fadeIn('slow');
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

