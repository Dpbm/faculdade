const answers = document.querySelectorAll("div.markdown");
const questions = document.querySelectorAll("div.user-message-bubble-color");

const total = questions.length;

let outHTML = "";

for(let i = 0; i < total; i++){
    outHTML += questions[i].innerHTML;
    outHTML += answers[i].innerHTML;
}

function downloadString(text, fileType, fileName) {
  //https://gist.github.com/danallison/3ec9d5314788b337b682
  var blob = new Blob([text], { type: fileType });

  var a = document.createElement('a');
  a.download = fileName;
  a.href = URL.createObjectURL(blob);
  a.dataset.downloadurl = [fileType, a.download, a.href].join(':');
  a.style.display = "none";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(function() { URL.revokeObjectURL(a.href); }, 1500);
}

downloadString(outHTML, "text/html", "genome.html");
