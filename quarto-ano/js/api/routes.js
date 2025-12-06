import DB from "./db.js";

export default class Routes {
  constructor(database) {
    this.db = database;
  }

  getProducts = (_, res) => {
    return res.status(200).json(this.db.getAll());
  };

  deleteProduct = (req, res) => {
    const id = parseInt(req.headers["id"]);

    if (!id) {
      return res.status(400).json({ message: "Invalid ID" });
    }

    this.db.remove(id);

    return res.status(200).json({ message: "Deletede product!" });
  };

  getById = (req, res) => {
    const id = parseInt(req.params["id"]);

    if (!id) {
      return res.status(400).json({ message: "Invalid ID" });
    }

    const data = this.db.getById(id);

    if (data.length <= 0) {
      return res.status(404).json({ message: "Not found!" });
    }

    return res.status(200).json(data[0]);
  };

  addProduct = (req, res) => {
    const incomingData = req.body;
    const data = DB.createItem(incomingData);
    const id = this.db.add(data);

    return res.status(201).json({ id });
  };
}
