$(document).ready(function () {

	// Menu Settings
	$('.menu-icon, .menu-icon-close').click(function (e) {
		e.preventDefault();
		$('.flex-container').toggleClass('active');
	});

	// Search Settings
	$('.search-icon').on('click', function (e) {
		e.preventDefault();
		$('.search-box').toggleClass('search-active');

		if ($('.search-box').hasClass('search-active')) {
			$('.search-icon-close').on('click', function (e) {
				e.preventDefault();
				$('.search-box').removeClass('search-active');
			});
		}
	});

	// LevelBar
	$('.level-bar-inner').css('width', '0');

	$(window).on('load', function () {
		$('.level-bar-inner').each(function () {
			var itemWidth = $(this).data('level');
			$(this).animate({	width: itemWidth	}, 800);
		});

	});

});
