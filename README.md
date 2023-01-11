[![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Default Credentials Cheat Sheet

<p align="center">
  <img src="https://media.moddb.com/cache/images/games/1/65/64034/thumb_620x2000/Lockpicking.jpg"/>
</p>

**One place for all the default credentials to assist pentesters during an engagement, this document has several products default login/password gathered from multiple sources.**

> P.S : Most of the credentials were extracted from changeme,routersploit and Seclists projects, you can use these tools to automate the process https://github.com/ztgrace/changeme , https://github.com/threat9/routersploit (kudos for the awesome work)

- [x] Project in progress

## Motivation
- One document for the most known vendors default credentials
- Assist pentesters during a pentest/red teaming engagement
- **Helping the Blue teamers to secure the company infrastructure assets by discovering this security flaw in order to mitigate it**. See 
[OWASP Guide [WSTG-ATHN-02] - Testing_for_Default_Credentials](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials "OWASP Guide")


#### Short stats of the dataset

|       | Product/Vendor |	Username | Password |
| --- | --- | --- | --- |
| **count**	| 3457	| 3457	| 3457 |
| **unique** |	1179	| 1085 |	1600 |
| **top** |	Oracle| <blank> | <blank> |
| **freq** |	235 |	718 |	461 |

#### Sources

- [Changeme](https://github.com/ztgrace/changeme "Changeme project")
- [Routersploit]( https://github.com/threat9/routersploit "Routersploit project")
- [betterdefaultpasslist]( https://github.com/govolution/betterdefaultpasslist "betterdefaultpasslist")
- [Seclists]( https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials "Seclist project")
- [ics-default-passwords](https://github.com/arnaudsoullie/ics-default-passwords) (thanks to @noraj)
- Vendors documentations/blogs

#### Creds script

You can turn the cheat sheet into a cli command and perform search queries for a specific product.

* Usage Guide
```bash
# Search for product creds
➤ python3 creds search tomcat                                                                                                      
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+

# Update records
➤ python3 creds update
Check for new updates...🔍
New updates are available 🚧
[+] Download database...

# Export Creds to files (could be used for brute force attacks)
➤ python3 creds search tomcat export
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+

[+] Creds saved to /tmp/tomcat-usernames.txt , /tmp/tomcat-passwords.txt 📥
```
  
[![asciicast](https://asciinema.org/a/526599.svg)](https://asciinema.org/a/526599)
  
#### Pass Station

[noraj][noraj] created CLI & library to search for default credentials among this database using `DefaultCreds-Cheat-Sheet.csv`.
The tool is named [Pass Station][pass-station] ([Doc][ps-doc]) and has some powerful search feature (fields, switches, regexp, highlight) and output (simple table, pretty table, JSON, YAML, CSV).

[![asciicast](https://asciinema.org/a/397713.svg)](https://asciinema.org/a/397713)

[noraj]:https://pwn.by/noraj/
[pass-station]:https://github.com/sec-it/pass-station
[ps-doc]:https://sec-it.github.io/pass-station/

## Contribute

If you cannot find the password for a specific product, please submit a pull request to update the dataset.<br>

> ### Disclaimer
> **For educational purposes only, use it at your own responsibility.** 
