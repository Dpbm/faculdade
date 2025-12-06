import net from 'node:net';

const PORT = 4000;

const server = net.createServer((socket) => {
    socket.on("ready", () => {
        console.log("ready!");
    });

    socket.on("data", (data) => {
        console.log(`[data] ${data}`);
    });

    socket.on("end", () => {
        console.log("finsihed");
        socket.destroy();
        server.close();
        return;
    })
});

server.listen(PORT, () => {
    console.log(`Listening on port: ${PORT}`);
});