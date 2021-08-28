$( document ).ready( function() {
  $( ".player_update" ).submit(function( event ) {
    event.preventDefault();
    $.ajax({
      url: $(this).attr("action"),
      method: $(this).attr("method"),
      data: $(this).serializeArray(),
      success: function(response) {
        console.log(response)
        alert("success")
      }
    })
  });
})
