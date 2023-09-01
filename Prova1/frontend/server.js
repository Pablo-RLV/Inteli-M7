const express = require('express');
const app = express();
const path = require('path');

// Serve arquivos estáticos da pasta 'public'
app.use(express.static('public'));

app.get('/', (req, res) => {
    const filePath = path.join(__dirname, 'index.html');
    res.sendFile(filePath);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
