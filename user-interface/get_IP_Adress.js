const { networkInterfaces } = require('os');
const fs = require('fs');

var package_json;



const nets = networkInterfaces();
const results = Object.create(null); // Or just '{}', an empty object

//read file -> when done then get IP address -> replace the ip address then write in the package.json
fs.readFile('package.json', (err, read_data) => {
    //read the JSON file 
    if (err) throw err;
    package_json = JSON.parse(read_data);
    
    // then read local machine IP address 
    for (const name of Object.keys(nets)) {
        for (const net of nets[name]) {
            // Skip over non-IPv4 and internal (i.e. 127.0.0.1) addresses
            if (net.family === 'IPv4' && !net.internal) {
                if (!results[name]) {
                    results[name] = [];
                }
                results[name].push(net.address);
            }
        }
    }

    try {
        package_json["config"]["myUrl"] = "http://"+results["en0"][0];
      } catch (error) {
        package_json["config"]["myUrl"] = "http://"+results["Wi-Fi"][0];
      }
      
    package_json["config"]["myUrl"] = "http://"+results["en0"][0];

    //write data to JSON file 
    let written_data = JSON.stringify(package_json, null, 2);
    fs.writeFile('package.json', written_data, (err) => {
        if (err) throw err;
        console.log('Data written to file');
    });
});






