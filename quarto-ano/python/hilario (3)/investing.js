//https://br.investing.com/commodities/real-time-futures    

const trs = document.querySelectorAll('tr.datatable-v2_row__hkEus');
var data = '';

for(const tr of trs){
    const columns = Array.from(tr.children).slice(1);
    const columnNames = columns.map((element) => element.innerText);
    data += columnNames.join(";") + "\n";
}

const blob = new Blob([data], { type: 'text/csv;charset=utf-8;' });
const filename = "data.csv";

if (navigator.msSaveBlob) { 
    navigator.msSaveBlob(blob, filename);
} else {
    var link = document.createElement("a");
    if (link.download !== undefined) { 
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", filename);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}