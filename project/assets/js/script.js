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
    var tooltip = $('<span class="tooltip hidden"></span>');

    $('body').append(tooltip);


    var item = $('[data-tooltip]');

    item.hover(function(){
      var $this = $(this),
          offset = $this.offset(),
          tooltip_str = $this.data('tooltip');

      tooltip.html(tooltip_str);

      tooltip.removeClass('hidden');

      var width = tooltip.innerWidth(),
          width_this = $this.innerWidth(),
          height = tooltip.innerHeight();

      tooltip.css({
        'left': (offset.left - (width / 2)) + (width_this / 2),
        'top': offset.top - height - 10
      })
    }, function(){
      tooltip.addClass('hidden');
    });

  }());

// $change-password
  (function(){
    var change_password = $('#change-password'),
        form = $('.fpassword', change_password);

    $('.open', change_password).click(function(){
      $(this).hide();
      $('.fpassword', change_password).removeClass('hide');
      return false;
    });
  }());

});