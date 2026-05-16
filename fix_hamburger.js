const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    
    // Check if hamburger.js is already included
    if (!content.includes('hamburger.js')) {
        // insert before </body>
        content = content.replace('</body>', '    <script src="hamburger.js"></script>\n</body>');
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log(`Added hamburger.js to ${file}`);
    }
});
