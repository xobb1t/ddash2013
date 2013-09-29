//= require_self

$(document).ready(function(){

  var $loader = $('#js-loader');

  function show_loader(block) {
    var w = block.innerWidth(),
        h = block.innerHeight(),
        l = block.offset().left,
        t = block.offset().top;

    $loader.show();

    $loader.css({
      'width': w + 10,
      'height': h + 10,
      'left': l - 5,
      'top': t - 5
    });
  }

// edit name
  (function(){
    var $edit_name = $('#js-edit-name');

    $edit_name.on('keyup', 'input', function(){
      if ($(this).val() === '') {
        $edit_name.removeClass('edit');
      }
      else {
        $edit_name.addClass('edit');
      }
    });

    $edit_name.on('blur', 'input', function(){
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


  function ajax_go(form, block) {
    show_loader(block);

    setTimeout(function(){
      $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function(data) {
          block.html(data);
          $loader.hide();
        }
      });
    }, 500);
  }


  $('#js-edit-name').on('submit', 'form', function(){
    var $this = $(this),
        block = $this.parent();

    if (!$('.field input', $this).val()) { return false; }

    ajax_go($this, block);

    return false;
  });

  $('#js-registration').on('submit', 'form', function(){
    var $this = $(this),
        block = $this.parent();

    ajax_go($this, block);
    return false;
  });

  $('#js-logo-form input').change(function(){
    console.log('Hello');
    $(this).closest('form').submit();
  });

});
