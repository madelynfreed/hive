$('myForm').submit(function(e){
	var postData = $(this).serializeArray();
	var formUrl = $(this).attr('action');

	$.ajax(
	{
		url: formURL,
		type: "POST",
		data: postData,
		success: function(data, textStatus, jqXHR)
		{
			document.write(data)
		}
	});
	e.preventDefault();
	e.unbind();	
});

$("myForm").submit();