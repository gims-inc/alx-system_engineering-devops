# web_stack_debugging_1

##
 ```
 pgrep -lf nginx
 ```
 ```
 netstat -pan | grep "80"
 ```
### Delete /etc/nginx/sites-enabled/default
 
### Create a symlink btn sites-enabled/default and sites-available default
  
### Remove the part:

 ```ipv6only=on```

### Verify your config file

 ```
 sudo nginx -t

 ```

### Restart nginx

 ```
  service nginx restart
 ```

### Resources

 [0](https://www.cyberciti.biz/faq/find-linux-what-running-on-port-80-command/)

 [Sites-Available vs Sites-Enabled in Nginx](https://maximorlov.com/tips/sites-available-vs-sites-enabled-in-nginx/)

