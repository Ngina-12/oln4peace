const sharp = require('sharp');

const input = 'OLN HOMEPAGE.png'; 
const output = 'OLN HOMEPAGE.webp';

sharp(input)
  .webp({ 
    quality: 90,        // Higher quality for text to keep it sharp
    lossless: false,    // 'false' is usually smaller, but try 'true' if the text looks blurry
    nearLossless: true  // Great for keeping text crisp without the huge file size
  })
  .toFile(output)
  .then(info => {
    console.log('Success! Text layer is now a WebP.');
    console.log(`New size: ${(info.size / 1024).toFixed(2)} KB`);
  })
  .catch(err => console.error('Error:', err));