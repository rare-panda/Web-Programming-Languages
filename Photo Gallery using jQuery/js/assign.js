var res;


$(document).ready(function () {
    $.ajax({
        url: './js/data.json',
        crossDomain: true,
        dataType: "json",
        success: function (result) {
            alert("File loaded successfully");
            res = result;
            res.forEach(element => {
                $('.gallery').append(
                    '<img src="images/square/' + element['path'] + '"' + 
                    ' alt = "' + element['title'] + '"' + '> '
                );
            });
        },
        error: function (e) {
            alert("error loading file");
        }
    });

    $(document).on('mouseenter', 'img', function (e) {
        $(this).addClass('gray');
        var img = res.find(e => {
            return e.title === $(this).attr('alt')
        });
        var bre = "<br />";
        $(document.body).append(
            '<div id="preview">' +  
            '<img src="' + $(this).attr('src').replace('square', 'medium') + '"' +
            ' alt = "' + $(this).attr('alt') + '"' + '> ' + 
            '<p>' + $(this).attr('alt') + bre + img.city + ' ' + img.country + ' ' + img.taken + '</p>' + 
            '</div>'
        );
        $('#preview').css({
            "left": e.pageX,
            "top": e.pageY
        });
        $('#preview').fadeIn(1000);
    });
    $(document).on('mouseleave', 'img', function () {
        $(this).removeClass('gray');
        $('#preview').remove();
    });
    $(document).on('mousemove', document, function (e) {
        $('#preview').offset({
            left: e.pageX,
            top: e.pageY + 20
        });
    });
});