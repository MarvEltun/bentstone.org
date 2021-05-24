$("#menu-btn").click(function() {
	$("#menu-btn").toggleClass("opened");

	if (!$(".menu-overlay").hasClass("size")) {
		$(".menu-overlay").toggleClass("size");
		$(".menu-overlay").toggleClass("show");
	}

	else if ($(".menu-overlay").hasClass("size")) {
		$(".menu-overlay").toggleClass("show");
		setTimeout(function() {
			$(".menu-overlay").toggleClass("size");
		}, 300);
	}
});

function closeMenu() {
	$("#menu-btn").toggleClass("opened");

	if (!$(".menu-overlay").hasClass("size")) {
		$(".menu-overlay").toggleClass("size");
		$(".menu-overlay").toggleClass("show");
	}

	else if ($(".menu-overlay").hasClass("size")) {
		$(".menu-overlay").toggleClass("show");
		setTimeout(function() {
			$(".menu-overlay").toggleClass("size");
		}, 300);
	}
}