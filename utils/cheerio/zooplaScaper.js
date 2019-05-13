const request = require('request');
const cheerio = require('cheerio');

const url3 = 'https://www.zoopla.co.uk/for-sale/property/london/dagenham/?price_max=425000&q=Dagenham%2C%20London&results_sort=newest_listings&search_source=home'

request(url3, (error, response, html) => {
    if(!error && response.statusCode == 200){
       const $ = cheerio.load(html);

        $('.listing-results-wrapper').each((i, el) => {
            const title = $(el).find('.listing-results-attr').children('a').text().replace(/\s\s+/g, '')
            const price = $(el).find('.text-price').text().replace(/\s\s+/g, '');
            const address = $(el).find('.listing-results-address').text().replace(/\s\s+/g, '')
            const desc = $(el).find('.listing-results-right').children('p').text().replace(/\s\s+/g, '')
            const listed = $(el).find('.top-half').text().replace(/\s\s+/g, '')
            const link = $(el).find('a').attr('href');

            const zooplaData = [{
                Title: title,
                Price: price,
                Address: address,
                Description: desc,
                Listed: listed,
                Thumbnail: thumbNail,
                Link: link
            }]
        });
    }
});
