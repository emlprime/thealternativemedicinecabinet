$(document).ready(function () {
    $('.toggle_target').hide();
    $('.toggle').click(function (event) {
        if($(event.target).parent().hasClass('closed')) {
            $(event.target).text('Hide Details');
            $(event.target).parent().addClass('open');
            $(event.target).parent().removeClass('closed');
            $(event.target).parent().find('.toggle_target').show();
            $(event.target).parent().find('.teaser').hide();
        }
        else {
            $(event.target).text('Read More');
            $(event.target).parent().addClass('closed');
            $(event.target).parent().removeClass('open');
            $(event.target).parent().find('.toggle_target').hide();
            $(event.target).parent().find('.teaser').show();
        }
    })

});
