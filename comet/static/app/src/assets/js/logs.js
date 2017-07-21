var logFilter = function(evt) {
    $('.callout').hide();
    evt.preventDefault();
    cls = $('#filter-category option:selected').val();
    $('.' + cls).show();
}


$("#log-filter").click(function(evt){
    logFilter(evt);
});

$("#reset-filter").click(function(evt){
    $('.callout').show();
});

