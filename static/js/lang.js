$("#lang-btn").click(function() {
	$("#lang-en").toggleClass("hide-lang");
	$("#lang-az").toggleClass("hide-lang");
	$("#lang-ru").toggleClass("hide-lang");
	$("#lang-tr").toggleClass("hide-lang");
	$("#lang-en").parent().toggleClass("a-lang");
	$("#lang-az").parent().toggleClass("a-lang");
	$("#lang-ru").parent().toggleClass("a-lang");
	$("#lang-tr").parent().toggleClass("a-lang");
});

$("#lang-btn-sm").click(function() {
	$("#lang-en-sm").toggleClass("hide-lang");
	$("#lang-az-sm").toggleClass("hide-lang");
	$("#lang-ru-sm").toggleClass("hide-lang");
	$("#lang-tr-sm").toggleClass("hide-lang");
});