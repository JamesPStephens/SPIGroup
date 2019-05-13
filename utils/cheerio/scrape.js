const request = require('request');
const cheerio = require('cheerio');

request('https://jamespstephens.github.io/Portfolio/', (error, response, html) => {
    if(!error && response.statusCode == 200){
       const $ = cheerio.load(html);

       const introSection = $('.portfolio-ProjectHeader');
    //    console.log(introSection.html());
    //    console.log(introSection.text());
    // const output = introSection.find('h1').text();
    // const output = introSection.children('h1').text();
    // const output = introSection.children('h3').next().text();
    // const output = introSection.children('p').parent().text();

    $('.row a').each((i, el) => {
    //    const item = $(el).text();
       const link = $(el).attr('href');
       console.log(link);
    });
    }
});
