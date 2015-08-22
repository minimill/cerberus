# Cerberus

Deploy static sites to obfuscated subdomains using just Git and Nginx.

## Setup

1. [Install Nginx][install-nginx].

2. Edit `remote/cerberus.nginx.conf` to reflect the domain you wish to run cerberus on, and the folder from which you want to server the static files.  The default domain is `work.minimill.co`, and the default location is `/srv/work/public_html/`.

3. Edit the three configuration variables in `remote/post-receive` to your liking:

    ```bash
    BASE_URL='work.minimill.co'           # Your domain
    CERBERUS_DIR='/srv/work/public_html/' # Location to serve static files
    CERBERUS='~/bin/cerberus-remote'      # Location of the cerberus script
    ```

4. On your server, install the necessary files:

    ```bash
    # Install the nginx configurations
    sudo cp remote/cerberus.nginx.conf /etc/nginx/sites-available/
    sudo ln -s /etc/nginx/sites-available/cerberus.nginx.conf /etc/nginx/sites-enabled
    sudo nginx -t # Should spit out "OK" messages
    sudo service nginx restart

    # Isntall the post-receive hook and cereberus-remote
    cp remote/post-receive remote/cerberus-remote /root/bin
    chmod +x /root/bin/cerberus-remote /root/bin/post-receive
    ```

5. On your local machine, put cerberus somewhere in the `PATH`:

    ```bash
    cp cerberus/cerberus ~/bin
    ```

## Usage

1. Run `cerberus init` in a git repo to setup the remote repo and add a new git remote.
2. `git push deploy`!  Just push to the `deploy` remote and Cerberus will deploy your remote.

[install-nginx]: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-14-04-lts
