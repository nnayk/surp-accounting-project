var request = require('request');

const _apiUrl='https://faceapi.mxface.ai/api/v3/face/';
const _subscriptionKey="0ZQKcVm0wAGFABr8Vj-FzVA4eN9Gh1711";//change subscription key

var fs = require('fs');
async function base64Encode(file) { 	
    var body = fs.readFileSync(file);
    return body.toString('base64');
}
var base64SingleFace = base64Encode('Leonardo.jpg');
var base64MultipleFace = base64Encode('Leonardo2.jpg');

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

async function classify(api,encodedImage,oldPath) {
	request(await getRequestOption(api,encodedImage), async function (error, response) {
		if (error) {
			console.log(error)
		}
		else {
			console.log("Response /"+api);
			if(response.statusCode == 200) {
				// res = JSON.parse(response.body.faces);
				// console.log('res type = ',typeof response.body.faces,response.body.faces,response.body.faces[0]["faceAnalytics"]["gender"]);
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
				// console.log(response.body.faces);
				// var faces=response.body;
				// for(var face of faces.faces){
				// 	console.log("Face Quality : " + face.quality);
				// }
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
	// for (let i = 0; i < 5; i++) {
	// 	console.log(`hi ${i}`);
	// 	if(i%2 == 0) await sleep(2000);
	//   }
	let total = 0;
	const files = await fs.promises.readdir(".");
	let count = 0;
	for (const file of files)
	{
		if(count == 100) break;
		if(count % 10 == 0) await sleep(30000);
		count++;
		if(file.slice(-4) !== 'jpeg') continue;
		let oldPath = file;
		console.log(oldPath)
		let encoded_image = await base64Encode(oldPath);
		// console.log(encoded_image);
		total += classify("analytics", encoded_image,oldPath).then(gender => console.log('hello',gender));
	}

	console.log(`Identified ${total} pics.`);
}

function sleep(ms) {
	return new Promise((resolve) => {
	  setTimeout(resolve, ms);
	});
  }

main()

// var base64SingleFace = base64Encode('Leonardo.jpg');
// gender = await sendRequest("analytics", base64SingleFace);
// console.log('hello',gender);
