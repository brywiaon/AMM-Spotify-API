This server-sided endpoint provides the following details about a user's live Spotify statistics:

{
  "artist":"artistname",
  "image":"imageurl",
  "playing":playingstatus(true/false),
  "title":"titlename",
  "updated":metadata
}

For this to work, please aquire your Spotify CLIENT_ID and CLIENT_SECRET from developer.spotify.com. Do not share your keys with anyone else.

Place your Spotify CLIENT_ID on line ---.

Place your Spotify CLIENT_SECRET on line ---.

By default, this "server" will run on 127.0.0.1:portnumber.

If you'd like to change the location, please edit the IP on line --- or the port on line ---.

For online deployment, please use a service such as Cloudflare Zero Trust Tunnel using your own domain, as this endpoint only runs on a local port on your machine.
