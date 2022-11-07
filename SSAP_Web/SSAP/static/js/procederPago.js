var stripe = Stripe('pk_test_51M1Iv7LIZZcOrtrucy46lBWVAe2AyYHzKCRWjrZnQnVq8YqdyudhK2P7gUY2Too0HtAyo5BncNOrr1YoCY9jrQ2k00tVjXjITo');

$(document).ready(function(){
    var elements = stripe.elements();
    var style = {
        base: {
            color: "#32325d",
            fontSize:'20px'
        }
    };
    var card = elements.create("card", { style: style});
    card.mount("#card-element");

    card.on('change', function(event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
          displayError.textContent = event.error.message;
          $("#btnSubmit").prop( "disabled", true );
        } else {
          displayError.textContent = '';
          $("#btnSubmit").prop( "disabled", false );
        }
    });

    // Create a token or display an error when the form is submitted.
    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
    event.preventDefault();

        stripe.createToken(card).then(function(result) {
            if (result.error) {
            // Inform the customer that there was an error.
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
            } else {
            // Send the token to your server.
            stripeTokenHandler(result.token);
            }
        });
    });

    function stripeTokenHandler(token) {
        // Insert the token ID into the form so it gets submitted to the server
        var form = document.getElementById('payment-form');
        var hiddenInput = document.createElement('input');
        hiddenInput.setAttribute('type', 'hidden');
        hiddenInput.setAttribute('name', 'stripeToken');
        hiddenInput.setAttribute('value', token.id);
        form.appendChild(hiddenInput);
        
        // Submit the form
        form.submit();
    }
});