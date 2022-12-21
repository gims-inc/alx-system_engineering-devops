# web_stack_debugging_1

##
 ```
 pgrep -lf nginx
 ```
## 
 ```
 netstat -pan | grep "80"
 ```
## Edit /etc/nginx/sites-available/default

 ```    
 vim /etc/nginx/sites-available/default

 ```
## change 8080 to 80

  ```
    listen [::]:80;
    listen 80;
  ```
### Remove the part:

 ```ipv6only=on```

## Verify your config file

 ```
 sudo nginx -t

 ```

## Restart nginx
 
 ```
  service nginx restart
 ```

### Resources

 [0](https://www.cyberciti.biz/faq/find-linux-what-running-on-port-80-command/)
