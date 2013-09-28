//= require_self

$(document).ready(function(){



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

});