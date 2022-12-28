// Javascript //

function CallSort() {
  eel.sort_function();
}

function Help() {
  alert("App to sort your files into folders with the name of the file type.")
}

eel.expose(ShowResult);
function ShowResult(results) {
  alert(results)
}