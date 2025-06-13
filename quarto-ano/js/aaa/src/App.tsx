import { ChangeEventHandler, useState } from "react";
import "./index.css";

const regex = new RegExp(/({( *[0-9]+ *: *1(\.0*)? *)|(( *[0-9]+ *: *0(\.[0-9]*)? *, *)+( *[0-9]+ *: *0(\.[0-9]*)? *))|(( *['"][01]+['"] *: *[0-9]+ *, *)+( *['"][01]+['"] *: *[0-9]+ *))})|(\[( *[0-9]+(\.[0-9])* *, *)*( *[0-9]+(\.[0-9])* *)\])/g);

export function App() {
  const [value, setValue] = useState("");
  return (
    <div className="h-screen flex flex-col items-center justify-center">
      <textarea onChange={(v) => setValue(v.target.value)} className="border">
      </textarea>
      <button onClick={() => alert(regex.test(value))} className="border">send</button>
    </div>
  );
}

export default App;
