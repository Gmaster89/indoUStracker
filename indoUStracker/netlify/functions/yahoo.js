const https = require('https');

exports.handler = async function(event, context) {
    const symbols = event.queryStringParameters.symbols;
    
    if (!symbols) {
        return { 
            statusCode: 400, 
            body: JSON.stringify({ error: 'No symbols provided' }),
            headers: { 'Access-Control-Allow-Origin': '*' }
        };
    }

    const url = `https://query1.finance.yahoo.com/v7/finance/quote?symbols=${symbols}`;

    return new Promise((resolve) => {
        https.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'application/json'
            }
        }, (res) => {
            let data = '';
            
            res.on('data', chunk => {
                data += chunk;
            });
            
            res.on('end', () => {
                resolve({
                    statusCode: res.statusCode,
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    },
                    body: data
                });
            });
        }).on('error', (err) => {
            resolve({
                statusCode: 500,
                headers: { 'Access-Control-Allow-Origin': '*' },
                body: JSON.stringify({ error: 'Failed fetching data from Yahoo Finance', details: err.message })
            });
        });
    });
};
