export default class DB {
  lastId = 9;

  data = [
    {
      id: 0,
      nome: "Caixa de Lápis de Colorir 24 cores",
      marca: "FaberCastel",
      preco: 30.5,
      quantidadeEstoque: 100,
      categoria: "Escolar",
    },
    {
      id: 1,
      nome: "Caderno Brochura 200 folhas",
      marca: "Tilibra",
      preco: 20.0,
      quantidadeEstoque: 20,
      categoria: "Escolar",
    },
    {
      id: 2,
      nome: "Lápis HB Número 2.",
      marca: "Leo&Leo",
      preco: 1.5,
      quantidadeEstoque: 200,
      categoria: "Escolar",
    },
    {
      id: 3,
      nome: "Caixa de Clips de Papel 50 unidades",
      marca: "clipes",
      preco: 15.0,
      quantidadeEstoque: 145,
      categoria: "Escritório",
    },
    {
      id: 4,
      nome: "Caneta Esferográfica Azul",
      marca: "Bic",
      preco: 2.0,
      quantidadeEstoque: 500,
      categoria: "Escritório",
    },
    {
      id: 5,
      nome: "Notas autoadesivas 50 folhas",
      marca: "PostIt",
      preco: 5.0,
      quantidadeEstoque: 100,
      categoria: "Escritório",
    },

    {
      id: 6,
      nome: "Pasta Elástico",
      marca: "CIS",
      preco: 8.5,
      quantidadeEstoque: 40,
      categoria: "Organização",
    },
    {
      id: 7,
      nome: "Fichario",
      marca: "Erik",
      preco: 40.8,
      quantidadeEstoque: 10,
      categoria: "Organização",
    },
    {
      id: 8,
      nome: "Envelope",
      marca: "Ciapel",
      preco: 3.2,
      quantidadeEstoque: 600,
      categoria: "Organização",
    },
  ];

  add(newItem) {
    this.data.push({ ...newItem, id: this.lastId });
    return this.lastId++;
  }

  remove(id) {
    this.data = this.data.filter((d) => d.id != id);
  }

  getAll() {
    return this.data;
  }

  getById(id) {
    return this.data.filter((d) => d.id == id);
  }

  static createItem(data) {
    return {
      nome: data["nome"] || null,
      categoria: data["categoria"] || null,
      marca: data["marca"] || null,
      preco: data["preco"] || null,
      quantidadeEstoque: data["quantidadeEstoque"] || 0,
    };
  }
}
