# WGGCommute - Adding Commute Times to WG-Gesucht Listings

This is a barebones implementation of a chrome extension that can be used to add commute times directly to listings on WG-gesucht.de. Simply specify a "workplace" location in the options-page of the extension and it will automatically query the Google Maps API for the shortest commute either by walking, driving or biking there from each of the locations on the page.

Currently this implementation is very much a WIP. It does run, however you will need to provide your own Key for the Google Maps API and deploy your own AWS Lamdba function using the included Python script.

I will provide more documentation once this project is more mature - hmu if you have any questions for now.