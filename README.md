This server-sided endpoint provides the following details about a user's live Spotify statistics:

Artist Name |
Image URL |
Playing Status |
Title Name |
Metadata 

The AMM-Spotify-API will return an endpoint such as below:

{
  "artist":"artistname",
  "image":"imageurl",
  "playing":playingstatus(true/false),
  "title":"titlename",
  "updated":metadata
}

For this to work, please aquire your Spotify CLIENT_ID and CLIENT_SECRET from developer.spotify.com. Do not share your keys with anyone else.

Place your Spotify CLIENT_ID on line 7.

Place your Spotify CLIENT_SECRET on line 8.

To have a standard baseline level of security, this enpoint requires an API_KEY, which must be consistent between the target URL and machine. Therefore, you must set a constant string of characters on this value, to ensure your data is only obtained by the target URL, and not be attackers.

Set your API_KEY on line 12.

Set your POLL_INTERVAL, which is the duration between the times this "server" will communicate with Spotify's API Endpoint.
Set your POLL_INTERVAL on line 15.

By default, this "server" will run on 127.0.0.1:portnumber.

If you'd like to change the location, please edit the IP on line 102 or the port on line 18.

For online deployment, please use a service such as Cloudflare Zero Trust Tunnel using your own domain, as this endpoint only runs on a local port on your machine.
