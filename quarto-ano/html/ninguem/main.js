const images = ["./img/1.png", "./img/2.png"];


const circuit = document.querySelector("#circuit");
const options = document.querySelector("#options");

function startImageDrag(ev){
    const imgSrc = ev.target.src;

    const img = new Image();
    img.src = imgSrc;
    ev.dataTransfer.setDragImage(img,10,10);
}

circuit.addEventListener('dragover', (ev) => {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = 'copy';
});

circuit.addEventListener('drop', (ev) => {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('image');
    console.log(data);
    ev.target.appendChild(data);
});

window.addEventListener('DOMContentLoaded', () => {



    for(const img of images){
        const imgElement = document.createElement("img");
        imgElement.src = img;
        imgElement.addEventListener('dragstart', startImageDrag);

        options.appendChild(imgElement);
    }
});