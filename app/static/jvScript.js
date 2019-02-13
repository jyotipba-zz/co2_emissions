$(document).ready(function(){

    $("#showCountry").click(function(){
        $("#countryForm").toggle();             // To show and hide the form for searching country
        });


      $('form').submit( function(e){
        $.ajax(
          {
            type: "POST",
            url: "/graph",
            dataType:'html',
            data: $('form').serialize(), // serializes the form's elements.
            success: function (data)
              {
                //console.log(data.co2)  // display the returned data in the console.
                $("#results").html(data);
              },
              error: function()
              {
                  $("#results").text('error occurred');
              }
           });

        e.preventDefault();

      });
});
