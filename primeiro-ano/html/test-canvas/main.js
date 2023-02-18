const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

let x = 0;
let y = 0;

const elementSizes = 10;
const totalObjects = 10;

let objectsPositions = [];
let generateObject;

const up    = () => y -= 10;
const down  = () => y += 10;
const left  = () => x -= 10;
const right = () => x += 10;

generateObject = () => {
  let xObjectPosition, yObjectPosition;

  const lo = 10;

  var hiw = canvas.width - (canvas.width % 10);
  var hih = canvas.heigth - (canvas.heigth % 10);

  while(
    JSON.stringify(objectsPositions).includes([xObjectPosition, yObjectPosition]) || 
      !xObjectPosition || 
      !yObjectPosition){
        xObjectPosition = lo + 10 * parseInt(Math.random() * ((hiw - lo)/11));
        yObjectPosition = lo + 10 * parseInt(Math.random() * ((hih - lo)/11));
  }
  
  return [xObjectPosition, yObjectPosition];
}

objectsPositions = Array(totalObjects).fill(undefined).map(generateObject);

const commands = {
  keyW: up,
  keyS: down,
  keyD: right,
  keyA: left
};

function drawObjects(){
  objectsPositions.forEach((position) => {
    context.fillStyle = 'green';
    context.fillRect(position[0], position[1], elementSizes, elementSizes);
  });
}

function drawPlayer(){
  context.fillStyle = 'red';
  context.fillRect(x,y, elementSizes, elementSizes);
}

function draw(){
  context.clearRect(0, 0, canvas.width, canvas.height);
  drawPlayer();
  drawObjects();
}

function checkCollisionObject(){
  const userPosition = JSON.stringify([x, y]);
  const objectsPositionsStr = JSON.stringify(objectsPositions);

  if(objectsPositionsStr.includes(userPosition))
    objectsPositions = objectsPositions.fileter((position) => JSON.stringify(position) !== userPosition);
}

document.addEventListener('keypress', (key) => {
  const {code} = key;

  if(!code) return;

  const actualCommand = commands[code];
  
  actualCommand();

  checkCollisionObject();
  draw();

});

draw();

