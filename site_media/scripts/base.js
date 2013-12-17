CODES = ['headstart']
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
	    });
	$('.discount_code_target').click( function(event) {
		$("#discount_code_form").show();
		$("#discount_code_form").css("top", event.pageY)
		$("#discount_code_form").css("left", event.pageX)
	    });
	$("#use_discount").click( function(event) {
		event.preventDefault();
		$("#discount_code_form").hide();
		var code = $("#discount_code_form input").val();
		if (CODES.indexOf(code) == -1) {
		    return
		}
		var buttons = $(document).find(".buy_book_button");
		$.each(buttons, function() {
			if($(this).hasClass(code)) {
			    $(this).show();
			} else {
			    $(this).hide();
			}
		    });
	    });
    });
