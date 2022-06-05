Due date: June 12, 2021, 11:59pm
Form validation is a way for you to tell the user what kind of input is required in each field and allows you to notify the user when the input is incorrect. There are many ways to do form validation (via HTML, client-side scripting or server-side scripting). In this assignment, you will use Javascript and write a plugin that displays information/error messages next to input fields.

Requirements

The code files for form validation are validate.html, validate.css and validate.js. You will only modify validate.js.

The validation rules are as follows:
•	The email field should be a valid email address (abc@def.xyz). A valid email consists of an email prefix and an email domain with two parts. <prefix>@<domain_part1>.<domain_part2>
•	The password field should contain at least six characters.
•	Password and confirm password fields should match.

When the field is currently being edited (focus event), a notification element will appear below the input field and will display information message (i.e. password should include at least six characters etc). When the field loses focus (blur event), information message will be hidden.

When the form is submitted, if there is any problem with any input field, that element will be highlighted (change class to “error”) and an error message will be shown right below the corresponding input element (i.e. You should enter at least six characters, passwords do not match etc).
When passwords do not match, highlight both password fields and show error message below confirm password field.

When user starts editing any highlighted field, remove “error” class from corresponding element.

You should use the form events functions to detect when a form field gains or loses focus. You should not use mouse and keyboard events such as click or keydown: there are multiple ways to give a form field focus, and it is difficult to detect all of them reliably using mouse and keyboard events. Span elements can be added using element creation and DOM insertion.



For validating email, you will need to write regular expressions. 
Although you will use JS validation and not HTML, you can use email validation rule or pattern from below page.
https://www.w3schools.com/tags/att_input_pattern.asp

Submission:
Zip your validate.js file and send it through eLearning. Do not include html and css files (remember you are not making any changes on those files). The name of the zip file should be PW2-yournetid.zip.
