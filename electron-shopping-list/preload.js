// Preload needed node_modules to use in other processes than main renderer process.
// This is because you can't use node in browser. (require() for ex.)
// nodeIntegration = false (Electron v5 and later)

const {
    contextBridge,
    ipcRenderer
} = require("electron");

let validChannels = ["item:add", "item:clear", "window:add"];
// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld(
    "api", {
        send: (channel, data) => {            
            if (validChannels.includes(channel)) {
                ipcRenderer.send(channel, data);
            }
        },
        receive: (channel, func) => {
            if (validChannels.includes(channel)) {
                ipcRenderer.on(channel, (event, ...args) => func(event, ...args) );
            }
        }
    }
);