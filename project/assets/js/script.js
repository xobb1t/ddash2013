//= require_self

$(document).ready(function(){


// edit name
  (function(){
    var $edit_name = $('#js-edit-name'),
        $field = $('.field input', $edit_name);

    $field.focus(function(){
      $edit_name.addClass('edit');
    });

    $field.blur(function(){
      $edit_name.removeClass('edit');
    });
  }());

// tooltips
  (function(){
    var item = $('[data-tooltip]');

    console.log(item);

  }());

});