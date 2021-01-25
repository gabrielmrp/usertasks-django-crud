
$( document ).ready(function() {

// Execute a function when the user releases a key on the keyboard
window.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    if($('#divAddEntity').css('display')!=="none") 
    	document.getElementById("add").click();
  }
});



$('#add').click(function() {
	var form = $('#formAdd');
	var entity = $('#entity').html(); 
	$.ajax({
	    url: '../../api/'+entity+'/',
	    type: 'POST',
	    data: form.serialize(),
	    beforeSend: function (xhr, settings) {
	        xhr.setRequestHeader("X-CSRFToken", form.attr('csrfmiddlewaretoken'));
	    },
	    success: function (arg) {
	        location.reload()
	    }
	});
	});

$('.delItem').click(function() {
	delItem = $(this).attr('itemid')
	console.log(delItem)
})

$('#del').click(function() {
	 
	var entity = $('#entity').html();

	$.ajax({
	    url: '../../api/'+entity+'/'+delItem,
	    type: 'DELETE', 
	    success: function (arg) {
	        location.reload()
	    }
	});
	});

$('#calladd').click(function() {
	
	 
 	if ( $('#divAddEntity').css('display') === "none" ) {
	  ///$( "#addEntity" ).css({"display":"block"});
	  $('#divAddEntity').show()
	  $("#calladd").html('<i class="fas fa-minus"></i>')
	} else  {
	  //$( "#addEntity" ).css({"display":"none"});
	  $('#divAddEntity').hide()
	  $("#calladd").html('<i class="fas fa-plus"></i>')
	}
});

$('.edit').click(function() {
 
	var entity = $('#entity').html()
	var itemid = $(this).attr('itemid') 
	var form = $("#form_edit_"+itemid)
	var status = form.find('input[name=status]').attr('value')=="pendente"?"feito":"pendente"
 	form.find('input[name=status]').attr({'value':status})
 
	$.ajax({
	    url: '../../api/'+entity+'/'+itemid+'/',//window.location.host+'/api/'+entity+'/',
	    type: 'PUT',
	    data: form.serialize(),
	    beforeSend: function (xhr, settings) {
	        xhr.setRequestHeader("X-CSRFToken", form.attr('csrfmiddlewaretoken'));
	    },
	    success: function (arg) {
	         location.reload()
	    }
	});
	});

$('select').click(function() {
	if($('select').val()=="feito")
		$('select').css({'background':'#28a745'})
	else
		$('select').css({'background':'#ffc107'})
});

});
