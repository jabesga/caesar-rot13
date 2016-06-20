$(document).ready(function() {
  $('input[type=submit]').click(function(){
    var form_data = JSON.stringify({
      "key": parseInt($('input[name=key]').val()),
      "sentence": $('input[name=sentence]').val()
    });

    if($(this).attr('id') == "encrypt-btn"){
      $.ajax({
        url: '/encrypt/',
        type: 'POST',
        contentType: 'application/json',
        data: form_data,
        success: function(data){
          $(".result").html("<strong>" + data + "</strong>");
        }
      });
    }
    if($(this).attr('id') == "decrypt-btn"){
      $.ajax({
        url: '/decrypt/',
        type: 'POST',
        contentType: 'application/json',
        data: form_data,
        success: function(data){
          $(".result").html("<strong>" + data + "</strong>");
        }
      });
    }
    return false;
  });
});
