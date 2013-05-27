$(document).ready(function () {
    $('.toggle_target').hide();
    $('.toggle').click(function (event) {
        console.log($(event.target).parent());
        if($(event.target).parent().hasClass('closed')) {
            console.log("open me");
            $(event.target).innerHtml='Hide Details';
            $(event.target).parent().addClass('open');
            $(event.target).parent().removeClass('closed');
            console.log($(event.target).parent().find('.toggle_target'));
            $(event.target).parent().find('.toggle_target').show();
        }
        else {
            console.log("close me");
            $(event.target).innerHtml='Read More';
            $(event.target).parent().addClass('closed');
            $(event.target).parent().removeClass('open');
            $(event.target).parent().find('.toggle_target').hide();
        }
    })

});
