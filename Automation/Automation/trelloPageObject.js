var url 		= 'https://trello.com/';
var logInPageButton 	= '=Log In';
var usernameInput 	= '#user';
var passwordInput 	= '#password';
var logInActionButton 	= '#login';
var memberInitials 	= '.member-initials';
var errorMessage 	= '.error-message';


exports.login = function(username, password) {
	browser.url(url);
	browser.click(logInPageButton);
	browser.waitForVisible(usernameInput, 10000);
	browser.setValue(usernameInput, username);
	browser.setValue(passwordInput, password);
	browser.click(logInActionButton,0,0);
}

exports.waitForError = function(){
	browser.waitForVisible(errorMessage, 10000);
}
exports.errorExists = function(){
	return browser.isExisting(errorMessage);
}


exports.waitForInitials = function(){
	browser.waitForVisible(memberInitials, 10000);
}
exports.initialsExist = function(){
	return browser.isExisting(memberInitials, 10000);
}
