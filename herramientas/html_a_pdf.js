// Uso: node html_a_pdf.js <entrada.html> <salida.pdf> "<título pie>"
const { chromium } = require('playwright');
const [,, html, pdf, titulo] = process.argv;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(html), { waitUntil: 'load' });
  await p.pdf({ path: pdf, format: 'Letter', printBackground: true, displayHeaderFooter: true,
    margin: { top: '18mm', bottom: '18mm', left: '19mm', right: '19mm' },
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-size:8px;width:100%;text-align:center;color:#666">${titulo} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>` });
  await b.close();
})();
