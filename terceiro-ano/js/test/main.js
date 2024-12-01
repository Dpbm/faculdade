const bulario = require('bulario');
(async() => {
    const busca = await bulario.pesquisar('dipirona')
    console.log(`\n INFORMAÇÕES DA PESQUISA`, busca)
})();
