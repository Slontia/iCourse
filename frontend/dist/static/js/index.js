function clearNavActive()
{
	$("#home").removeClass("active");
	$("#course").removeClass("active");
	$("#contact").removeClass("active");
}

function a()
{
	alert("按钮调用成功!");
}

function loginModal()
{
	$("#regBtn").removeClass("btn-primary");
	$("#regBtn").addClass("btn-default");
	$("#logBtn").removeClass("btn-default");
	$("#logBtn").addClass("btn-primary");
	$("#regModal").hide();
    $("#logModal").show();
}

function registerModal()
{
	$("#logBtn").removeClass("btn-primary");
	$("#logBtn").addClass("btn-default");
    $("#regBtn").removeClass("btn-default");
	$("#regBtn").addClass("btn-primary");
	$("#logModal").hide();
    $("#regModal").show();	
}