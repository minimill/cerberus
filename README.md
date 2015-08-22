# Ceberus

Deploy static sites to obfuscated subdomains using just Git and Nginx.

## Setup

1. [Install Nginx][install-nginx].

2. Add the ceberus-specific nginx configurations:
    
    1. Edit `ceberus.nginx.conf` to reflect the domain you wish to root your subdomains on, and the folder in which you want to server the static files from.  The default domain is `<subdomain>.ceberus.minimill.co`, and the default location is `/ceberus/`.
    
    2. Enable these Nginx configurations:

        ```bash
        cd /etc/nginx/
        sudo cp ceberus.nginx.conf sites-available
        sudo ln -s /etc/nginx/sites-available/ceberus.nginx.conf sites-enabled
        cd -
        sudo nginx -t # Should spit out "OK" messages
        sudo service nginx restart
        ```

3. Set up the post-commit hooks:
    
    1. Edit the three configuration variables in `post-receive` to your liking:

        ```bash
        BASE_URL='.ceberus.minimill.co'  # Your domain
        CEBERUS_DIR='sites/'             # Location to serve static files
        CEBERUS='./ceberus'              # Location of the ceberus script
        ```

    2. Put a copy of `post-receive` in `path/to/your_repo.git/hooks/`.  Make sure it's executable.

        ```bash
        cp post-receive path/to/your_repo.git/hooks
        chmod +x path/to/your_repo.git/hooks/post-receive
        ```

## Usage

4. `git push`!  You should be able to push to `path/to/your_repo.git` and Ceberus will deploy to a subdomain.

[install-nginx]: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-14-04-lts

