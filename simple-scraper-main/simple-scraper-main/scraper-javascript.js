/**
 * scraper-javascript.js
 * To run this script, copy and paste `node scraper-javascript.js` in the terminal
 */

const cheerio = require('cheerio');

(async () => {
  const url = 'https://l.facebook.com/l.php?u=https%3A%2F%2Fstarlink.com%2Faccount%2Fservice-line%2FAST-2293597-46342-54%3FselectedDevice%3Dut01000000-00000000-0060d786%26page%3D0%26limit%3D5%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExQ3ZtRFMxZ3VMeENkdmtwQ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR76Uh3e4C-cNmoCQ2oZxxAj9qdIiRCIsuZg_ZABlT1S-eovJNmlxAAuiLoA0A_aem_YWdncwCjOHup56qgx0veSiTN-Bsh%26brid%3DYWdncwGWfb0jThlfAln8tzQv4WsD&h=AUCZ8qv32qec0hTmElncvA3VOsLJX7_u9nwc5sLmEyIIS3NwxJRHlYqYJ3ZlihcCEspFtAVUNNMAab4yQiHvWMeSFbxVOp0V3PBtq_qVsvjAA_Bx3VoDQaBvhebhcc-ETps4gg';
  const response = await fetch(url);

  const $ = cheerio.load(await response.text());
  console.log($.html());

  const title = $('h1').text();
  const text = $('p').text();
  const link = $('a').attr('href');

  console.log(title);
  console.log(text);
  console.log(link);
})();