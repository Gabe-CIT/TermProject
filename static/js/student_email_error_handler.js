/*
This is genuinely one of the most barebones things I could have ever coded in JS, but atleast it sort of works.

An eye sore :(((
 */

document.addEventListener("DOMContentLoaded", function () {
    const emailField = document.querySelector("input[name='email_address_data']");
    
    emailField.addEventListener('input', function () {
        let emailValue = emailField.value;

        if (!emailValue.includes("@my.bcit.ca")) {
            emailField.classList.add("invalid-email");
            emailField.setAttribute("title", "Invalid email. Must contain an @ symbol.");
            // id like some more checks here, but this atleast gives some user feedback :)
        } else {
            emailField.classList.remove("invalid-email");
            emailField.removeAttribute("title", "Invalid email. Must contain an @ symbol.");
        }; 
    });
});