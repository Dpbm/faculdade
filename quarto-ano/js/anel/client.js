import net from 'node:net';

const connection = net.createConnection({port:4000}, () => {
    
    connection.write("aaa");
    connection.end();
    connection.destroy();
});
