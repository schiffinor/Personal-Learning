function submitSearch() {
	var search = document.getElementById("searchBar").value;
	eel.fetchSearch(search)(callback);
}
function callback() {
	
}