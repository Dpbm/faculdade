console.log("Testing Closure with function () {}")
func = function(){
  let a = 10;
  inner_func = function (){
    return a;
  }

  return inner_func;
}

f = func();
console.log(`value from f: ${f()}`);


console.log('------------------------------');

console.log("Testing Closure with () => {}");
func = () => {
  let a = 10;
  inner_func = () => {
    return a;
  }

  return inner_func;
}

f = func();
console.log(`value from f: ${f()}`);
