
Due date: June 19, 11:59pm
In this practice work, you will create todo list by using HTML, CSS and JQuery as shown in question.png.

 


Requirements:

When user clicks on the + icon, it will toggle between showing and hiding the textbox which is used to insert a new item to the list. 

When user focuses on the textbox, it will change the border color of the textbox (any color) and when user presses the enter key, it will add the item to the list.

When user hovers over any todo item, it will show delete button and when clicked on the delete button, will delete the item from the list. 

When user clicks on the todo item, it will strike through the item and show it as completed.



Source for icons: 

<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.css">

<i class="fa fa-plus">
<i class="fa fa-trash"></i>


You can use different icons from a different source.


Solution Hint:

1. You can use below HTML code for your initial list.

<ul>
	<li><span><i class="fa fa-trash"></i></span> Meet TAs</li>
	<li><span><i class="fa fa-trash"></i></span> Post grades</li>
	<li><span><i class="fa fa-trash"></i></span> PTA meeting</li>
</ul>

2. Define the width and height of the span element as 40px  and initially hide it. Set display: inline-block to see affect of changing width and height for the element. Set background color as red, font color as white and text-align to center. 
You don’t have to have exact same user interface, your work will be graded based on functionality but these settings will help you to have a similar look.


3. Define mouseenter event for li element (ul.on(“mouseenter”. “li”, function(){}) for showing the trash bin, and mouseleave for hiding the bin.

https://api.jquery.com/mouseenter/#mouseenter-handler

https://api.jquery.com/mouseleave/#mouseleave-handler

4. For actually hiding and showing the trash bin, you can use show() and hide() or fadeIn() and fadeOut().

$(this).find(“span”).show();

$(this) will give current li element.


Submission:
Zip your html, css, and js files together (PW3-yournetid.zip) and send through eLearning.

Note: If you are using external css and js, make sure you use relative path (not absolute) for file references.
