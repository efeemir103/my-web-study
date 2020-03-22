const electron = require('electron');
const url = require('url');
const path = require('path');

// Remove DevTools.
process.env.NODE_ENV = 'production';

// Deconstruct app, BrowserWindow, Menu and inter-process-communication objects.
const {app, BrowserWindow, Menu, ipcMain} = electron;

let mainWindow;
let addWindow;

// Listen for app to be ready.
app.on('ready', async function() {
    // Create new window.
    mainWindow = new BrowserWindow({
        webPreferences: {
            nodeIntegration: false, // is default value after Electron v5
            contextIsolation: true, // protect against prototype pollution
            enableRemoteModule: false, // turn off remote
            preload: path.join(__dirname, "preload.js") // use a preload script
        }
    });
    // Load html into window.
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol: 'file:',
        slashes: true
    }));
    // or just
    // mainWindow.loadFile('mainWindow.html');
    
    // Build menu from template.
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);

    // Insert menu.
    Menu.setApplicationMenu(mainMenu);

    // Quit app when closed.
    mainWindow.on('closed', function() {
        app.quit();
    });
});

// Handle create add window.
function createAddWindow() {
    // Create new window.
    addWindow = new BrowserWindow({
        width: 300,
        height: 200,
        title: 'Add Shopping List Item',
        webPreferences: {
            nodeIntegration: false, // is default value after Electron v5
            contextIsolation: true, // protect against prototype pollution
            enableRemoteModule: false, // turn off remote
            preload: path.join(__dirname, "preload.js") // use a preload script
        }
    });
    // Load html into window.
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'addWindow.html'),
        protocol: 'file:',
        slashes: true
    }));
    // or just
    // addWindow.loadFile('addWindow.html');  

    // Garbage collection handle.
    addWindow.on('closed', function() {
        addWindow = null;
    })
}

// Catch item:add.
ipcMain.on('item:add', function(e, item) {
    mainWindow.webContents.send('item:add', item);
    addWindow.close();
});

// Catch window:add.
ipcMain.on('window:add', function() {
    createAddWindow();
});

// Create menu template.
const mainMenuTemplate = [
    {
        label: 'File',
        submenu: [
            {
                label: 'Add Item',
                click() {
                    createAddWindow();
                }
            },
            {
                label: 'Clear Items',
                click() {
                    mainWindow.webContents.send('item:clear');
                }
            },
            {
                label: 'Quit',
                // Hotkey to quit.
                accelerator: process.platform == 'darwin' ? 'Command+Q' : 'Ctrl+Q',
                click() {
                    app.quit();
                }
            }
        ]
    }
]

// If mac, add empty object to menu.
if(process.platform == 'darwin') {
    // Add empty object to beginning.
    mainMenuTemplate.unshift({});
}

// Add developer tools item if not in production.
if(process.env.NODE_ENV !== 'production') {
    mainMenuTemplate.push({
        label: 'Developer Tools',
        submenu: [
            {
                label: 'Toggle DevTools',
                accelerator: process.platform == 'darwin' ? 'Command+I' : 'Ctrl+I',
                click(item, focusedWindow) {
                    focusedWindow.toggleDevTools();
                }
            },
            {
                role: 'reload'
            }
        ]
    })
}