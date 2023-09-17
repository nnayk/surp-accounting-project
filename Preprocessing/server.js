var request = require('request');

const _apiUrl=process.env.URL;
const _subscriptionKey=process.env.KEY;//change subscription key

var fs = require('fs');

/* encode the image */
async function base64Encode(file) { 	
    var body = fs.readFileSync(file);
    return body.toString('base64');
}

/* return the api request options */
async function getRequestOption(api,encodedImage) {
	var options = {
		url: _apiUrl + api,
		method: 'POST',
		headers: {
			'subscriptionkey': _subscriptionKey,
			'Content-Type': 'application/json'
		},
		json: {
			encoded_image:encodedImage
		},
		rejectUnauthorized: false,
	};
	return options	
}

/* return the gender specified in the given api response */
async function get_gender(response,file)
{
	try
	{
		return response.body.faces[0]["faceAnalytics"]["gender"];
	}catch
	{
		console.log('error with ',file);
		return null;
	}
}

/* make the api request and  move the image to the correct gender folder */
async function classify(api,encodedImage,oldPath) {
	request(await getRequestOption(api,encodedImage), async function (error, response) {
		if (error) {
			console.log(error)
		}
		else {
			console.log("Response /"+api);
			if(response.statusCode == 200) {
				gender = await get_gender(response,oldPath);
				console.log('inny',gender);
				if (gender === "Male")
				{
					fs.rename(oldPath, `../Headshots/Male/${oldPath}`, function (err) {
						if (err) throw err
						console.log(`Identified ${oldPath} as Male.`)
					});

					return 1;
				}
				else if (gender === "Female")
				{
					fs.rename(oldPath, `../Headshots/Female/${oldPath}`, function (err) {
						if (err) throw err
						console.log(`Identified ${oldPath} as Female.`)
					});
					return 1;
				}
				else
					console.log('error');
			}
			else{
				console.log("Error :");
				console.log(response.body);
			}
		}
	});

	return 0;

	console.log('done')

}

async function main()
{
	let total = 0;
	const files = await fs.promises.readdir(".");
	let count = 0;
        /* identify gender for each image */
	for (const file of files)
	{
		if(count == 100) break;
		if(count % 10 == 0) await sleep(30000);
		count++;
		if(file.slice(-4) !== 'jpeg') continue;
		let oldPath = file;
		console.log(oldPath)
		let encoded_image = await base64Encode(oldPath);
		total += classify("analytics", encoded_image,oldPath).then(gender => console.log('hello',gender));
	}

	console.log(`Identified ${total} pics.`);
}

/* Wait for next api request cycle */
function sleep(ms) {
	return new Promise((resolve) => {
	  setTimeout(resolve, ms);
	});
  }

main()
