import express from "express";

import { PORT } from "./constants.js";
import Routes from "./routes.js";
import DB from "./db.js";

const server = express();

server.use(express.json());

const routes = new Routes(new DB());

server.get("/produtos", routes.getProducts);
server.get("/produtos/:id", routes.getById);
server.post("/produtos", routes.addProduct);
server.delete("/produtos", routes.deleteProduct);

server.listen(PORT, () => console.log("Servidor rodando..."));
