# Default Credentials Cheat Sheet
<p align="center">
  <img src="https://media.moddb.com/cache/images/games/1/65/64034/thumb_620x2000/Lockpicking.jpg"/>
</p>

One place for all the default credentials to assist the pentesters during an engagement, this document has a several products default credentials that are gathered from several sources.

> P.S : Most of the credentials are extracted from the changeme,routersploit and Seclists projects, you can use these tools to automate the process https://github.com/ztgrace/changeme , https://github.com/threat9/routersploit (kudos for the awesome work)

- [x] Project in progress

## Motivation
- One document for the most known vendors default credentials
- Assist pentesters during a pentest/red teaming engagement
- **Helping the Red/Blue teamers to secure the company infrastructure by discovering this security flaw in order to mitigate it**. See 
[OWASP Guide [WSTG-ATHN-02] - Testing_for_Default_Credentials](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials "OWASP Guide")


#### Short stats of the dataset

|       | Product/Vendor |	Username | Password |
| --- | --- | --- | --- |
| **count**	| 3343	| 3343	| 3343 |
| **unique** |	1071	| 1059 |	1546 |
| **top** |	Oracle| <blank> | <blank> |
| **freq** |	235 |	703 |	455 |

#### Sources

- [Changeme](https://github.com/ztgrace/changeme "Changeme project")
- [Routersploit]( https://github.com/threat9/routersploit "Routersploit project")
- [betterdefaultpasslist]( https://github.com/govolution/betterdefaultpasslist "betterdefaultpasslist")
- [Seclists]( https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials "Seclist project")
- [ics-default-passwords](https://github.com/arnaudsoullie/ics-default-passwords) (thanks to @noraj)
- Vendors documentations/blogs

#### Creds script

You can turn the cheat sheet into a cli command and perform search queries for a specific product.

```bash
# Usage
➤ python3 creds search tomcat                                                                                                      
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+
```

#### Pass Station

[noraj][noraj] created CLI & library to search for default credentials among this database using `DefaultCreds-Cheat-Sheet.csv`.
The tool is named [Pass Station][pass-station] ([Doc][ps-doc]) and has some powerful search feature (fields, switches, regexp, highlight) and output (simple table, pretty table, JSON, YAML, CSV).

[![asciicast](https://asciinema.org/a/397713.svg)](https://asciinema.org/a/397713)

[noraj]:https://pwn.by/noraj/
[pass-station]:https://github.com/sec-it/pass-station
[ps-doc]:https://sec-it.github.io/pass-station/

#### Contribute
If you cannot find the password for a specific product, please submit a pull request to update the dataset.<br>

> #### Disclaimer
> **For educational purposes only, use it at your own responsibility.** 

| Product/Vendor   | Username | Password |
| ---      | ---      | --- |
| Zyxel (ssh)   | zyfwp | PrOw!aN_fXp |
| APC UPS (web) | apc | apc |
| Weblogic (web) | system | manager |
| Weblogic (web) |  system | manager |
| Weblogic (web) |  weblogic | weblogic1 |
| Weblogic (web) |  WEBLOGIC | WEBLOGIC |
| Weblogic (web) |  PUBLIC | PUBLIC |
| Weblogic (web) |  EXAMPLES | EXAMPLES |
| Weblogic (web) |  weblogic | weblogic |
| Weblogic (web) |  system | password |
| Weblogic (web) |  weblogic | welcome(1) |
| Weblogic (web) |  system | welcome(1) |
| Weblogic (web) |  operator | weblogic |
| Weblogic (web) |  operator | password |
| Weblogic (web) |  system | Passw0rd |
| Weblogic (web) |  monitor | password |
| Kanboard (web) |  admin | admin |
| Dlink (web) | admin | admin | 
| Dlink (web) | 1234 | 1234 | 
| Dlink (web) | root | 12345 | 
| Dlink (web) | root | root | 
| Kali linux (OS) | kali | kali | 
| F5 | admin | admin | 
| F5 | root | default | 
| F5 | support |  | 
| F5-Networks | <N/A> |  | 
| Barracuda (web) | admin | admin | 
| Barracuda (web) | ssladmin | ssladmin | 
| Checkpoint (web) | admin | admin | 
| Checkpoint (web) | admin| abc123  | 
| Citrix Systems (web) | nsroot | nsroot | 
| Citrix Systems (web) | root | rootadmin | 
| Pfsense (web) | admin | pfsense | 
| fortinet (web) | admin |  | 
| fortinet (web) | maintainer | bcpb+serial# | 
| fortinet (web) | maintainer | admin  | 
| comtrend (ssh) | admin | admin  | 
| axis (web) | root | pass  | 
| axis (web) | root | admin  | 
| hikvision (ssh) | admin | 12345  | 
| honeywell (ssh) | admin | 12345  |
| Apache Tomcat (web) |  tomcat | tomcat |
| Apache Tomcat (web) |  admin | admin |
| Apache Tomcat (web) |  ovwebusr | OvW*busr1 |
| Apache Tomcat (web) |  j2deployer | j2deployer |
| Apache Tomcat (web) |  cxsdk | kdsxc |
| Apache Tomcat (web) |  ADMIN | ADMIN |
| Apache Tomcat (web) |  xampp | xampp |
| Apache Tomcat (web) |  tomcat | s3cret |
| Apache Tomcat (web) |  QCC | QLogic66 |
| Apache Tomcat (web) |  admin | None |
| Apache Tomcat (web) |  admin | tomcat |
| Apache Tomcat (web) |  root | root |
| Apache Tomcat (web) |  role1 | role1 |
| Apache Tomcat (web) |  role | changethis |
| Apache Tomcat (web) |  tomcat | changethis |
| Apache Tomcat (web) |  admin | j5Brn9 |
| Apache Tomcat (web) |  role1 | tomcat |
| zte (ssh) | admin | admin | 
| zte (ssh) | ZXDSL | ZXDSL | 
| zte (ssh) | user | user | 
| zte (ssh) | on | on | 
| zte (ssh) | root | Zte521 | 
| zte (ssh) | root | W!n0&oO7. | 
| netgar (ssh) | admin | admin | 
| netgar (ssh) | admin | 1234 | 
| netgar (ssh) | admin |  | 
| 2wire (ssh) | admin | admin | 
| asmax (ssh) | admin | admin | 
| asmax (ssh) | support | support | 
| asmax (ssh) | user | user | 
| bhu (ssh) | admin | admin | 
| ipfire (ssh) | admin | admin | 
| ipfire (ssh) | root | admin | 
| ipfire (ssh) | admin |  | 
| linksys (ssh) | admin | admin | 
| linksys (ssh) | admin | password | 
| linksys (ssh) | root | admin  | 
| linksys (ssh) | linksys |  | 
| netcore (ssh) | admin | admin  | 
| netcore (ssh) | guest | guest | 
|2Wire, Inc.|http| | 
|360 Systems|factory|factory | 
|3COM|3comcso|RIP000 | 
|3COM||12345 | 
|3COM||1234admin | 
|3COM|| | 
|3COM||ANYCOM | 
|3COM||ILMI | 
|3COM||PASSWORD | 
|3COM||admin | 
|3COM||comcomcom | 
|3COM|<N/A>| | 
|3COM|<N/A>|PASSWORD | 
|3COM|<N/A>|admin | 
|3COM|Admin|Admin | 
|3COM|Administrator| | 
|3COM|Administrator|admin | 
|3COM|Type User: FORCE| | 
|3COM|User|Password | 
|3COM|adm| | 
|3COM|admin|1234admin | 
|3COM|admin| | 
|3COM|admin|admin | 
|3COM|admin|comcomcom | 
|3COM|admin|password | 
|3COM|admin|synnet | 
|3COM|adminttd|adminttd | 
|3COM|debug|synnet | 
|3COM|defug|synnet | 
|3COM|manager|manager | 
|3COM|monitor|monitor | 
|3COM|none|admin | 
|3COM|read|synnet | 
|3COM|recover|recover | 
|3COM|recovery|recovery | 
|3COM|root|!root | 
|3COM|security|security | 
|3COM|tech| | 
|3COM|tech|tech | 
|3COM|write|synnet | 
|3M|VOL-0215| | 
|3M|volition| | 
|3M|volition|volition | 
|3ware|Administrator|3ware | 
|ACCTON||0000 | 
|ACCTON|__super|(caclulated) | 
|ACCTON|admin| | 
|ACCTON|manager|manager | 
|ACCTON|monitor|monitor | 
|ACCTON|none|0 | 
|ADC Kentrox||secret | 
|ADC Kentrox|<N/A>|secret | 
|ADIC|admin|password | 
|ADIC|admin|secure | 
|ADP|sysadmin|master | 
|ADT||2580 | 
|ADTRAN|admin|password | 
|AIRAYA Corp|Airaya|Airaya | 
|ALLNET|admin|admin | 
|ALLNET|admin|password | 
|ALLNET|none|admin | 
|AMI||A.M.I | 
|AMI||AM | 
|AMI||AMI | 
|AMI||AMI!SW | 
|AMI||AMI.KEY | 
|AMI||AMI.KEZ | 
|AMI||AMI?SW | 
|AMI||AMIPSWD | 
|AMI||AMISETUP | 
|AMI||AMI_SW | 
|AMI||AMI~ | 
|AMI||BIOSPASS | 
|AMI||CMOSPWD | 
|AMI||HEWITT RAND | 
|AMI||aammii | 
|AMI|<N/A>|A.M.I | 
|AMI|<N/A>|AM | 
|AMI|<N/A>|AMI | 
|AMI|<N/A>|AMI!SW | 
|AMI|<N/A>|AMI.KEY | 
|AMI|<N/A>|AMI.KEZ | 
|AMI|<N/A>|AMI?SW | 
|AMI|<N/A>|AMIAMI | 
|AMI|<N/A>|AMIDECOD | 
|AMI|<N/A>|AMIPSWD | 
|AMI|<N/A>|AMISETUP | 
|AMI|<N/A>|AMI_SW | 
|AMI|<N/A>|AMI~ | 
|AMI|<N/A>|BIOSPASS | 
|AMI|<N/A>|HEWITT RAND | 
|AMI|<N/A>|aammii | 
|AMX||1988 | 
|AMX|| | 
|AMX||admin | 
|AMX|Admin|1988 | 
|AMX|Administrator|vision2 | 
|AMX|NetLinx|password | 
|AMX|admin|1988 | 
|AMX|admin|admin | 
|AMX|administrator|password | 
|AMX|guest|guest | 
|AMX|root|mozart | 
|AOC|<N/A>|admin | 
|APACHE|admin|jboss4 | 
|APC|(any)|TENmanUFactOryPOWER | 
|APC||serial number of the Call-UPS | 
|APC||serial number of the Share-UPS | 
|APC|<N/A>|TENmanUFactOryPOWER | 
|APC|<N/A>|backdoor | 
|APC|POWERCHUTE|APC | 
|APC|apc|apc | 
|APC|device|apc | 
|APC|device|device | 
|APC|readonly|apc | 
|ARtem||admin | 
|ASMAX|admin|epicrouter | 
|AST||SnuFG5 | 
|AST|<N/A>|SnuFG5 | 
|AT&T|<N/A>|mcp | 
|ATL|Service|5678 | 
|ATL|operator|1234 | 
|AVM|<N/A>|0 | 
|AVM|<N/A>|<N/A> | 
|AWARD||1322222 | 
|AWARD||256256 | 
|AWARD||589589 | 
|AWARD||589721 | 
|AWARD|| | 
|AWARD||?award | 
|AWARD||AWARD SW | 
|AWARD||AWARD?SW | 
|AWARD||AWARD_PW | 
|AWARD||AWARD_SW | 
|AWARD||Award | 
|AWARD||BIOS | 
|AWARD||CONCAT | 
|AWARD||HELGA-S | 
|AWARD||HEWITT RAND | 
|AWARD||HLT | 
|AWARD||PASSWORD | 
|AWARD||SER | 
|AWARD||SKY_FOX | 
|AWARD||SWITCHES_SW | 
|AWARD||SW_AWARD | 
|AWARD||SZYX | 
|AWARD||Sxyz | 
|AWARD||TTPTHA | 
|AWARD||TzqF | 
|AWARD||ZAAADA | 
|AWARD||aLLy | 
|AWARD||aPAf | 
|AWARD||admin | 
|AWARD||alfarome | 
|AWARD||award.sw | 
|AWARD||award_? | 
|AWARD||award_ps | 
|AWARD||awkward | 
|AWARD||biosstar | 
|AWARD||biostar | 
|AWARD||condo | 
|AWARD||djonet | 
|AWARD||efmukl | 
|AWARD||g6PJ | 
|AWARD||h6BB | 
|AWARD||j09F | 
|AWARD||j256 | 
|AWARD||j262 | 
|AWARD||j322 | 
|AWARD||j64 | 
|AWARD||lkw peter | 
|AWARD||lkwpeter | 
|AWARD||setup | 
|AWARD||t0ch20x | 
|AWARD||t0ch88 | 
|AWARD||wodj | 
|AWARD||zbaaaca | 
|AWARD||zjaaadc | 
|AXUS|<N/A>|0 | 
|Accelerated Networks|sysadm|anicust | 
|Aceex|admin| | 
|Acer|| | 
|Actiontec|| | 
|Actiontec|admin|password | 
|AdComplete.com|Admin1|Admin1 | 
|Adaptec|Administrator|adaptec | 
|AddPac Technology|root|router | 
|Addon|admin|admin | 
|Adobe|admin|admin | 
|Adobe|anonymous|anonymous | 
|Adobe|aparker@geometrixx.info|aparker | 
|Adobe|author|author | 
|Adobe|jdoe@geometrixx.info|jdoe | 
|Adobe|replication-receiver|replication-receiver | 
|Adobe|vgnadmin|vgnadmin | 
|Adtech|root|ax400 | 
|Adtran||adtran | 
|Adtran|admin|password | 
|Advanced Integration||Advance | 
|Advanced Integration|<N/A>|Advance | 
|Advantek Networks|admin| | 
|Aethra|admin|password | 
|AirLink Plus||admin | 
|AirTies RT-210|admin|admin | 
|Airlink||admin | 
|Aironet|| | 
|Airway||0000 | 
|Aladdin|root|kn1TG7psLu | 
|Alcatel|| | 
|Alcatel||admin | 
|Alcatel|<N/A>|1064 | 
|Alcatel|SUPERUSER|ANS#150 | 
|Alcatel Thomson|admin|admin | 
|Alcatel|adfexc|adfexc | 
|Alcatel|admin|switch | 
|Alcatel|at4400|at4400 | 
|Alcatel|client|client | 
|Alcatel|dhs3mt|dhs3mt | 
|Alcatel|dhs3pms|dhs3pms | 
|Alcatel|diag|switch | 
|Alcatel|ftp_admi|kilo1987 | 
|Alcatel|ftp_inst|pbxk1064 | 
|Alcatel|ftp_nmc|tuxalize | 
|Alcatel|ftp_oper|help1954 | 
|Alcatel|halt|tlah | 
|Alcatel|install|llatsni | 
|Alcatel|kermit|kermit | 
|Alcatel|mtch|mtch | 
|Alcatel|mtcl| | 
|Alcatel|mtcl|mtcl | 
|Alcatel|root|letacla | 
|Alcatel|root|permit | 
|Alcatel|superuser|superuser | 
|Alien Technology|alien|alien | 
|Alien Technology|root|alien | 
|Allied Telesyn||manager | 
|Allied Telesyn|<N/A>|admin | 
|Allied Telesyn|admin| | 
|Allied Telesyn|manager|admin | 
|Allied Telesyn|manager|friend | 
|Allied Telesyn|manager|manager | 
|Allied Telesyn|root| | 
|Allied Telesyn|secoff|secoff | 
|Allnet|admin|admin | 
|Allot|admin|allot | 
|Allot|root|bagabu | 
|Alteon|admin| | 
|Alteon|admin|admin | 
|Alteon|admin|linga | 
|Ambit|root| | 
|Ambit|root|root | 
|Ambit|user|user | 
|Amigo|admin|epicrouter | 
|Amino||leaves | 
|Amino||snake | 
|Amitech|admin|admin | 
|AmpJuke|admin|pass | 
|Amptron||Polrty | 
|Amptron|<N/A>|Polrty | 
|Andover Controls|acc|acc | 
|Apache Project|jj| | 
|Apache|admin| | 
|Apache|admin|admin | 
|Apache|admin|j5Brn9 | 
|Apache|admin|tomcat | 
|Apache|both|tomcat | 
|Apache|role|changethis | 
|Apache|role1|role1 | 
|Apache|role1|tomcat | 
|Apache|root|changethis | 
|Apache|root|root | 
|Apache|tomcat|changethis | 
|Apache|tomcat|tomcat | 
|Apple||public | 
|Apple||xyzzy | 
|Apple|<N/A>|admin | 
|Apple|<N/A>|password | 
|Apple Computer||public | 
|Apple Computer||xyzzy | 
|Apple|admin|public | 
|Apple|mobile|dottie | 
|Apple|root|admin | 
|Apple|root|alpine | 
|Applied Innovations|scout|scout | 
|Areca|admin|0 | 
|Arescom|<N/A>|atc123 | 
|Arlotto|admin|123456 | 
|Arris|admin|password | 
|Arrowpoint|| | 
|Arrowpoint|admin|system | 
|Aruba|admin|admin | 
|Arun|123|234 | 
|Asante|IntraStack|Asante | 
|Asante|IntraSwitch|Asante | 
|Asante|admin|asante | 
|Asante|superuser| | 
|Asante|superuser|asante | 
|Ascend||ascend | 
|Ascend|<N/A>|ascend | 
|Ascend|readonly|lucenttech2 | 
|Ascend|readwrite|lucenttech1 | 
|Ascend|root|ascend | 
|Ascom||3ascotel | 
|Aspect|DTA|TJM | 
|Aspect|customer|none | 
|Asus|<N/A>|admin | 
|Asus|admin|admin | 
|Asus|adsl|adsl1234 | 
|Atlantis|admin|atlantis | 
|Atlassian|Crowd|password | 
|Atlassian|Demo|password | 
|Atlassian|Username|password | 
|Atlassian|crowd­-openid-­server|password | 
|Attachmate||PASSWORD | 
|Audioactive||telos | 
|Autodesk|autocad|autocad | 
|Avaya||Craftr4 | 
|Avaya|<N/A>| | 
|Avaya|<N/A>|admin | 
|Avaya|Administrator|ggdaseuaimhrke | 
|Avaya|Craft|crftpw | 
|Avaya|admin|admin | 
|Avaya|admin|admin123 | 
|Avaya|admin|barney | 
|Avaya|admin|password | 
|Avaya|craft| | 
|Avaya|craft|crftpw | 
|Avaya|dadmin|dadmin | 
|Avaya|dadmin|dadmin01 | 
|Avaya|diag|danger | 
|Avaya|manuf|xxyyzz | 
|Avaya|root|ROOT500 | 
|Avaya|root|cms500 | 
|Avaya|root|ggdaseuaimhrke | 
|Avaya|root|root | 
|Avenger News System (ANS)||Administrative | 
|Avocent|root|tslinux | 
|Award||lkwpeter | 
|Award|<N/A>|1322222 | 
|Award|<N/A>|256256 | 
|Award|<N/A>|?award | 
|Award|<N/A>|AWARD_SW | 
|Award|<N/A>|BIOS | 
|Award|<N/A>|CONCAT | 
|Award|<N/A>|CONDO | 
|Award|<N/A>|HELGA-S | 
|Award|<N/A>|HEWITT RAND | 
|Award|<N/A>|HLT | 
|Award|<N/A>|PASSWORD | 
|Award|<N/A>|SER | 
|Award|<N/A>|SKY_FOX | 
|Award|<N/A>|SWITCHES_SW | 
|Award|<N/A>|SY_MB | 
|Award|<N/A>|SZYX | 
|Award|<N/A>|Sxyz | 
|Award|<N/A>|TTPTHA | 
|Award|<N/A>|TzqF | 
|Award|<N/A>|aLLy | 
|Award|<N/A>|aPAf | 
|Award|<N/A>|admin | 
|Award|<N/A>|alfarome | 
|Award|<N/A>|award | 
|Award|<N/A>|awkward | 
|Award|<N/A>|biosstar | 
|Award|<N/A>|biostar | 
|Award|<N/A>|g6PJ | 
|Award|<N/A>|h6BB | 
|Award|<N/A>|j09F | 
|Award|<N/A>|j256 | 
|Award|<N/A>|j262 | 
|Award|<N/A>|j322 | 
|Award|<N/A>|j64 | 
|Award|<N/A>|lkw peter | 
|Award|<N/A>|lkwpeter | 
|Award|<N/A>|setup | 
|Award|<N/A>|t0ch20x | 
|Award|<N/A>|t0ch88 | 
|Award|<N/A>|wodj | 
|Award|<N/A>|zbaaaca | 
|Axis|<N/A>| | 
|Axis Communications|root|pass | 
|Axis|root|pass | 
|Axway|setup|setup | 
|Aztech|admin|admin | 
|Aztech|isp|isp | 
|Aztech|root|admin | 
|BBR-4MG and|root|<N/A> | 
|BEA|system|weblogic | 
|BECU|musi1921|Musii%1921 | 
|BLACKBOX|Administrator|public | 
|BMC Software|Administrator|the same all over | 
|BMC Software|Best1_User|BackupU$r | 
|BMC|patrol|patrol | 
|BNI|USER|USER | 
|BT|admin|admin | 
|Barco, Inc.||clickshare | 
|Barco, Inc.|admin|admin | 
|Barracuda|admin|admin | 
|Barracuda|ssladmin|ssladmin | 
|Bausch Datacom|admin|epicrouter | 
|Bay Networks||NetICs | 
|Bay Networks|<N/A>|NetICs | 
|Bay Networks|Manager| | 
|Bay Networks|User| | 
|Bay Networks|security|security | 
|Beetel|admin|admin | 
|Beetel|admin|password | 
|Belkin||MiniAP | 
|Belkin|<N/A>|admin | 
|Belkin|admin|none | 
|Benq|admin|admin | 
|Best Practical Solutions|root|password | 
|BestPractical|root|password | 
|Bewan|bewan|bewan | 
|Billion|| | 
|Billion|admin|admin | 
|BinTec|<N/A>|snmp-Trap | 
|BinTec|Admin|No | 
|BinTec|admin|bintec | 
|Bintec|admin|bintec | 
|Bintec|admin|funkwerk | 
|Biodata||Babylon | 
|Biodata|config|biodata | 
|Biostar||Biostar | 
|Biostar||Q54arwms | 
|Biostar|<N/A>|Biostar | 
|Biostar|<N/A>|Q54arwms | 
|Biscom|admin|admin | 
|BizDesign|Admin|ImageFolio | 
|Black Widow Web Design Ltd|admin|nimda | 
|Blaeri|Blaeri|22332323 | 
|Blitzz Technologies|admin|admin | 
|Blue Coat Systems|admin|articon | 
|Bluecoat|admin|admin | 
|Bomgar|admin|password | 
|Borland|| | 
|Borland|politically|correct | 
|Bosch|live|live | 
|Bosch|service|service | 
|Bosch|user|user | 
|Breezecom|| | 
|Breezecom||Helpdesk | 
|Breezecom||Master | 
|Breezecom||Super | 
|Breezecom||laflaf | 
|Breezecom|<N/A>|Helpdesk | 
|Breezecom|<N/A>|Master | 
|Breezecom|<N/A>|Super | 
|Breezecom|<N/A>|laflaf | 
|Broadlogic|admin|admin | 
|Broadlogic|installer|installer | 
|Broadlogic|webadmin|webadmin | 
|Brocade|admin|brocade1 | 
|Brocade|admin|password | 
|Brocade|factory|Fact4EMC | 
|Brocade|root|Serv4EMC | 
|Brocade|root|fibranne | 
|Brocade|root|fivranne | 
|Brocade|user|password | 
|Brother||access | 
|Brother|<N/A>|access | 
|Brother Industries Ltd.||00000000 | 
|Brother Industries Ltd.||12345678 | 
|Brother Industries Ltd.|admin|access | 
|Brother|admin|access | 
|Buffalo Technology|admin|password | 
|Buffalo|root| | 
|Buffalo/MELCO|root| | 
|Busybox|admin|admin | 
|CA Process Automation|pamadmin|pamadmin | 
|CGI World||protection | 
|CNET|admin|1234 | 
|CNet|Admin|admin | 
|COM3|admin|admin | 
|CTX International||CTX_123 | 
|CTX International|<N/A>|CTX_123 | 
|Cable And Wireless|admin|1234 | 
|Cabletron|| | 
|Cabletron|netman| | 
|Canon/Brother|7654321|7654321 | 
|Canon|<N/A>|0 | 
|Capricorn Infotech India||1234567890 | 
|CareStream Health|KeyOperator|DV5800 | 
|CareStream Health|LocalService|DV5800 | 
|Carsten Schmitz|admin|password | 
|Cayman|<N/A>| | 
|Cayman|admin|(serial number) | 
|Cayman|admin| | 
|Cayman|}| | 
|Celerity|mediator|mediator | 
|Celerity|root|Mua'dib | 
|Cellit|cellit|cellit | 
|Ceragon Networks|root|tooridu | 
|Chase Research||iolan | 
|Check Point|admin|admin | 
|Check Point|admin|adminadmin | 
|Checkpoint|admin|abc123 | 
|Checkpoint|admin|admin | 
|Chuming Chen|administrator|adminpass | 
|CipherTrust|admin|password | 
|Ciphertrust|admin|password | 
|Cisco| EAdmin| | 
|Cisco| UAMIS_| | 
|Cisco| UNITY_| | 
|Cisco| UOMNI_| | 
|Cisco| UVPIM_| | 
|Cisco|| | 
|Cisco||Cisco | 
|Cisco||Cisco router | 
|Cisco||_Cisco | 
|Cisco||c | 
|Cisco||cc | 
|Cisco||changeit | 
|Cisco||cisco | 
|Cisco||letmein | 
|Cisco||public/private/secret | 
|Cisco||riverhead | 
|Cisco|<N/A>|Cisco router | 
|Cisco|<N/A>|ILMI | 
|Cisco|<N/A>|c | 
|Cisco|<N/A>|cable-docsis | 
|Cisco|<N/A>|cc | 
|Cisco|<N/A>|cisco | 
|Cisco|Administrator|admin | 
|Cisco|Administrator|changeme | 
|Cisco|CISCO15|otbu+1 | 
|Cisco|Cisco|Cisco | 
|Cisco|ESubscriber| | 
|Cisco|End User|7936 | 
|Cisco|admin| | 
|Cisco|admin|admin | 
|Cisco|admin|changeme | 
|Cisco|admin|cisco | 
|Cisco|admin|default | 
|Cisco|admin|diamond | 
|Cisco|admin|tsunami | 
|Cisco|bbsd-client| | 
|Cisco|bbsd-client|changeme2 | 
|Cisco|bubba|(unknown) | 
|Cisco|cisco| | 
|Cisco|cisco|cisco | 
|Cisco|cmaker|cmaker | 
|Cisco|enable| | 
|Cisco|enable|cisco | 
|Cisco|guest| | 
|Cisco|hsa|hsadb | 
|Cisco|hsa|hsadb  | 
|Cisco|netrangr|attack | 
|Cisco|pnadmin|pnadmin | 
|Cisco|praisenetwork|perfectpraise | 
|Cisco|private ReadWrite access|secret | 
|Cisco|public ReadOnly access|secret | 
|Cisco|ripeop| | 
|Cisco|root |attack | 
|Cisco|root|Cisco | 
|Cisco|root|attack | 
|Cisco|root|blender | 
|Cisco|root|password | 
|Cisco|root|secur4u | 
|Cisco|sa| | 
|Cisco|technician|2 + last 4 of Audio | 
|Cisco|uwmadmin|password | 
|Cisco|wlse|wlsedb | 
|Cisco|wlseuser|wlsepassword | 
|Cisco-Arrowpoint|admin|system | 
|Citel||citel | 
|Citel|citel|password | 
|Citrix Systems, Inc.|nsroot|nsroot | 
|Citrix Systems, Inc.|root|rootadmin | 
|Claris||familymacintosh | 
|ClearOne Communications|ClearOne|RAV | 
|ClearOne Communications|clearone|converge | 
|Cnet|Admin|epicrouter | 
|Cnet|admin|password | 
|Cobalt|admin|admin | 
|Colubris Networks|admin|admin | 
|Colubris|admin|admin | 
|Comcast Home Networking|comcast| | 
|Comcast SMC|cusadmin|highspeed | 
|Comcast SMC|cusadmin|CantTouchThis | 
|Comersus|admin|dmr99 | 
|Comodo Group, Inc|mydlp|mydlp | 
|Compaq|| | 
|Compaq||Compaq | 
|Compaq|<N/A>|Compaq | 
|Compaq|PFCUser|240653C9467E45 | 
|Compaq|administrator|administrator | 
|Compaq|anonymous| | 
|Compaq|operator|operator | 
|Compaq|root|manager | 
|Compaq|root|rootme | 
|Compaq|user|public | 
|Compaq|user|user | 
|Compualynx|administrator|asecret | 
|Comtrend|admin|1234 | 
|Comtrend|admin| | 
|Comtrend|admin|admin | 
|Conceptronic|admin|1234 | 
|Conceptronic|admin|password | 
|Conceptronic|anonymous|password | 
|Concord||last | 
|Concord|<N/A>|last | 
|Conexant|<N/A>|admin | 
|Conexant|<N/A>|epicrouter | 
|Conexant|Administrator|admin | 
|Conexant|admin|amigosw1 | 
|Conexant|admin|conexant | 
|Conexant|admin|epicrouter | 
|Conexant|admin|password | 
|Conitec|Adam|29111991 | 
|Control4||ducati900ss | 
|Control4|root|t0talc0ntr0l4! | 
|Corecess|Administrator|admin | 
|Corecess|admin| | 
|Corecess|corecess|corecess | 
|CoronaMatrix|admin|admin | 
|Covertix|Admin|Admin | 
|Creative|<N/A>| | 
|Crossbeam||x40rocks | 
|Crystalview||Crystal | 
|CyberMax||Congress | 
|CyberMax|<N/A>|Congress | 
|Cyberguard|cgadmin|cgadmin | 
|Cyclades|root| | 
|Cyclades|root|tslinux | 
|Cyclades|super|surt | 
|D-Link||admin | 
|D-Link||private | 
|D-Link||public | 
|D-Link|<N/A>|admin | 
|D-Link|Admin| | 
|D-Link|Alphanetworks|wrgg15_di524 | 
|D-Link|D-Link|D-Link | 
|D-Link|admin| | 
|D-Link|admin|admin | 
|D-Link|admin|gvt12345 | 
|D-Link|admin|none | 
|D-Link|admin|password | 
|D-Link|admin|public | 
|D-Link|admin|year2000 | 
|D-Link|dont need one|admin | 
|D-Link|none|none | 
|D-Link|none|private | 
|D-Link|root|admin | 
|D-Link|user| | 
|D-Link|user|none | 
|D9287ar|Clarissa| | 
|DIGICOM|root|admin | 
|DVB|dvstation|dvst10n | 
|DVB|root|pixmet2003 | 
|Daewoo||Daewuu | 
|Daewoo|<N/A>|Daewuu | 
|Dallas Semiconductors|root|tini | 
|Dassault Systemes|Test Everything| | 
|Data General|op|op | 
|Data General|op|operator | 
|Data General|operator|operator | 
|DataWizard Technologies Inc.|anonymous| | 
|DataWizard Technologies Inc.|test|test | 
|Datacom||letmein | 
|Datacom|<N/A>|letmein | 
|Datacom|sysadm|sysadm | 
|Datawizard.net|anonymous|any | 
|Datawizard.net|anonymous|any@ | 
|Davolink|user|user | 
|Davox|admin|admin | 
|Davox|davox|davox | 
|Davox|root|davox | 
|Davox|sa| | 
|Daytek||Daytec | 
|Daytek|<N/A>|Daytec | 
|Debian||tatercounter2000 | 
|Deerfield|MDaemon|MServer | 
|Dell||Dell | 
|Dell||Fireport | 
|Dell||nz0u4bbe | 
|Dell|<N/A>|1RRWTTOOI | 
|Dell|<N/A>|Dell | 
|Dell|<N/A>|admin | 
|Dell|Admin| | 
|Dell|Administrator|storageserver | 
|Dell|VNC|winterm | 
|Dell|admin|admin | 
|Dell|admin|password | 
|Dell|rapport|r@p8p0r+ | 
|Dell|root|calvin | 
|Dell|root|wyse | 
|Demarc|admin|my_DEMARC | 
|Deutsche Telekom||0 | 
|Deutsche Telekom|admin| | 
|Develcon||BRIDGE | 
|Develcon||password | 
|Develcon|<N/A>|BRIDGE | 
|Develcon|<N/A>|password | 
|Dictaphone|NETOP| | 
|Dictaphone|NETWORK|NETWORK | 
|Dictaphone|PBX|PBX | 
|Digicom|admin|michelangelo | 
|Digicom|user|password | 
|Digicorp||BRIDGE | 
|Digicorp||password | 
|Digicorp|<N/A>|BRIDGE | 
|Digicorp|<N/A>|password | 
|Digicraft Software|Yak|asd123 | 
|Digital Equipment|1|manager | 
|Digital Equipment|1|operator | 
|Digital Equipment|1|syslib | 
|Digital Equipment|1.1|SYSTEM | 
|Digital Equipment|2|maintain | 
|Digital Equipment|2|manager | 
|Digital Equipment|2|operator | 
|Digital Equipment|2|syslib | 
|Digital Equipment|30|games | 
|Digital Equipment|5|games | 
|Digital Equipment|7|maintain | 
|Digital Equipment||1 | 
|Digital Equipment||ACCESS | 
|Digital Equipment||SYSTEM | 
|Digital Equipment||access | 
|Digital Equipment||komprie | 
|Digital Equipment||system | 
|Digital Equipment|<N/A>|ACCESS | 
|Digital Equipment|<N/A>|SYSTEM | 
|Digital Equipment|<N/A>|komprie | 
|Digital Equipment|ALLIN1|ALLIN1 | 
|Digital Equipment|ALLIN1MAIL|ALLIN1MAIL | 
|Digital Equipment|ALLINONE|ALLINONE | 
|Digital Equipment|BACKUP|BACKUP | 
|Digital Equipment|BATCH|BATCH | 
|Digital Equipment|DCL|DCL | 
|Digital Equipment|DECMAIL|DECMAIL | 
|Digital Equipment|DECNET|DECNET | 
|Digital Equipment|DECNET|NONPRIV | 
|Digital Equipment|DEFAULT|DEFAULT | 
|Digital Equipment|DEFAULT|USER | 
|Digital Equipment|DEMO|DEMO | 
|Digital Equipment|FIELD|DIGITAL | 
|Digital Equipment|FIELD|FIELD | 
|Digital Equipment|FIELD|SERVICE | 
|Digital Equipment|FIELD|TEST | 
|Digital Equipment|GUEST|GUEST | 
|Digital Equipment|HELP|HELP | 
|Digital Equipment|HELPDESK|HELPDESK | 
|Digital Equipment|HOST|HOST | 
|Digital Equipment|INFO|INFO | 
|Digital Equipment|INGRES|INGRES | 
|Digital Equipment|LINK|LINK | 
|Digital Equipment|MAILER|MAILER | 
|Digital Equipment|MBMANAGER|MBMANAGER | 
|Digital Equipment|MBWATCH|MBWATCH | 
|Digital Equipment|NETCON|NETCON | 
|Digital Equipment|NETMGR|NETMGR | 
|Digital Equipment|NETNONPRIV|NETNONPRIV | 
|Digital Equipment|NETPRIV|NETPRIV | 
|Digital Equipment|NETSERVER|NETSERVER | 
|Digital Equipment|NETWORK|NETWORK | 
|Digital Equipment|NEWINGRES|NEWINGRES | 
|Digital Equipment|NEWS|NEWS | 
|Digital Equipment|OPERVAX|OPERVAX | 
|Digital Equipment|PDP11|PDP11 | 
|Digital Equipment|PDP8|PDP8 | 
|Digital Equipment|POSTMASTER|POSTMASTER | 
|Digital Equipment|PRIV|PRIV | 
|Digital Equipment|REPORT|REPORT | 
|Digital Equipment|RJE|RJE | 
|Digital Equipment|STUDENT|STUDENT | 
|Digital Equipment|SYS|SYS | 
|Digital Equipment|SYSMAINT|DIGITAL | 
|Digital Equipment|SYSMAINT|SERVICE | 
|Digital Equipment|SYSMAINT|SYSMAINT | 
|Digital Equipment|SYSTEM|MANAGER | 
|Digital Equipment|SYSTEM|OPERATOR | 
|Digital Equipment|SYSTEM|SYSLIB | 
|Digital Equipment|SYSTEM|SYSTEM | 
|Digital Equipment|SYSTEST|UETP | 
|Digital Equipment|SYSTEST_CLIG|SYSTEST | 
|Digital Equipment|SYSTEST_CLIG|SYSTEST_CLIG | 
|Digital Equipment|TELEDEMO|TELEDEMO | 
|Digital Equipment|TEST|TEST | 
|Digital Equipment|UETP|UETP | 
|Digital Equipment|USER|PASSWORD | 
|Digital Equipment|USER|USER | 
|Digital Equipment|USERP|USERP | 
|Digital Equipment|VAX|VAX | 
|Digital Equipment|VMS|VMS | 
|Digital Equipment|accounting|accounting | 
|Digital Equipment|boss|boss | 
|Digital Equipment|demo|demo | 
|Digital Equipment|manager|manager | 
|Digital Equipment|software|software | 
|Digium, Inc.|admin|password | 
|Divar|admin| | 
|Divar|viewer| | 
|Dlink|admin| | 
|Dlink|admin|admin | 
|Dlink|admin|public | 
|DotNetNuke Corporation|admin|dnnadmin | 
|DotNetNuke Corporation|host|dnnhost | 
|Draytek Corp|admin| | 
|Draytek|Draytek|1234 | 
|Draytek|admin| | 
|Draytek|admin|admin | 
|Draytek|draytek|1234 | 
|DuPont|root|par0t | 
|Ducati Motor Holding||Last 4 digits of VIN | 
|Dynalink|admin|admin | 
|Dynalink|admin|private | 
|Dynalink|userNotUsed|userNotU | 
|Dynix Library Systems|LIBRARY| | 
|Dynix Library Systems|SETUP| | 
|Dynix Library Systems|circ| | 
|E-Con|admin|epicrouter | 
|E-Tech||admin | 
|E-Tech|admin|epicrouter | 
|E-Tech|admin|password | 
|E-Tech|none|admin | 
|EMC|MCUser|MCUser1 | 
|EMC|admin| | 
|EMC|admin|changeme | 
|EMC|backuponly|backuponly1 | 
|EMC|backuprestore|backuprestore1 | 
|EMC|dpn|changeme | 
|EMC|restoreonly|restoreonly1 | 
|EMC|root|8RttoTriz | 
|EMC|root|changeme | 
|EMC|viewuser|viewuser1 | 
|EPISD|computer|repair | 
|EPiServer AB|admin|store | 
|EZPhotoSales|admin|admin | 
|Eaton|admin|admin | 
|Echelon Corporation|ilon|ilon | 
|Edimax|admin|123 | 
|Edimax|admin|1234 | 
|Edimax|admin| | 
|Edimax|admin|epicrouter | 
|Edimax|admin|password | 
|Edimax|admin|su@psir | 
|Edimax|edimax|software01 | 
|Edimax|guest|1234 | 
|Edimax|guest| | 
|Efficient|| | 
|Efficient||admin | 
|Efficient|<N/A>|admin | 
|Efficient Networks||hs7mwxkk | 
|Efficient Networks|<N/A>|4getme2 | 
|Efficient Networks|login|admin | 
|Efficient|login|admin | 
|Efficient|login|password | 
|Efficient|superuser|admin | 
|Efficinet Networks|login|admin | 
|Ektron, Inc.|builtin|builtin | 
|Ektron, Inc.|sa|Ektron | 
|Elron|(hostname/ipaddress)|sysadmin | 
|Elsa|| | 
|Elsa||cisco | 
|Elsa|<N/A>| | 
|Elsa|<N/A>|cisco | 
|Emerson|Admin|Emerson1 | 
|Eminent|admin|admin | 
|EnGenius|admin|admin | 
|Enhydra |admin|enhydra | 
|Enox||xo11nE | 
|Enox|<N/A>|xo11nE | 
|Enterasys||netadmin | 
|Enterasys|admin| | 
|Enterasys|admin|netadmin | 
|Enterasys|tiger|tiger123 | 
|Entrust|admin|admin | 
|Entrust|websecadm|changeme | 
|Epox||central | 
|Epox|<N/A>|central | 
|Ericsson ACC|public| | 
|Ericsson|MD110|help | 
|Ericsson|admin|default | 
|Ericsson|expert|expert | 
|Ericsson|netman|netman | 
|EverFocus|admin|admin | 
|EverFocus|operator|operator | 
|EverFocus|supervisor|supervisor | 
|Exabyte|anonymous|Exabyte | 
|Exacq Technologies|admin|admin256 | 
|Exacq Technologies|user|user5710 | 
|Exinda Networks|admin|exinda | 
|Extended Systems|admin|admin | 
|Extended Systems|admin|extendnet | 
|Extreme Networks|admin| | 
|F5|admin|admin | 
|F5|root|default | 
|F5|support| | 
|F5-Networks|<N/A>| | 
|Fastream Technologies|root| | 
|Fastwire|fastwire|fw | 
|FatWire|firstsite|firstsite | 
|FatWire|fwadmin|xceladmin | 
|Firebird Project|SYSDBA|masterkey | 
|Firebird|SYSDBA|masterkey | 
|Flowpoint|| | 
|Flowpoint||password | 
|Flowpoint|<N/A>| | 
|Flowpoint|<N/A>|password | 
|Flowpoint|admin|admin | 
|Fortigate|admin| | 
|Fortinet||bcpb(serial number of the firewall) | 
|Fortinet|admin| | 
|Fortinet|maintainer|admin | 
|Fortinet|maintainer|bcpb[SERIAL NO.] | 
|Fortinet|maintainer|pbcpbn(add-serial-number) | 
|Foscam|admin| | 
|Foundry Networks|| | 
|Foundry Networks|admin|admin | 
|Freetech||Posterie | 
|Freetech|<N/A>|Posterie | 
|FrontRange Solutions|master|access | 
|Fujitsu Siemens||connect | 
|Fujitsu Siemens|manage|!manage | 
|Funk Software|admin|radius | 
|GE Security, Inc.|install|install | 
|GE|museadmin|Muse!Admin | 
|GVC|Administrator|admin | 
|Galacticomm|Sysop|Sysop | 
|Gandalf||console | 
|Gandalf||gandalf | 
|Gandalf||system | 
|Gandalf||xmux | 
|Gateway|admin|admin | 
|Geeklog|username|password | 
|General Instruments|test|test | 
|Gericom|Administrator| | 
|Gigabyte|admin|admin | 
|Globespan Virata|DSL|DSL | 
|GlobespanVirata|root|root | 
|Google|admin|urchin | 
|Gossamer Threads Inc.|admin|admin | 
|Gossamer Threads Inc.|author|author | 
|Gossamer Threads Inc.|guest|guest | 
|GrandStream||admin | 
|GrandStream|Administrator|admin | 
|GrandStream|End User|123 (or blank) | 
|Grandstream Networks, Inc|End User|123 | 
|Grandstream Networks, Inc|admin|admin | 
|Grandstream|admin|1234 | 
|Greatspeed|admin|broadband | 
|Groupee, Inc.|Admin5|4tugboat | 
|GuardOne||guardone | 
|GuardOne|n.a|guardone | 
|Guru|admin|admin | 
|H2O Project|admin|admin | 
|HP|<N/A>| | 
|HP|<N/A>|AUTORAID | 
|HP|Administrator|admin | 
|HP|Factory|56789 | 
|HP|admin|!admin | 
|HP|admin| | 
|HP|admin|admin | 
|HP|admin|isee | 
|HP|root|password | 
|Hayes|system|isp | 
|Hemoco Software|lansweeperuser|mysecretpassword0* | 
|Hewlett Packard|admin|admin | 
|Hewlett-Packard|| | 
|Hewlett-Packard||hewlpack | 
|Hewlett-Packard|<N/A>|hewlpack | 
|Hewlett-Packard|ADVMAIL| | 
|Hewlett-Packard|ADVMAIL|HP | 
|Hewlett-Packard|ADVMAIL|HPOFFICE DATA | 
|Hewlett-Packard|Admin|Admin | 
|Hewlett-Packard|Administrator|The last eight digits of the serial number | 
|Hewlett-Packard|Anonymous| | 
|Hewlett-Packard|FIELD| | 
|Hewlett-Packard|FIELD|HPONLY | 
|Hewlett-Packard|FIELD|HPP187 SYS | 
|Hewlett-Packard|FIELD|HPWORD PUB | 
|Hewlett-Packard|FIELD|LOTUS | 
|Hewlett-Packard|FIELD|MANAGER | 
|Hewlett-Packard|FIELD|MGR | 
|Hewlett-Packard|FIELD|SERVICE | 
|Hewlett-Packard|FIELD|SUPPORT | 
|Hewlett-Packard|HELLO|FIELD.SUPPORT | 
|Hewlett-Packard|HELLO|MANAGER.SYS | 
|Hewlett-Packard|HELLO|MGR.SYS | 
|Hewlett-Packard|HELLO|OP.OPERATOR | 
|Hewlett-Packard|HPSupport|badg3r5 | 
|Hewlett-Packard|MAIL|HPOFFICE | 
|Hewlett-Packard|MAIL|MAIL | 
|Hewlett-Packard|MAIL|MPE | 
|Hewlett-Packard|MAIL|REMOTE | 
|Hewlett-Packard|MAIL|TELESUP | 
|Hewlett-Packard|MANAGER|COGNOS | 
|Hewlett-Packard|MANAGER|HPOFFICE | 
|Hewlett-Packard|MANAGER|ITF3000 | 
|Hewlett-Packard|MANAGER|SECURITY | 
|Hewlett-Packard|MANAGER|SYS | 
|Hewlett-Packard|MANAGER|TCH | 
|Hewlett-Packard|MANAGER|TELESUP | 
|Hewlett-Packard|MGE|VESOFT | 
|Hewlett-Packard|MGR|CAROLIAN | 
|Hewlett-Packard|MGR|CCC | 
|Hewlett-Packard|MGR|CNAS | 
|Hewlett-Packard|MGR|COGNOS | 
|Hewlett-Packard|MGR|CONV | 
|Hewlett-Packard|MGR|HPDESK | 
|Hewlett-Packard|MGR|HPOFFICE | 
|Hewlett-Packard|MGR|HPONLY | 
|Hewlett-Packard|MGR|HPP187 | 
|Hewlett-Packard|MGR|HPP189 | 
|Hewlett-Packard|MGR|HPP196 | 
|Hewlett-Packard|MGR|INTX3 | 
|Hewlett-Packard|MGR|ITF3000 | 
|Hewlett-Packard|MGR|NETBASE | 
|Hewlett-Packard|MGR|REGO | 
|Hewlett-Packard|MGR|RJE | 
|Hewlett-Packard|MGR|ROBELLE | 
|Hewlett-Packard|MGR|SECURITY | 
|Hewlett-Packard|MGR|SYS | 
|Hewlett-Packard|MGR|TELESUP | 
|Hewlett-Packard|MGR|VESOFT | 
|Hewlett-Packard|MGR|WORD | 
|Hewlett-Packard|MGR|XLSERVER | 
|Hewlett-Packard|OPERATOR|COGNOS | 
|Hewlett-Packard|OPERATOR|DISC | 
|Hewlett-Packard|OPERATOR|SUPPORT | 
|Hewlett-Packard|OPERATOR|SYS | 
|Hewlett-Packard|OPERATOR|SYSTEM | 
|Hewlett-Packard|Oper|Oper | 
|Hewlett-Packard|PCUSER|SYS | 
|Hewlett-Packard|RSBCMON|SYS | 
|Hewlett-Packard|SPOOLMAN|HPOFFICE | 
|Hewlett-Packard|WP|HPOFFICE | 
|Hewlett-Packard|admin|admin | 
|Hewlett-Packard|admin|hp.com | 
|Hewlett-Packard|admin|isee | 
|HighPOint|RAID|hpt | 
|Honeynet Project|roo|honey | 
|Honeynet Project|root|honey | 
|Honeywell|LocalComServer|LCS pwd 03 | 
|Honeywell|TPSLocalServer|TLS pwd 03 | 
|Horizon DataSys||foolproof | 
|Hosting Controller|AdvWebadmin|advcomm500349 | 
|Huawei|TMAR#HWMT8007079| | 
|Huawei Technologies Co|TMAR#HWMT8007079| | 
|Huawei Technologies Co|admin|admin | 
|Huawei|admin|admin | 
|Hyperic, Inc.|hqadmin|hqadmin | 
|IBM|$ALOC$| | 
|IBM|$SRV|$SRV | 
|IBM|11111111|11111111 | 
|IBM|22222222|22222222 | 
|IBM||IBM | 
|IBM||MBIU0 | 
|IBM||ascend | 
|IBM||sertafu | 
|IBM|<N/A>| | 
|IBM|<N/A>|IBM | 
|IBM|<N/A>|MBIU0 | 
|IBM|<N/A>|R1QTPS | 
|IBM|<N/A>|admin | 
|IBM|<N/A>|ascend | 
|IBM|<N/A>|sertafu | 
|IBM|ADMIN| | 
|IBM|AP2SVP| | 
|IBM|APL2PP| | 
|IBM|AUTOLOG1| | 
|IBM|Administrator|admin | 
|IBM|BATCH| | 
|IBM|BATCH1| | 
|IBM|BATCH2| | 
|IBM|CCC| | 
|IBM|CICSUSER|CISSUS | 
|IBM|CMSBATCH| | 
|IBM|CMSBATCH|CMSBATCH | 
|IBM|CMSUSER| | 
|IBM|CPNUC| | 
|IBM|CPRM| | 
|IBM|CSPUSER| | 
|IBM|CVIEW| | 
|IBM|DATAMOVE| | 
|IBM|DBDCCICS|DBDCCIC | 
|IBM|DEMO1| | 
|IBM|DEMO2| | 
|IBM|DEMO3| | 
|IBM|DEMO4| | 
|IBM|DIRECT| | 
|IBM|DIRMAINT| | 
|IBM|DISKCNT| | 
|IBM|EREP| | 
|IBM|ESSEX| | 
|IBM|FORSE|FORSE | 
|IBM|FSFADMIN| | 
|IBM|FSFTASK1| | 
|IBM|FSFTASK2| | 
|IBM|GCS| | 
|IBM|IBMUSER|SYS1 | 
|IBM|IDMS| | 
|IBM|IDMSSE| | 
|IBM|IIPS| | 
|IBM|IPC| | 
|IBM|IPFSERV| | 
|IBM|ISPVM| | 
|IBM|IVPM1| | 
|IBM|IVPM2| | 
|IBM|MAINT| | 
|IBM|MAINT|MAINT | 
|IBM|MOESERV| | 
|IBM|NEVIEW| | 
|IBM|OLTSEP| | 
|IBM|OP1| | 
|IBM|OPER|OPER | 
|IBM|OPERATIONS|OPERATIONS | 
|IBM|OPERATNS| | 
|IBM|OPERATNS|OPERATNS | 
|IBM|OPERATOR| | 
|IBM|Operator|Operator | 
|IBM|PDMREMI| | 
|IBM|PENG| | 
|IBM|POST|BASE | 
|IBM|PROCAL| | 
|IBM|PRODBM| | 
|IBM|PRODCICS|PRODCICS | 
|IBM|PROG|PROG | 
|IBM|PROMAIL| | 
|IBM|PSFMAINT| | 
|IBM|PVM| | 
|IBM|QSRV|11111111 | 
|IBM|QSRV|22222222 | 
|IBM|QSRV|QSRV | 
|IBM|RDM470| | 
|IBM|ROUTER| | 
|IBM|RSCS| | 
|IBM|RSCSV2| | 
|IBM|SAVSYS| | 
|IBM|SFCMI| | 
|IBM|SFCNTRL| | 
|IBM|SMART| | 
|IBM|SQLDBA| | 
|IBM|SQLUSER| | 
|IBM|SYSA|SYSA | 
|IBM|SYSADMIN| | 
|IBM|SYSCKP| | 
|IBM|SYSDUMP1| | 
|IBM|SYSERR| | 
|IBM|SYSWRM| | 
|IBM|TDISK| | 
|IBM|TEMP| | 
|IBM|TSAFVM| | 
|IBM|USERID|PASSW0RD | 
|IBM|USERID|PASSWORD | 
|IBM|VASTEST| | 
|IBM|VCSRV|VCSRV | 
|IBM|VM3812| | 
|IBM|VMARCH| | 
|IBM|VMASMON| | 
|IBM|VMASSYS| | 
|IBM|VMBACKUP| | 
|IBM|VMBSYSAD| | 
|IBM|VMMAP| | 
|IBM|VMTAPE| | 
|IBM|VMTLIBR| | 
|IBM|VMUTIL| | 
|IBM|VSEIPO| | 
|IBM|VSEMAINT| | 
|IBM|VSEMAN| | 
|IBM|VTAM| | 
|IBM|VTAM|VTAM | 
|IBM|VTAMUSER| | 
|IBM|admin| | 
|IBM|admin|admin | 
|IBM|admin|password | 
|IBM|admin|secure | 
|IBM|db2fenc1|db2fenc1 | 
|IBM|db2inst1|db2inst1 | 
|IBM|fg_sysadmin|password | 
|IBM|guest| | 
|IBM|guest|guest | 
|IBM|hscroot|abc123 | 
|IBM|ibm|2222 | 
|IBM|ibm|password | 
|IBM|ibm|service | 
|IBM|qpgmr|qpgmr | 
|IBM|qsecofr|11111111 | 
|IBM|qsecofr|22222222 | 
|IBM|qsecofr|qsecofr | 
|IBM|qserv|qserv | 
|IBM|qsrv|qsrv | 
|IBM|qsrvbas|qsrvbas | 
|IBM|qsvr|ibmcel | 
|IBM|qsvr|qsvr | 
|IBM|qsysopr|qsysopr | 
|IBM|quser|quser | 
|IBM|root| | 
|IBM|root|passw0rd | 
|IBM|secofr|secofr | 
|IBM|sedacm|secacm | 
|IBM|storwatch|specialist | 
|IBM|superadmin|secret | 
|IBM|sysopr|sysopr | 
|IBM|user|USERP | 
|IBM|vt100|public | 
|IBM|webadmin|webibm | 
|IBM|wpsadmin|wpsadmin | 
|INOVA|iclock|timely | 
|IQinVision|root|system | 
|IRC||FOOBAR | 
|Inedo|Admin|Admin | 
|Infoblox|admin| | 
|Informix|informix|informix | 
|Infosmart|admin|0 | 
|Infrant|admin|infrant1 | 
|Innovaphone|admin|ip20 | 
|Innovaphone|admin|ip21 | 
|Innovaphone|admin|ip3000 | 
|Innovaphone|admin|ip305Beheer | 
|Innovaphone|admin|ip400 | 
|Inova|iclock|timely | 
|Integral|Administrator|letmein | 
|Integrated Networks|Administrator|1234 | 
|Integrated Networks|Administrator|12345678 | 
|Integrated Networks|Administrator|19750407 | 
|Intel||Intel | 
|Intel||isolation | 
|Intel||shiva | 
|Intel|Guest| | 
|Intel|NICONEX|NICONEX | 
|Intel|intel|intel | 
|Intel|root| | 
|Intel|setup|setup | 
|Intel/Shiva|admin|hello | 
|IntelliTouch|administrator|1234 | 
|Interbase|SYSDBA|masterkey | 
|Intermec||intermec | 
|Intermec|intermec|intermec | 
|Internet Archive|admin|letmein | 
|Intershop|operator|$chwarzepumpe | 
|Intersystems|system|sys | 
|Intracom|admin|admin | 
|Inventel Wanadoo|Admin|Admin | 
|Inventel|admin|admin | 
|Ipswitch|XXSESS_MGRYY|X#1833 | 
|Ipswitch|admin|admin | 
|Ipswitch|guest| | 
|IronPort|admin|ironport | 
|Irongate|admin|NetSurvibox | 
|Iwill||iwill | 
|Iwill|<N/A>|iwill | 
|JAHT|admin|epicrouter | 
|JAMF Software|jamfsoftware|jamfsw03 | 
|JD Edwards|JDE|JDE | 
|JDE|PRODDTA|PRODDTA | 
|JDS Microprocessing|hydrasna| | 
|JDS|hydrasna| | 
|Janitza|Homepage Password|0th | 
|Janitza|admin|Janitza | 
|Janitza|guest|Janitza | 
|Janitza|user|Janitza | 
|Jaspersoft Corporation|demo|demo | 
|Jaspersoft Corporation|jasperadmin|jasperadmin | 
|Jaspersoft Corporation|joeuser|joeuser | 
|Jaspersoft Corporation|superuser|superuser | 
|Jean-Philippe Lang|admin|admin | 
|Jeebles Technology||admin | 
|JetWay||spooml | 
|JetWay|<N/A>|spooml | 
|Jetform|Jetform| | 
|JioFi (web)|administrator|administrator|
|Johnson Controls|johnson|control | 
|Joss Technology||57gbzb | 
|Joss Technology||technolgi | 
|Joss Technology|<N/A>|57gbzb | 
|Joss Technology|<N/A>|technolgi | 
|Juniper|admin|abc123 | 
|Juniper|admin|netscreen | 
|Juniper|admin|peribit | 
|Juniper|netscreen|netscreen | 
|Juniper|redline|redline | 
|Juniper|serial#|serial# | 
|Juniper|super|juniper123 | 
|Justin Hagstrom|admin|admin | 
|Justin Hagstrom|test|test | 
|KASDA|admin|adslroot | 
|KTI|admin|123 | 
|KTI|admin|123456 | 
|KTI|superuser|123456 | 
|Kalatel|<N/A>|3477 | 
|Kalatel|<N/A>|8111 | 
|Kentico Software|administrator| | 
|Kethinov|root|password | 
|Keyscan|keyscan|KEYSCAN | 
|Kodak|PACSLinkIP|NetServer | 
|Kodak|PLMIMService|NetServer | 
|Kodak|RNIServiceManager|NetServer | 
|Kodak|SA|PASSWORD | 
|Kodak|Service|Service | 
|Kodi|kodi|kodi | 
|Konica Minolta||0000 | 
|Konica Minolta||1234 | 
|Konica Minolta|| | 
|Konica Minolta||MagiMFP | 
|Konica Minolta||sysAdmin | 
|Konica Minolta|<N/A>|0 | 
|Konica Minolta|<N/A>|sysadm | 
|Konica Minolta|admin|administrator | 
|Kronos|SuperUser|kronites | 
|Kyocera|2800|2800 | 
|Kyocera||admin00 | 
|Kyocera|<N/A>|PASSWORD | 
|Kyocera|<N/A>|admin00 | 
|Kyocera|admin| | 
|Kyocera|admin|admin | 
|Kyocera|root|root | 
|LANCOM|<N/A>| | 
|LANSA|WEBADM|password | 
|LANSA|admin|admin | 
|LANSA|dev|dev | 
|LAXO|admin|admin | 
|LG||jannie | 
|LG|admin|epicrouter | 
|LG|vikram|singh | 
|LGIC|LR-ISDN|LR-ISDN | 
|LaCie|admin|admin | 
|Lanier||sysadm | 
|Lanier|admin| | 
|Lanier|supervisor| | 
|Lantronics||access | 
|Lantronics||system | 
|Lantronix||access | 
|Lantronix|<N/A>| | 
|Lantronix|<N/A>|access | 
|Lantronix|<N/A>|admin | 
|Lantronix|<N/A>|lantronix | 
|Lantronix|<N/A>|system | 
|Lantronix|login|access | 
|Lantronix|sysadmin|PASS | 
|Leading Edge||MASTER | 
|Leading Edge|<N/A>|MASTER | 
|Lenel|admin|admin | 
|Level1|admin|admin | 
|Leviton|admin|leviton | 
|Liebert|Liebert|Liebert | 
|Lindsay Electronics|ADMINISTRATOR|SENTINEL | 
|Lindsay Electronics|SENTINEL|SENTINEL | 
|Linksys||admin | 
|Linksys||epicrouter | 
|Linksys|<N/A>| | 
|Linksys|<N/A>|admin | 
|Linksys|Administrator|admin | 
|Linksys|admin| | 
|Linksys|admin|admin | 
|Linksys|comcast|1234 | 
|Linksys|root|orion99 | 
|Linksys|user|tivonpw | 
|Linux|gonzo| | 
|Linux|root|uClinux | 
|Linux|satan| | 
|Linux|snake| | 
|Liquidware Labs, Inc.|ssadmin|sspassword | 
|Livingston|!root| | 
|Livingstone|root| | 
|Lockdown|setup|changeme! | 
|LogiLink|admin|1234 | 
|Logitech||0 | 
|Loglogic|root|logapp | 
|Loglogic|toor|logapp | 
|Longshine|admin|0 | 
|Lucent|(any 3 characters)|cascade | 
|Lucent|(any 3 chars)|cascade | 
|Lucent|<N/A>|admin | 
|Lucent|<N/A>|cascade | 
|Lucent|Administrator| | 
|Lucent|LUCENT01|UI-PSWD-01 | 
|Lucent|LUCENT02|UI-PSWD-02 | 
|Lucent|admin|AitbISP4eCiG | 
|Lucent|admin|Ascend | 
|Lucent|bciim|bciimpw | 
|Lucent|bcim|bcimpw | 
|Lucent|bcms|bcmspw | 
|Lucent|bcnas|bcnaspw | 
|Lucent|blue|bluepw | 
|Lucent|browse|browsepw | 
|Lucent|browse|looker | 
|Lucent|craft|craft | 
|Lucent|craft|craftpw | 
|Lucent|cust|custpw | 
|Lucent|enquiry|enquirypw | 
|Lucent|field|support | 
|Lucent|inads|inads | 
|Lucent|inads|indspw | 
|Lucent|init|initpw | 
|Lucent|locate|locatepw | 
|Lucent|maint|maintpw | 
|Lucent|maint|rwmaint | 
|Lucent|nms|nmspw | 
|Lucent|pw|pwpw | 
|Lucent|rcust|rcustpw | 
|Lucent|readonly|lucenttech2 | 
|Lucent|readwrite|lucenttech1 | 
|Lucent|root|ascend | 
|Lucent|super|super | 
|Lucent|support|supportpw | 
|Lucent|sysadm|admpw | 
|Lucent|sysadm|sysadmpw | 
|Lucent|sysadm|syspw | 
|Lucent|tech|field | 
|Luxon Communications|administrator|19750407 | 
|M Technology||mMmM | 
|M Technology|<N/A>|mMmM | 
|MERCURY|Administrator|admin | 
|MP3Mystic|admin|mp3mystic | 
|MRV|admin|admin | 
|MTNL|admin|admin | 
|MachSpeed||sp99dd | 
|MachSpeed|<N/A>|sp99dd | 
|Macromedia|<N/A>|admin | 
|Macsense|admin|admin | 
|Magento|admin|123123 | 
|Magic-Pro||prost | 
|Magic-Pro|<N/A>|prost | 
|Main Street Softworks|MCVEADMIN|password | 
|Mambo|admin|admin | 
|ManageEngine|admin|admin | 
|Mandarin Library Automation|admin|boca raton | 
|Mantis|administrator|root | 
|Marconi|ami| | 
|McAfee|admin|admin123 | 
|McAfee|scmadmin|scmchangeme | 
|McAfee|webshield|webshieldchangeme | 
|McData|Administrator|password | 
|McData|McdataSE|redips | 
|Mediatrix|admin|1234 | 
|Mediatrix|administrator| | 
|Megastar||star | 
|Megastar|<N/A>|star | 
|Memotec|memotec|supervisor | 
|Mentec|MICRO|RSX | 
|Mercury Interactive|admin|admin | 
|Meridian|service|smile | 
|Michiel|admin|phplist | 
|Microcom|admin|epicrouter | 
|Microcom|admin|superuser | 
|Microcom|user|password | 
|Micron||sldkj754 | 
|Micron||xyzall | 
|Micron|<N/A>|sldkj754 | 
|Micron|<N/A>|xyzall | 
|Micronet|admin|admin | 
|Micronet|admin|epicrouter | 
|Micronet|mac| | 
|Micronet|root|default | 
|Micronics||dn_04rjc | 
|Micronics|<N/A>|dn_04rjc | 
|Microplex|root|root | 
|Microsoft|| | 
|Microsoft||admin | 
|Microsoft||sa | 
|Microsoft|Administrator| | 
|Microsoft|Administrator|Administrator | 
|Microsoft|Guest| | 
|Microsoft|Guest|Guest | 
|Microsoft|IS_$hostname|IS_$hostname | 
|Microsoft|LDAP_Anonymous|LdapPassword_1 | 
|Microsoft|LessonUser1| | 
|Microsoft|LessonUser2| | 
|Microsoft|MSHOME|MSHOME | 
|Microsoft|User|User | 
|Microsoft|sa| | 
|Mike Peters|bsxuser|bsxpass | 
|MikroTik|admin| | 
|Mikrotik|admin| | 
|Milan|root|root | 
|Minolta PagrPro|<N/A>|sysadm | 
|Minolta QMS|admin| | 
|Minolta QMS|operator| | 
|Mintel||SYSTEM | 
|Mintel|<N/A>|SYSTEM | 
|Mitel|<N/A>| | 
|Mitel Networks|1nstaller|5X2000 | 
|Mitel Networks|installer|sx2000 | 
|Mitel Networks|maint1|sx2000 | 
|Mitel Networks|maint2|sx2000 | 
|Mitel Networks|s1stem|5X2000 | 
|Mitel Networks|system|sx2000 | 
|Mitel|installer|1000 | 
|Mitel|system|mnet | 
|Mitel|system|password | 
|Mobotix|admin|meinsm | 
|Mole|admin|admin | 
|Motive|admin|isee | 
|Motorola||0000 | 
|Motorola|admin|motorola | 
|Motorola|admin|password | 
|Motorola|cablecom|router | 
|Motorola|service|smile | 
|Motorola|setup| | 
|Motorola|technician|yZgO8Bvj | 
|Mutare||admin | 
|Muze|admin|muze | 
|MySQL|admin@example.com|admin | 
|MySQL|root| | 
|MySQL|superdba|admin | 
|MyioSoft|demo|demo | 
|NAI|GlobalAdmin|GlobalAdmin | 
|NAI|admin|admin123 | 
|NCR|ncrm|ncrm | 
|NEC|<N/A>| | 
|NEC|admin|password | 
|NGSEcure|admin|admin | 
|NGSec|admin| | 
|NGSec|admin|asd | 
|NICE Systems Ltd.|Administrator|nicecti | 
|NICE Systems Ltd.|Nice-admin|nicecti | 
|NOMADIX|admin| | 
|NRG or RICOH||password | 
|NSI|root|nsi | 
|Nanoteq|admin|NetSeq | 
|NeXT|me| | 
|NeXT|root|NeXT | 
|NeXT|signa|signa | 
|NetApp|admin|NetCache | 
|NetApp|admin|admin123 | 
|NetBotz|netbotz|netbotz | 
|NetGenesis|naadmin|naadmin | 
|Netasq|admin|admin | 
|Netcomm||admin | 
|Netcomm|admin|password | 
|Netcomm|user|password | 
|Netcordia|admin|admin | 
|Netgear||1234 | 
|Netgear||admin | 
|Netgear||private | 
|Netgear||zebra | 
|Netgear|<N/A>| | 
|Netgear|<N/A>|admin | 
|Netgear|<N/A>|password | 
|Netgear|Admin|password | 
|Netgear|Gearguy|Geardog | 
|Netgear|admin|1234 | 
|Netgear|admin| | 
|Netgear|admin|admin | 
|Netgear|admin|draadloos | 
|Netgear|admin|infrant1 | 
|Netgear|admin|netgear1 | 
|Netgear|admin|password | 
|Netgear|admin|setup | 
|Netgear|comcast|1234 | 
|Netgear|cusadmin|highspeed | 
|Netgear|super|5777364 | 
|Netgear|superman|21241036 | 
|Netopia|| | 
|Netopia|<N/A>| | 
|Netopia|admin| | 
|Netopia|admin|noway | 
|Netopia|factory|(see note) | 
|Netopia|netopia|netopia | 
|Netport|setup|setup | 
|Netscape|admin|admin | 
|Netscreen|<N/A>| | 
|Netscreen|Administrator| | 
|Netscreen|admin| | 
|Netscreen|admin|netscreen | 
|Netscreen|netscreen|netscreen | 
|Netscreen|operator| | 
|Netstar|admin|password | 
|Network Appliance|admin|NetCache | 
|Network Associates|e250|e250changeme | 
|Network Associates|e500|e500changeme | 
|Network Everywhere||admin | 
|NetworkICE|iceman| | 
|NewMedia-NET GmbH|root|admin | 
|Nexsan|ADMIN|PASSWORD | 
|Niksun|vcr|NetVCR | 
|Nimble||xdfk9874t3 | 
|Nimble|<N/A>|xdfk9874t3 | 
|Nokia||9999 | 
|Nokia||Telecom | 
|Nokia||nokai | 
|Nokia||nokia | 
|Nokia|Security Code|12345 | 
|Nokia|Telecom|Telecom | 
|Nokia|client|client | 
|Nokia|m1122|m1122 | 
|Nokia|nop|12345 | 
|Nokia|nop|123454 | 
|Nokia|root|nokia | 
|Nokia|root|rootme | 
|Nokia|telecom|telecom | 
|Norstar|**23646|23646 | 
|Norstar|**266344|266344 | 
|Nortel|266344|266344 | 
|Nortel||0 | 
|Nortel|| | 
|Nortel||l1 | 
|Nortel||l2 | 
|Nortel||ro | 
|Nortel||rw | 
|Nortel||rwa | 
|Nortel||secure | 
|Nortel|<N/A>|266344 | 
|Nortel|<N/A>| | 
|Nortel|<N/A>|secure | 
|Nortel|Manager| | 
|Nortel|admin|000000 | 
|Nortel|admin| | 
|Nortel|admin|admin | 
|Nortel|admin|admin000 | 
|Nortel|admin|root | 
|Nortel|admin|setup | 
|Nortel|administrator|PlsChgMe! | 
|Nortel|ccrusr|ccrusr | 
|Nortel|conferencing|admin | 
|Nortel|debug|gubed | 
|Nortel|distrib|distrib0 | 
|Nortel|disttech|4tas | 
|Nortel|disttech|disttech | 
|Nortel|disttech|etas | 
|Nortel|l2|l2 | 
|Nortel|l3|l3 | 
|Nortel|login|0 | 
|Nortel|login|0000 | 
|Nortel|login|1111 | 
|Nortel|login|8429 | 
|Nortel|maint|maint | 
|Nortel|maint|ntacdmax | 
|Nortel|mlusr|mlusr | 
|Nortel|ro|ro | 
|Nortel|root|3ep5w2u | 
|Nortel|rw|rw | 
|Nortel|rwa|rwa | 
|Nortel|service|smile | 
|Nortel|spcl|0 | 
|Nortel|spcl|0000 | 
|Nortel|supervisor|PlsChgMe! | 
|Nortel|supervisor|visor | 
|Nortel|sysadmin|nortel | 
|Nortel|system|adminpwd | 
|Nortel|tasman|tasmannet | 
|Nortel|trmcnfg|trmcnfg | 
|Nortel|user| | 
|Nortel|user|user | 
|Nortel|user|user0000 | 
|Novell||cr0wmt 911 | 
|Novell||root | 
|Novell||san fran 8 | 
|Novell|ADMIN| | 
|Novell|ADMIN|ADMIN | 
|Novell|ADMIN|admin | 
|Novell|ARCHIVIST| | 
|Novell|ARCHIVIST|ARCHIVIST | 
|Novell|BACKUP| | 
|Novell|BACKUP|BACKUP | 
|Novell|CHEY_ARCHSVR| | 
|Novell|CHEY_ARCHSVR|CHEY_ARCHSVR | 
|Novell|FAX| | 
|Novell|FAX|FAX | 
|Novell|FAXUSER| | 
|Novell|FAXUSER|FAXUSER | 
|Novell|FAXWORKS| | 
|Novell|FAXWORKS|FAXWORKS | 
|Novell|GATEWAY| | 
|Novell|GATEWAY|GATEWAY | 
|Novell|GUEST| | 
|Novell|GUEST|GUEST | 
|Novell|GUEST|GUESTGUE | 
|Novell|GUEST|GUESTGUEST | 
|Novell|GUEST|TSEUG | 
|Novell|HPLASER| | 
|Novell|HPLASER|HPLASER | 
|Novell|LASER| | 
|Novell|LASER|LASER | 
|Novell|LASERWRITER| | 
|Novell|LASERWRITER|LASERWRITER | 
|Novell|MAIL| | 
|Novell|MAIL|MAIL | 
|Novell|POST| | 
|Novell|POST|POST | 
|Novell|PRINT| | 
|Novell|PRINT|PRINT | 
|Novell|PRINTER| | 
|Novell|PRINTER|PRINTER | 
|Novell|ROOT| | 
|Novell|ROOT|ROOT | 
|Novell|ROUTER| | 
|Novell|SABRE| | 
|Novell|SUPERVISOR| | 
|Novell|SUPERVISOR|HARRIS | 
|Novell|SUPERVISOR|NETFRAME | 
|Novell|SUPERVISOR|NF | 
|Novell|SUPERVISOR|NFI | 
|Novell|SUPERVISOR|SUPERVISOR | 
|Novell|SUPERVISOR|SYSTEM | 
|Novell|TEST| | 
|Novell|TEST|TEST | 
|Novell|USER_TEMPLATE| | 
|Novell|USER_TEMPLATE|USER_TEMPLATE | 
|Novell|WANGTEK| | 
|Novell|WANGTEK|WANGTEK | 
|Novell|WINDOWS_PASSTHRU| | 
|Novell|WINDOWS_PASSTHRU|WINDOWS_PASSTHRU | 
|Novell|WINSABRE|SABRE | 
|Novell|WINSABRE|WINSABRE | 
|Novell|admin|admin | 
|Novell|admin|novell | 
|Novell|sadmin| | 
|Novell|servlet|manager | 
|Nullsoft|admin|changeme | 
|Nurit|$system| | 
|OCE|<N/A>|0 and the number of OCE printer | 
|ODS|ods|ods | 
|OMRON|<N/A>| | 
|OPEN Networks|root|0P3N | 
|OSMC|osmc|osmc | 
|OTRS Inc.|root@localhost|root | 
|Oki|admin|<SEE COMMENT> | 
|Oki|admin|OkiLAN | 
|Oki|root|<SEE COMMENT> | 
|Oleg Khabarov|username|password | 
|Olicom|<N/A>|AaBbCcDd | 
|Omnitronix||SMDR | 
|Omnitronix||SUPER | 
|Open-Xchange Inc.|mailadmin|secret | 
|OpenConnect|admin|OCS | 
|OpenConnect|adminstat|OCS | 
|OpenConnect|adminuser|OCS | 
|OpenConnect|adminview|OCS | 
|OpenConnect|helpdesk|OCS | 
|OpenMarket|Bobo|hello | 
|OpenMarket|Coco|hello | 
|OpenMarket|Flo|hello | 
|OpenMarket|Joe|hello | 
|OpenMarket|Moe|hello | 
|OpenMarket|admin|demo | 
|OpenMarket|user_analyst|demo | 
|OpenMarket|user_approver|demo | 
|OpenMarket|user_author|demo | 
|OpenMarket|user_checker|demo | 
|OpenMarket|user_designer|demo | 
|OpenMarket|user_editor|demo | 
|OpenMarket|user_expert|demo | 
|OpenMarket|user_marketer|demo | 
|OpenMarket|user_pricer|demo | 
|OpenMarket|user_publisher|demo | 
|Openlink|admin|admin | 
|Openwave|cac_admin|cacadmin | 
|Openwave|sys|uplink | 
|Optivision|root|mpegvideo | 
|Oracle|<N/A>| | 
|Oracle|ADAMS|WOOD | 
|Oracle|ADLDEMO|ADLDEMO | 
|Oracle|ADMIN|JETSPEED | 
|Oracle|ADMIN|WELCOME | 
|Oracle|ADMINISTRATOR|ADMINISTRATOR | 
|Oracle|ADMINISTRATOR|admin | 
|Oracle|ANDY|SWORDFISH | 
|Oracle|AP|AP | 
|Oracle|APPLSYS|APPLSYS | 
|Oracle|APPLSYS|FND | 
|Oracle|APPLSYSPUB|FNDPUB | 
|Oracle|APPS|APPS | 
|Oracle|APPUSER|APPUSER | 
|Oracle|AQ|AQ | 
|Oracle|AQDEMO|AQDEMO | 
|Oracle|AQJAVA|AQJAVA | 
|Oracle|AQUSER|AQUSER | 
|Oracle|AUDIOUSER|AUDIOUSER | 
|Oracle|AURORA$JIS$UTILITY$| | 
|Oracle|AURORA$ORB$UNAUTHENTICATED|INVALID | 
|Oracle|AURORA@ORB@UNAUTHENTICATED|INVALID | 
|Oracle|BC4J|BC4J | 
|Oracle|BLAKE|PAPER | 
|Oracle|BRIO_ADMIN|BRIO_ADMIN | 
|Oracle|CATALOG|CATALOG | 
|Oracle|CDEMO82|CDEMO82 | 
|Oracle|CDEMOCOR|CDEMOCOR | 
|Oracle|CDEMORID|CDEMORID | 
|Oracle|CDEMOUCB|CDEMOUCB | 
|Oracle|CENTRA|CENTRA | 
|Oracle|CIDS|CIDS | 
|Oracle|CIS|CIS | 
|Oracle|CISINFO|CISINFO | 
|Oracle|CLARK|CLOTH | 
|Oracle|COMPANY|COMPANY | 
|Oracle|COMPIERE|COMPIERE | 
|Oracle|CQSCHEMAUSER|PASSWORD | 
|Oracle|CSMIG|CSMIG | 
|Oracle|CTXDEMO|CTXDEMO | 
|Oracle|CTXSYS| | 
|Oracle|CTXSYS|CTXSYS | 
|Oracle|DBI|MUMBLEFRATZ | 
|Oracle|DBSNMP|DBSNMP | 
|Oracle|DEMO|DEMO | 
|Oracle|DEMO8|DEMO8 | 
|Oracle|DEMO9|DEMO9 | 
|Oracle|DES|DES | 
|Oracle|DEV2000_DEMOS|DEV2000_DEMOS | 
|Oracle|DIP|DIP | 
|Oracle|DISCOVERER_ADMIN|DISCOVERER_ADMIN | 
|Oracle|DSGATEWAY|DSGATEWAY | 
|Oracle|DSSYS|DSSYS | 
|Oracle|EJSADMIN|EJSADMIN | 
|Oracle|EMP|EMP | 
|Oracle|ESTOREUSER|ESTORE | 
|Oracle|EVENT|EVENT | 
|Oracle|EXFSYS|EXFSYS | 
|Oracle|FINANCE|FINANCE | 
|Oracle|FND|FND | 
|Oracle|FROSTY|SNOWMAN | 
|Oracle|GL|GL | 
|Oracle|GPFD|GPFD | 
|Oracle|GPLD|GPLD | 
|Oracle|HCPARK|HCPARK | 
|Oracle|HLW|HLW | 
|Oracle|HR|HR | 
|Oracle|IMAGEUSER|IMAGEUSER | 
|Oracle|IMEDIA|IMEDIA | 
|Oracle|JMUSER|JMUSER | 
|Oracle|JONES|STEEL | 
|Oracle|JWARD|AIROPLANE | 
|Oracle|L2LDEMO|L2LDEMO | 
|Oracle|LBACSYS|LBACSYS | 
|Oracle|LIBRARIAN|SHELVES | 
|Oracle|MASTER|PASSWORD | 
|Oracle|MDDEMO|MDDEMO | 
|Oracle|MDDEMO_CLERK|CLERK | 
|Oracle|MDDEMO_MGR|MGR | 
|Oracle|MDSYS|MDSYS | 
|Oracle|MFG|MFG | 
|Oracle|MGWUSER|MGWUSER | 
|Oracle|MIGRATE|MIGRATE | 
|Oracle|MILLER|MILLER | 
|Oracle|MMO2|MMO2 | 
|Oracle|MODTEST|YES | 
|Oracle|MOREAU|MOREAU | 
|Oracle|MTSSYS|MTSSYS | 
|Oracle|MTS_USER|MTS_PASSWORD | 
|Oracle|MTYSYS|MTYSYS | 
|Oracle|MXAGENT|MXAGENT | 
|Oracle|NAMES|NAMES | 
|Oracle|OAS_PUBLIC|OAS_PUBLIC | 
|Oracle|OCITEST|OCITEST | 
|Oracle|ODM|ODM | 
|Oracle|ODM_MTR|MTRPW | 
|Oracle|ODS|ODS | 
|Oracle|ODSCOMMON|ODSCOMMON | 
|Oracle|OE|OE | 
|Oracle|OEMADM|OEMADM | 
|Oracle|OEMREP|OEMREP | 
|Oracle|OLAPDBA|OLAPDBA | 
|Oracle|OLAPSVR|INSTANCE | 
|Oracle|OLAPSYS|MANAGER | 
|Oracle|OMWB_EMULATION|ORACLE | 
|Oracle|OO|OO | 
|Oracle|OPENSPIRIT|OPENSPIRIT | 
|Oracle|ORACACHE|(random password) | 
|Oracle|ORAREGSYS|ORAREGSYS | 
|Oracle|ORASSO|ORASSO | 
|Oracle|ORDPLUGINS|ORDPLUGINS | 
|Oracle|ORDSYS|ORDSYS | 
|Oracle|OSE$HTTP$ADMIN|(random password) | 
|Oracle|OSP22|OSP22 | 
|Oracle|OUTLN|OUTLN | 
|Oracle|OWA|OWA | 
|Oracle|OWA_PUBLIC|OWA_PUBLIC | 
|Oracle|OWNER|OWNER | 
|Oracle|PANAMA|PANAMA | 
|Oracle|PATROL|PATROL | 
|Oracle|PERFSTAT|PERFSTAT | 
|Oracle|PLEX|PLEX | 
|Oracle|PLSQL|SUPERSECRET | 
|Oracle|PM|PM | 
|Oracle|PO|PO | 
|Oracle|PO7|PO7 | 
|Oracle|PO8|PO8 | 
|Oracle|PORTAL30|PORTAL30 | 
|Oracle|PORTAL30|PORTAL31 | 
|Oracle|PORTAL30_DEMO|PORTAL30_DEMO | 
|Oracle|PORTAL30_PUBLIC|PORTAL30_PUBLIC | 
|Oracle|PORTAL30_SSO|PORTAL30_SSO | 
|Oracle|PORTAL30_SSO_PS|PORTAL30_SSO_PS | 
|Oracle|PORTAL30_SSO_PUBLIC|PORTAL30_SSO_PUBLIC | 
|Oracle|POWERCARTUSER|POWERCARTUSER | 
|Oracle|PRIMARY|PRIMARY | 
|Oracle|PUBSUB|PUBSUB | 
|Oracle|PUBSUB1|PUBSUB1 | 
|Oracle|QDBA|QDBA | 
|Oracle|QS|QS | 
|Oracle|QS_ADM|QS_ADM | 
|Oracle|QS_CB|QS_CB | 
|Oracle|QS_CBADM|QS_CBADM | 
|Oracle|QS_CS|QS_CS | 
|Oracle|QS_ES|QS_ES | 
|Oracle|QS_OS|QS_OS | 
|Oracle|QS_WS|QS_WS | 
|Oracle|RE|RE | 
|Oracle|REPADMIN|REPADMIN | 
|Oracle|REPORTS_USER|OEM_TEMP | 
|Oracle|REP_MANAGER|DEMO | 
|Oracle|REP_OWNER|DEMO | 
|Oracle|REP_OWNER|REP_OWNER | 
|Oracle|RMAIL|RMAIL | 
|Oracle|RMAN|RMAN | 
|Oracle|SAMPLE|SAMPLE | 
|Oracle|SAP|SAPR3 | 
|Oracle|SCOTT|TIGER | 
|Oracle|SDOS_ICSAP|SDOS_ICSAP | 
|Oracle|SECDEMO|SECDEMO | 
|Oracle|SERVICECONSUMER1|SERVICECONSUMER1 | 
|Oracle|SH|SH | 
|Oracle|SITEMINDER|SITEMINDER | 
|Oracle|SLIDE|SLIDEPW | 
|Oracle|STARTER|STARTER | 
|Oracle|STRAT_USER|STRAT_PASSWD | 
|Oracle|SWPRO|SWPRO | 
|Oracle|SWUSER|SWUSER | 
|Oracle|SYMPA|SYMPA | 
|Oracle|SYS|CHANGE_ON_INSTALL | 
|Oracle|SYS|D_SYSPW | 
|Oracle|SYSADM|SYSADM | 
|Oracle|SYSMAN|OEM_TEMP | 
|Oracle|SYSMAN|oem_temp | 
|Oracle|SYSTEM|D_SYSTPW | 
|Oracle|SYSTEM|MANAGER | 
|Oracle|TAHITI|TAHITI | 
|Oracle|TDOS_ICSAP|TDOS_ICSAP | 
|Oracle|TESTPILOT|TESTPILOT | 
|Oracle|TRACESRV|TRACE | 
|Oracle|TRACESVR|TRACE | 
|Oracle|TRAVEL|TRAVEL | 
|Oracle|TSDEV|TSDEV | 
|Oracle|TSUSER|TSUSER | 
|Oracle|TURBINE|TURBINE | 
|Oracle|ULTIMATE|ULTIMATE | 
|Oracle|USER|USER | 
|Oracle|USER0|USER0 | 
|Oracle|USER1|USER1 | 
|Oracle|USER2|USER2 | 
|Oracle|USER3|USER3 | 
|Oracle|USER4|USER4 | 
|Oracle|USER5|USER5 | 
|Oracle|USER6|USER6 | 
|Oracle|USER7|USER7 | 
|Oracle|USER8|USER8 | 
|Oracle|USER9|USER9 | 
|Oracle|UTLBSTATU|UTLESTAT | 
|Oracle|VIDEOUSER|VIDEO USER | 
|Oracle|VIF_DEVELOPER|VIF_DEV_PWD | 
|Oracle|VIRUSER|VIRUSER | 
|Oracle|VRR1|VRR1 | 
|Oracle|WEBCAL01|WEBCAL01 | 
|Oracle|WEBDB|WEBDB | 
|Oracle|WEBREAD|WEBREAD | 
|Oracle|WKSYS|WKSYS | 
|Oracle|WWW|WWW | 
|Oracle|WWWUSER|WWWUSER | 
|Oracle|XPRT|XPRT | 
|Oracle|admin|admin | 
|Oracle|admin|adminadmin | 
|Oracle|admin|security | 
|Oracle|admin|welcome | 
|Oracle|bpel|bpel | 
|Oracle|cn=orcladmin|welcome | 
|Oracle|demo|demo | 
|Oracle|ilom-admin|ilom-admin | 
|Oracle|ilom-operator|ilom-operator | 
|Oracle|internal|oracle | 
|Oracle|joe|password | 
|Oracle|mary|password | 
|Oracle|nm2user|nm2user | 
|Oracle|oracle|oracle | 
|Oracle|scott|tiger or tigger | 
|Oracle|siteadmin|siteadmin | 
|Oracle|sys|change_on_install | 
|Oracle|sys|sys | 
|Oracle|system|manager | 
|Oracle|system|password | 
|Oracle|system|security | 
|Oracle|system/manager|sys/change_on_install | 
|Oracle|webdb|webdb | 
|Oracle|weblogic|weblogic | 
|Oracle|wlcsystem|wlcsystem | 
|Oracle|wlpisystem|wlpisystem | 
|Orange|admin|admin | 
|Orange|root|1234 | 
|Osicom|Manager|Admin | 
|Osicom|Manager|Manager | 
|Osicom|d.e.b.u.g|User | 
|Osicom|debug|d.e.b.u.g | 
|Osicom|echo|User | 
|Osicom|echo|echo | 
|Osicom|guest|User | 
|Osicom|guest|guest | 
|Osicom|sysadm|Admin | 
|Osicom|sysadm|sysadm | 
|Osicom|write|private | 
|Overland|Factory|56789 | 
|Overland Storage|root|Password | 
|OvisLink Canada Inc.|root|root | 
|OvisLink Canada Inc.|user|user | 
|PBX|tech|nician | 
|PHPReactor|core|phpreactor | 
|PLANET Technology Corp.|admin|ISPMODE | 
|PLANET Technology Corp.|admin|[^_^] | 
|POWERLOGIC|Administrator|Gateway | 
|PRTG|prtgadmin|prtgadmin | 
|Pacific Micro Data|pmd| | 
|Packard Bell||bell9 | 
|Packard Bell|<N/A>|bell9 | 
|Packeteer||touchpwd= | 
|Panasonic||1234 | 
|Panasonic|<N/A>| | 
|Panasonic|admin|1234 | 
|Panasonic|admin|12345 | 
|Pandatel|admin|admin | 
|Parallels|admin|setup | 
|Parrot||0000 | 
|Patton|monitor|monitor | 
|Patton|superuser|superuser | 
|PentaSafe|PSEAdmin|$secure$ | 
|Pentagram|admin|password | 
|Pentaoffice||pento | 
|Perle|admin|superuser | 
|Philips|admin|admin | 
|Phoenix v1.14|Administrator|admin | 
|Pikatel|DSL|DSL | 
|Pirelli|admin|admin | 
|Pirelli|admin|microbusiness | 
|Pirelli|admin|mu | 
|Pirelli|admin|smallbusiness | 
|Pirelli|user|password | 
|Pivotal Software, Inc. |guest|guest | 
|PlainTree||default.password | 
|Planet||default | 
|Planet|admin|1234 | 
|Planet|admin|epicrouter | 
|Planex|admin|0 | 
|PokerTracker Software|postgres|dbpass | 
|PokerTracker Software|postgres|svcPASS83 | 
|Pollsafe|SMDR|SECONDARY | 
|Polycom|| | 
|Polycom||ACCORD | 
|Polycom||admin | 
|Polycom||x6zynd56 | 
|Polycom|Polycom|456 | 
|Polycom|Polycom|SpIp | 
|Polycom|administrator|* * # | 
|PostgreSQL|postgres| | 
|Powerchute|pwrchute|pwrchute | 
|Prestige|admin|1234 | 
|Prestigio|<N/A>| | 
|Prime|dos|dos | 
|Prime|fam|fam | 
|Prime|guest|guest | 
|Prime|guest1|guest | 
|Prime|guest1|guest1 | 
|Prime|mail|mail | 
|Prime|maint|maint | 
|Prime|mfd|mfd | 
|Prime|netlink|netlink | 
|Prime|prime|prime | 
|Prime|prime|primeos | 
|Prime|primenet|primenet | 
|Prime|primenet|primeos | 
|Prime|primeos|prime | 
|Prime|primeos|primeos | 
|Prime|primos_cs|prime | 
|Prime|primos_cs|primos | 
|Prime|system|prime | 
|Prime|system|system | 
|Prime|tele|tele | 
|Prime|test|test | 
|PrimeBase|Administrator| | 
|Prolink|admin|password | 
|Promise Technology, Inc.|administrator|password | 
|Promise|admin|admin | 
|Promise|engmode|hawk201 | 
|Prostar|none|4321 | 
|Protocraft|musi1921|Musi%1921 | 
|Proxicast||1234 | 
|Proxim|| | 
|Proxim||public | 
|Psionteklogix|admin|admin | 
|Psionteklogix|support|h179350 | 
|Pyramid Computer|admin|admin | 
|Pyramid Computer|admin|gnumpf | 
|Q-Tec|Admin| | 
|QDI||QDI | 
|QDI||lesarotl | 
|QDI||password | 
|QDI|<N/A>|QDI | 
|QDI|<N/A>|lesarotl | 
|QLogic|admin|password | 
|QLogic|images|images | 
|QualiTeam|master|master | 
|Quantex||teX1 | 
|Quantex||xljlbj | 
|Quantex|<N/A>|teX1 | 
|Quantex|<N/A>|xljlbj | 
|Quantum|| | 
|Quest Software|TOAD|TOAD | 
|Questra Corporation|guest|guest | 
|Questra Corporation|questra|questra | 
|Quintum Technologies Inc.|admin|admin | 
|RCA||admin | 
|RM||RM | 
|RM|<N/A>|RM | 
|RM|RMUser1|password | 
|RM|admin|rmnetlm | 
|RM|admin2|changeme | 
|RM|adminstrator|changeme | 
|RM|deskalt|password | 
|RM|deskman|changeme | 
|RM|desknorm|password | 
|RM|deskres|password | 
|RM|guest| | 
|RM|replicator|replicator | 
|RM|setup|changeme | 
|RM|teacher|password | 
|RM|temp1|password | 
|RM|topicalt|password | 
|RM|topicnorm|password | 
|RM|topicres|password | 
|RNN|admin|demo | 
|RObiGVqUbQt|wVQxyQec|eomjbOBLLwbZeiKV | 
|RSA|admin|admin1234 | 
|RSA|administrator|RSAAppliance | 
|RSA|master|themaster01 | 
|Radio Shack||744 | 
|Radio Shack|[MULTIPLE]|744 | 
|Radvision||MCUrv | 
|Radvision|admin| | 
|Radware|lp|lp | 
|Radware|radware|radware | 
|Raidzone||raidzone | 
|Raidzone|<N/A>|raidzone | 
|Rainbow||PASSWORD | 
|Rainbow||rainbow | 
|Ramp Networks|wradmin|trancell | 
|RapidStream|rsadmin| | 
|Raritan Inc.|admin|raritan | 
|Raritan Inc.|epiq_api|raritan | 
|Raritan Inc.|web_api|sl33p30F00dumass! | 
|Raritan|admin|raritan | 
|RayTalk|root|root | 
|Red Hat, Inc||AMIAMI | 
|Red Hat, Inc||AMIDECOD | 
|Red Hat, Inc|admin|admin | 
|Red Hat, Inc|piranha|piranha | 
|Red Hat, Inc|piranha|q | 
|RedHat|piranha|piranha | 
|RedHat|piranha|q | 
|Redcreek Communications||1234 | 
|Redcreek Communications||private | 
|Remedy|ARAdmin|AR#Admin# | 
|Remedy|Demo| | 
|Research||Col2ogro2 | 
|Research|<N/A>|Col2ogro2 | 
|Research Machines|manager|changeme | 
|Resumix|root|resumix | 
|Ricoh||password | 
|Ricoh||sysadm | 
|Ricoh|<N/A>|password | 
|Ricoh|<N/A>|sysadm | 
|Ricoh|admin| | 
|Ricoh|admin|no password | 
|Ricoh|admin|password | 
|Ricoh|sysadm|sysadm | 
|Ricoh|sysadmin|password | 
|Riverbed|Admin|password | 
|Rizen|Admin|123qwe | 
|RoamAbout|admin|password | 
|Rodopi|Rodopi|Rodopi | 
|RuggedCom|Admin|admin | 
|SAF Tehnika|administrator|d1scovery | 
|SAF Tehnika|integrator|p1nacate | 
|SAF Tehnika|monitor|monitor | 
|SAF Tehnika|operator|col1ma | 
|SAGEM|admin|epicrouter | 
|SAP|Administrator|manage | 
|SAP|DDIC|19920706 | 
|SAP|Developer|isdev | 
|SAP|EARLYWATCH|SUPPORT | 
|SAP|Replicator|iscopy | 
|SAP|SAP*|06071992 | 
|SAP|SAP*|7061992 | 
|SAP|SAP*|PASS | 
|SAP|SAPCPIC|ADMIN | 
|SAP|SAPCPIC|admin | 
|SAP|SAPR3|SAP | 
|SAP|TMSADM| | 
|SAP|admin|axis2 | 
|SAP client EARLYWATCH|admin|Support | 
|SAP|ctb_admin|sap123 | 
|SAP|itsadmin|init | 
|SAP|xmi_demo|sap123 | 
|SMA America||sma | 
|SMC||0000 | 
|SMC|| | 
|SMC||smcadmin | 
|SMC|<N/A>|smcadmin | 
|SMC|Admin|Barricade | 
|SMC|Administrator|smcadmin | 
|SMC|admin| | 
|SMC|admin|admin | 
|SMC|admin|barricade | 
|SMC|admin|smcadmin | 
|SMC|cusadmin|highspeed | 
|SMC|default|WLAN_AP | 
|SMC|mso|w0rkplac3rul3s | 
|SMC|none|none | 
|SMC|smc|smcadmin | 
|SOPHIA (Schweiz)|admin|Protector | 
|SOPHIA (Schweiz)|root|root | 
|SSA|SSA|SSA | 
|SUN|root|sun123 | 
|SWEEX|sweex|mysweex | 
|Saba|admin|admin | 
|Safecom|admin|epicrouter | 
|Sagem|Menara|Menara | 
|Sagem|admin|admin | 
|Sagem|root|1234 | 
|Samba|Any|Any | 
|Sambar Technologies|admin| | 
|Sambar Technologies|anonymous| | 
|Sambar Technologies|billy-bob| | 
|Sambar Technologies|ftp| | 
|Sambar Technologies|guest|guest | 
|Samsung||s!a@m#n$p%c | 
|Samsung|<N/A>| | 
|Samsung|admin|password | 
|Samsung|public|public | 
|Samuel Abels|user|password | 
|Schneider Electric||admin | 
|Schneider Electric|USER|USER | 
|Schneider Electric|ntpupdate|ntpupdate | 
|Scientific Atlanta|admin|w2402 | 
|Seagate|admin|admin | 
|Seagull Scientific|ADMIN|admin | 
|Seagull Scientific|USER|USER | 
|Seclore|root|changeonfirstlogin | 
|Seclore|sa|changeonfirstlogin | 
|Secure Computing|admin| | 
|Securicor3NET|manager|friend | 
|Semaphore|DESQUETOP| | 
|Semaphore|DS| | 
|Semaphore|DSA| | 
|Semaphore|PHANTOM| | 
|Sempre|admin|admin | 
|Senao|admin| | 
|Sercom|admin|admin | 
|Server Technology|ADMN|admn | 
|Server Technology|GEN1|gen1 | 
|Server Technology|GEN2|gen2 | 
|Seyeon Technology Co., Ltd|root|root | 
|Sharp|<N/A>|sysadm | 
|Sharp|Administrator|admin | 
|Sharp|admin|Sharp | 
|Sharp|admin|admin | 
|Sharp|none|sysadm | 
|Shiva|admin|hello | 
|Shiva|guest| | 
|Shiva|hello|hello | 
|Shiva|root| | 
|ShoreTel|Admin|admin1 | 
|Shoretel|admin|changeme | 
|Shuttle||Spacve | 
|Shuttle|<N/A>|Spacve | 
|Siemens|31994|31994 | 
|NevisIDM|bootstrap|generated | 
|Siemens||0 | 
|Siemens||123456 | 
|Siemens||admin | 
|Siemens|<N/A>|123456 | 
|Siemens|<N/A>| | 
|Siemens|<N/A>|SKY_FOX | 
|Siemens|<N/A>|admin | 
|Siemens|<N/A>|gubed | 
|Siemens Corp|18140815|18140815 | 
|Siemens Corp|31994|31994 | 
|Siemens Corp||SKY_FOX | 
|Siemens Corp||uboot | 
|Siemens Corp|WinCCAdmin|2WSXcde | 
|Siemens Corp|WinCCConnect|2WSXcder | 
|Siemens Corp|admin| | 
|Siemens Corp|admin|pwp | 
|Siemens Corp|eng|engineer | 
|Siemens Corp|op|op | 
|Siemens Corp|op|operator | 
|Siemens Corp|poll|poll | 
|Siemens Corp|poll|tech | 
|Siemens Corp|su|super | 
|Siemens Corp|sysadmin|sysadmin | 
|Siemens Corp|system|field | 
|Siemens Corp|system|system | 
|Siemens Corp|tech|tech | 
|Siemens|admin| | 
|Siemens|admin|<N/A> | 
|Siemens|admin|admin | 
|Siemens|admin|hagpolm1 | 
|Siemens|admin|pwp | 
|Siemens|basisk|basisk | 
|Siemens|eng|engineer | 
|Siemens|op|op | 
|Siemens|op|operator | 
|Siemens|poll|tech | 
|Siemens|su|super | 
|Siemens|superuser|admin | 
|Siemens|sysadmin|sysadmin | 
|Siemens|tech|field | 
|Siemens|tech|tech | 
|Sierra Wireless|user|12345 | 
|Sigma|admin|admin | 
|Signamax|admin|admin | 
|Siips|Administrator|ganteng | 
|Silex Technology|root| | 
|Silicon Graphics|4Dgifts|4Dgifts | 
|Silicon Graphics|4Dgifts| | 
|Silicon Graphics|6.x| | 
|Silicon Graphics|Ezsetup| | 
|Silicon Graphics|OutOfBox| | 
|Silicon Graphics|demos| | 
|Silicon Graphics|field|field | 
|Silicon Graphics|guest| | 
|Silicon Graphics|lp| | 
|Silicon Graphics|tour|tour | 
|Silicon Graphics|tutor| | 
|Silicon Graphics|tutor|tutor | 
|Silvercrest|admin|admin | 
|Site Interactive|admin|pass | 
|Sitecom||damin | 
|Sitecom||sitecom | 
|Sitecom|admin|admin | 
|Sitecom|admin|password | 
|Sitecore Corporation|Audrey|a | 
|Sitecore Corporation|Bill|b | 
|Sitecore Corporation|Denny|d | 
|Sitecore Corporation|Lonnie|l | 
|Sitecore Corporation|Minnie|m | 
|Sitecore Corporation|admin|b | 
|SmartSwitch|admin| | 
|Snap Appliance|admin|admin | 
|SnapGear|root|default | 
|Snapgear|root|admin | 
|Snom|Administrator|0000 | 
|Software AG|Administrator|manage | 
|Softwarehouse|manager|manager | 
|SolarWinds|LocalAdministrator|#l@$ak#.lk;0@P | 
|SolarWinds|whd|whd | 
|Solution 6|aaa|often blank | 
|Solwise|root|same as webui pwd | 
|Sonic-X|root|admin | 
|SonicWALL|admin|password | 
|Sonicwall|admin|password | 
|Sony Ericsson||0000 | 
|Sony|admin|admin | 
|Sorenson||admin | 
|Sourcefire|admin|password | 
|Sourcefire|root|password | 
|Sovereign Hill|Admin|shs | 
|Sparklan|admin|admin | 
|Spectra Logic|administrator| | 
|Spectra Logic|operator| | 
|SpeedStream||admin | 
|SpeedStream|<N/A>|adminttd | 
|SpeedStream|Administrator|admin | 
|SpeedStream|admin|admin | 
|SpeedXess||speedxess | 
|Sphairon|admin|passwort | 
|Spider Systems||hello | 
|Spike|enable| | 
|Splunk|admin|changeme | 
|Ssangyoung||2501 | 
|Stan Ozier|admin| | 
|Stratitec|root|ahetzip8 | 
|SuSE GmbH|root|root | 
|Sun Microsystems|root|changeme | 
|Sun|admin|admin | 
|Sun|root|changeme | 
|Sun|root|t00lk1t | 
|Sun|ssp|ssp | 
|Super Micro Computer, Inc.|ADMIN|ADMIN | 
|SuperMicro||ksdjfg934t | 
|SuperMicro|<N/A>|ksdjfg934t | 
|Supercook|admin|AlpheusDigital1010 | 
|Supercook|super|super | 
|Supermicro|ADMIN|admin | 
|Surecom|admin|admin | 
|Surecom|admin|surecom | 
|Sweex|| | 
|Sweex||admin | 
|Sweex||mysweex | 
|Sweex|admin|1234 | 
|Sweex|admin|epicrouter | 
|Sweex|none|blank | 
|Sweex|rdc123|rdc123 | 
|Sweex|sweex|mysweex | 
|Swissvoice|target|password | 
|Syabas Technology|ftpuser|1234 | 
|Syabas Technology|nmt|1234 | 
|Sybase|12.x| | 
|Sybase|DBA|SQL | 
|Sybase|jagadmin| | 
|Sybase|sa| | 
|Sybase|sa|sasasa | 
|Symantec||symantec | 
|Symantec|<N/A>|symantec | 
|Symantec|admin| | 
|Symantec|admin|symantec | 
|Symantec|root|brightmail | 
|Symbol|<N/A>|Symbol | 
|Symbol|Symbol|Symbol | 
|Symbol Technologies, Inc|admin|superuser | 
|Symbol|admin|symbol | 
|Symmetricom|guest|truetime | 
|Symmetricom|operator|mercury | 
|Synology Inc|admin| | 
|SysKonnect|default.password| | 
|SysMaster|admin|12345 | 
|System/32|install|secret | 
|T-Com||0 | 
|T-Com||123456 | 
|T-Com|<N/A>|0 | 
|T-Comfort|Administrator| | 
|T-com|veda|12871 | 
|TELTRONIC S.A.U.|admin|tetra | 
|TIBCO|admin|admin | 
|TIBCO|admin|changeit | 
|TMC||BIGO | 
|TMC|<N/A>|BIGO | 
|TOTOLINK|onlime_r|12345 | 
|TOTOLINK|root|12345 | 
|TP Link|admin|admin | 
|TVT System||enter | 
|TVT System|craft| | 
|TYPO3||joh316 | 
|TYPO3|admin|password | 
|Tandberg||GWrv | 
|Tandberg||TANDBERG | 
|Tandberg|<N/A>|10023 | 
|Tandberg|Admin| | 
|Tandberg|admin| | 
|Tandberg|admin|TANDBERG | 
|Tandberg|root|TANDBERG | 
|Tandem|super.super| | 
|Tandem|super.super|master | 
|Tasman|Tasman|Tasmannet | 
|Team Xodus|xbox|xbox | 
|Tegile|admin|tegile | 
|Teklogix|Administrator| | 
|Telappliant|admin|1234 | 
|Telco Systems|telco|telco | 
|Telebit|setup|setup | 
|Telebit|snmp|nopasswd | 
|Teledat|admin|1234 | 
|Telelec|eagle|eagle | 
|Teletronics|admin|1234 | 
|Telewell|admin|admin | 
|Telewell|admin|password | 
|Telindus|<N/A>| | 
|Telindus|admin|admin | 
|Tellabs|root|admin_1 | 
|Tellabs|tellabs|tellabs#1 | 
|Telus|(created)|telus00 | 
|Telus|(created)|telus99 | 
|Terayon|| | 
|Terayon|admin|password | 
|TexBox||123 | 
|TextPortal|god1|12345 | 
|TextPortal|god2|12345 | 
|Thecus Tech|admin|admin | 
|Thomson||admin | 
|Thomson|<N/A>|admin | 
|Thomson|admin|admin | 
|Thomson|admin|password | 
|Tiara Networks|<N/A>|tiara | 
|Tiara|tiara|tiaranet | 
|Tim Schaab|theman|changeit | 
|TimeTools|admin|admin | 
|Tiny||Tiny | 
|Tinys||tiny | 
|Tinys|<N/A>|Tiny | 
|TopLayer|siteadmin|toplayer | 
|Topcom|admin|admin | 
|Toshiba||24Banc81 | 
|Toshiba||Toshiba | 
|Toshiba||toshy99 | 
|Toshiba|<N/A>|24Banc81 | 
|Toshiba|<N/A>| | 
|Toshiba|<N/A>|Toshiba | 
|Toshiba|<N/A>|toshy99 | 
|Toshiba|Admin|123456 | 
|Toshiba|admin|123456 | 
|Toshiba|super|superpass | 
|Trend Micro|admin|admin | 
|Trend Micro|admin|imsa7.0 | 
|Trend Micro|root|trendimsa1.0 | 
|TrendMicro|admin|imss7.0 | 
|TrendNET|admin|password | 
|Trintech|t3admin|Trintech | 
|Tripp Lite|root|TrippLite | 
|Triumph-Adler|admin|0 | 
|Troy|admin|extendnet | 
|Tsunami|managers|managers | 
|Tumbleweed|Admin|SECRET123 | 
|Typo3 Association|admin|password | 
|U.S. Robotics||12345 | 
|U.S. Robotics|<N/A>|admin | 
|U.S. Robotics|Any|12345 | 
|U.S. Robotics|admin| | 
|U.S. Robotics|admin|admin | 
|U.S. Robotics|none|amber | 
|U.S. Robotics|root|12345 | 
|U.S. Robotics|root|admin | 
|U.S. Robotics|support|support | 
|UNEX|<N/A>|password | 
|UNIX|adm| | 
|UNIX|adm|adm | 
|UNIX|admin|admin | 
|UNIX|administrator| | 
|UNIX|administrator|administrator | 
|UNIX|anon|anon | 
|UNIX|bbs| | 
|UNIX|bbs|bbs | 
|UNIX|bin|sys | 
|UNIX|checkfs|checkfs | 
|UNIX|checkfsys|checkfsys | 
|UNIX|checksys|checksys | 
|UNIX|daemon| | 
|UNIX|daemon|daemon | 
|UNIX|demo| | 
|UNIX|demo|demo | 
|UNIX|demos| | 
|UNIX|demos|demos | 
|UNIX|dni| | 
|UNIX|dni|dni | 
|UNIX|fal| | 
|UNIX|fal|fal | 
|UNIX|fax| | 
|UNIX|fax|fax | 
|UNIX|ftp| | 
|UNIX|ftp|ftp | 
|UNIX|games| | 
|UNIX|games|games | 
|UNIX|gopher|gopher | 
|UNIX|gropher| | 
|UNIX|guest| | 
|UNIX|guest|guest | 
|UNIX|guest|guestgue | 
|UNIX|halt| | 
|UNIX|halt|halt | 
|UNIX|informix|informix | 
|UNIX|install|install | 
|UNIX|lp| | 
|UNIX|lp|bin | 
|UNIX|lp|lineprin | 
|UNIX|lp|lp | 
|UNIX|lpadm|lpadm | 
|UNIX|lpadmin|lpadmin | 
|UNIX|lynx| | 
|UNIX|lynx|lynx | 
|UNIX|mail| | 
|UNIX|mail|mail | 
|UNIX|man| | 
|UNIX|man|man | 
|UNIX|me| | 
|UNIX|me|me | 
|UNIX|mountfs|mountfs | 
|UNIX|mountfsys|mountfsys | 
|UNIX|mountsys|mountsys | 
|UNIX|news| | 
|UNIX|news|news | 
|UNIX|nobody| | 
|UNIX|nobody|nobody | 
|UNIX|nuucp| | 
|UNIX|operator| | 
|UNIX|operator|operator | 
|UNIX|oracle| | 
|UNIX|postmaster| | 
|UNIX|postmaster|postmast | 
|UNIX|powerdown|powerdown | 
|UNIX|rje|rje | 
|UNIX|root| | 
|UNIX|root|hp | 
|UNIX|root|root | 
|UNIX|service|smile | 
|UNIX|setup| | 
|UNIX|setup|setup | 
|UNIX|shutdown| | 
|UNIX|shutdown|shutdown | 
|UNIX|sync| | 
|UNIX|sync|sync | 
|UNIX|sys|bin | 
|UNIX|sys|sys | 
|UNIX|sys|system | 
|UNIX|sysadm|admin | 
|UNIX|sysadm|sysadm | 
|UNIX|sysadmin|sysadmin | 
|UNIX|sysbin|sysbin | 
|UNIX|system_admin| | 
|UNIX|system_admin|system_admin | 
|UNIX|trouble|trouble | 
|UNIX|umountfs|umountfs | 
|UNIX|umountfsys|umountfsys | 
|UNIX|umountsys|umountsys | 
|UNIX|unix|unix | 
|UNIX|user|user | 
|UNIX|uucp|uucp | 
|UNIX|uucpadm|uucpadm | 
|UNIX|web| | 
|UNIX|web|web | 
|UNIX|webmaster| | 
|UNIX|webmaster|webmaster | 
|UNIX|www| | 
|UNIX|www|www | 
|USRobotics|admin|admin | 
|UT Lexar|lexar| | 
|UTStarcom|dbase|dbase | 
|UTStarcom|field|field | 
|UTStarcom|guru|*3noguru | 
|UTStarcom|snmp|snmp | 
|Unex||password | 
|Unidesk|Administrator|Unidesk1 | 
|Unify||123456 | 
|Union|root|root | 
|Unisys|ADMINISTRATOR|ADMINISTRATOR | 
|Unisys|HTTP|HTTP | 
|Unisys|NAU|NAU | 
|United Technologies Corporation|admin|1234 | 
|Unknown||password | 
|Unknown|operator|operator | 
|Unknown|overseer|overseer | 
|Unknown|test|test | 
|UsRobotics|Any|12345 | 
|Utstar|admin|utstar | 
|VASCO|admin| | 
|VBrick Systems|admin|admin | 
|VPASP|admin|admin | 
|VPASP|vpasp|vpasp | 
|Various|root|admin | 
|Veramark|admin|password | 
|Verifone||166816 | 
|Verilink|| | 
|Veritas|admin|password | 
|Verity|admin|admin | 
|Verizon|admin|password | 
|Vextrec Technology||Vextrex | 
|Vextrec Technology|<N/A>|Vextrex | 
|VieNuke|admin|admin | 
|Vina Technologies|| | 
|Virtual Programming|admin|admin | 
|Virtual Programming|vpasp|vpasp | 
|Visa VAP|root|QNX | 
|Visual Networks|admin|visual | 
|Vobis||merlin | 
|Vobis|<N/A>|merlin | 
|VoiceGenie Technologies|pw|pw | 
|VoiceObjects Germany|voadmin|manager | 
|Vonage|user|user | 
|VxWorks|admin|admin | 
|VxWorks|guest|guest | 
|WAAV|admin|waav | 
|WLAN_3D|Administrator|admin | 
|WWWBoard|WebAdmin|WebBoard | 
|Wanadoo|admin|admin | 
|Wanco, Inc.||ABCD | 
|Wanco, Inc.||Guest | 
|Wanco, Inc.||NTCIP | 
|Wanco, Inc.||Public | 
|Wang|CSG|SESAME | 
|WatchGuard||wg | 
|WatchGuard|admin|admin | 
|WatchGuard|admin|readwrite | 
|WatchGuard|status|readonly | 
|Watchguard||wg | 
|Watchguard|admin| | 
|Watchguard|user|pass | 
|Web Wiz|Administrator|letmein | 
|Webmin|admin|hp.com | 
|Webramp|wradmin|trancell | 
|Weidm�eller|admin|detmond | 
|Westell|CSG|SESAME | 
|Westell|admin| | 
|Westell|admin|password | 
|Westell|admin|password1 | 
|Westell|admin|sysAdmin | 
|Wim Bervoets||Compleri | 
|Wim Bervoets|<N/A>|Compleri | 
|Wireless, Inc.|root|rootpass | 
|WorldClient|WebAdmin|Admin | 
|Wyse||Fireport | 
|Wyse|<N/A>|password | 
|Wyse|VNC|winterm | 
|Wyse|rapport|r@p8p0r+ | 
|Wyse|root| | 
|Wyse|root|wyse | 
|X-Micro|1502|1502 | 
|X-Micro|super|super | 
|XAMPP|newuser|wampp | 
|Xavi|<N/A>| | 
|Xavi|admin|admin | 
|Xerox|11111|x-admin | 
|Xerox||11111 | 
|Xerox|<N/A>|0 | 
|Xerox|Administrator|Fiery.1 | 
|Xerox|NSA|nsa | 
|Xerox|admin|1111 | 
|Xerox|admin|2222 | 
|Xerox|admin|22222 | 
|Xerox|admin| | 
|Xerox|admin|admin | 
|Xerox|admin|x-admin | 
|Xerox|savelogs|crash | 
|Xinit Systems Ltd.|openfiler|password | 
|Xylan|admin|switch | 
|Xylan|diag|switch | 
|Xyplex||access | 
|Xyplex||system | 
|Xyplex|<N/A>| | 
|Xyplex|<N/A>|access | 
|Xyplex|<N/A>|system | 
|Xyplex|setpriv|system | 
|Yakumo|admin|admin | 
|Yokogawa|<N/A>|727 | 
|Yokogawa|admin|!admin | 
|Yuxin|User|1234 | 
|Yuxin|User|19750407 | 
|ZEOS||zeosx | 
|ZEOS|<N/A>|zeosx | 
|ZTE|ADSL|expert03 | 
|Zcom|root|admin | 
|Zcomax|admin|password | 
|Zebra Technologies|admin|1234 | 
|Zebra|admin|1234 | 
|Zenith||3098z | 
|Zenith||Zenith | 
|Zenith|<N/A>|3098z | 
|Zenith|<N/A>|Zenith | 
|Zeus|admin| | 
|Zoom|admin|zoomadsl | 
|ZyWALL Series|<N/A>|admin | 
|Zyxel|1234|1234 | 
|Zyxel|192.168.1.1 60020|@dsl_xilno | 
|Zyxel||1234 | 
|Zyxel|<N/A>|1234 | 
|Zyxel|<N/A>| | 
|Zyxel|<N/A>|admin | 
|Zyxel|Admin|atc456 | 
|Zyxel|admin|0000 | 
|Zyxel|admin|1234 | 
|Zyxel|admin| | 
|Zyxel|admin|admin | 
|Zyxel|root|1234 | 
|Zyxel|webadmin|1234 | 
|accton t-online||0 | 
|acer|acer|acer | 
|actiontec|admin|admin | 
|adtran|<N/A>| | 
|adtran|<N/A>|Password | 
|adtran|<N/A>|adtran | 
|allied|| | 
|ast|<N/A>| | 
|backtrack|root|toor | 
|boson|<N/A>| | 
|canyon|Administrator|admin | 
|crt|egcr|ergc | 
|cuproplus|<N/A>| | 
|cyberguard|cgadmin|cgadmin | 
|darkman|ioFTPD|ioFTPD | 
|decnet|operator|admin | 
|digicom|Admin| | 
|drupal.org|admin|admin | 
|eMachines|emaq|4133 | 
|eQ-3|root|MuZhlo9n%8!G | 
|eSeSIX Computer GmbH|root|jstwo | 
|eZ Systems|admin|publish | 
|enCAD|<N/A>| | 
|ericsson||help | 
|ericsson|<N/A>| | 
|fon|admin|admin | 
|giga|Administrator|admin | 
|glFtpD|glftpd|glftpd | 
|glftpd|glftpd|glftpd | 
|greatspeed|netadmin|nimdaten | 
|haier|ucenik23|ucenik | 
|iDirect|admin|P@55w0rd! | 
|iDirect|root|iDirect | 
|iNTERFACEWARE Inc.|admn|password | 
|iPSTAR|admin|operator | 
|iblitzz|admin|admin | 
|inchon|admin|admin | 
|infacta|Administrator| | 
|intel|| | 
|intel|admin| | 
|intel|khan|kahn | 
|intel|root|admin | 
|intex|<N/A>| | 
|ion|<N/A>|admin | 
|ion|Administrator|admin | 
|iso sistemi|<N/A>| | 
|kaptest|admin| | 
|latis network|<N/A>| | 
|longshine|admin|0 | 
|m0n0wall|admin|mono | 
|maxdata|<N/A>| | 
|medion|<N/A>|medion | 
|metro|client|client | 
|microRouter|<N/A>|letmein | 
|mklencke|root|blablabla | 
|motorola|<N/A>| | 
|mro software|SYSADM|sysadm | 
|nCircle|root|ciwuxe | 
|olitec (Trendchip)|admin|admin | 
|olitec|admin|adslolitec | 
|oodie.com|admin|admin | 
|ovislink|root| | 
|penril datability|<N/A>|system | 
|pfSense|admin|pfsense | 
|phoenix|<N/A>|admin | 
|phpLiteAdmin||admin | 
|phpMyAdmin|root| | 
|phpTest|admin|1234 | 
|phpTest|guest|guest | 
|planet|admin|admin | 
|ptcl|admin|admin | 
|rPath|admin|password | 
|redline|admin|admin | 
|reg.pnu.ac.ir|880175445|11223344 | 
|remote-exploit|root|toor | 
|rm|administrator|password/changeme or secret | 
|schneider|USER|USER | 
|securstar|admin|rainbow | 
|seninleyimben|admin|admin | 
|sharp|<N/A>| | 
|sitara|root| | 
|smartBridges|admin|public | 
|sprint|self|system | 
|stratacom|stratacom|stratauser | 
|stuccoboy|stuccoboy|100198 | 
|technology|root| | 
|telecom|operator| | 
|tert|james|james | 
|topsec|superman|talent | 
|vertex|root|vertex25 | 
|warraCorp|pepino|pepino | 
|weblogic|system|weblogic | 
|winwork|operator| | 
|wline|admin|1234 | 
|xavi|admin|admin | 
|xd|xd|xd | 
|xerox|<N/A>|admin | 
|xerox|admin|1111 | 
|zenitel|admin|alphaadmin | 
|zenitel|ADMIN|alphacom | 
|zenitel||1851 | 
|zenitel||1234 | 
|zoom|admin|zoomadsl | 
| thomson (ssh) | admin | admin | 
| thomson (ssh) | admin | password | 
| windows (RDP) | Administrator | FELDTECH |
| windows (RDP) | secure | SecurityMaster08 |  
| windows (RDP) | admin | trinity |
| windows (RDP) | administrator | Wyse#123 |
| windows (RDP) | user | Wyse#123 |
| windows (RDP) | admin | admin |
| windows (RDP) | Administrator | Administrator |
| windows (RDP) | sonos | sonos |
| windows (RDP) | demo | m9ff.QW |
| windows (RDP) | wasadmin | wasadmin |
| windows (RDP) | maxadmin | maxadmin |
| windows (RDP) | mxintadm | mxintadm |
| windows (RDP) | maxreg | maxreg |
| windows (RDP) | root | |
| windows (RDP) | admin | admin |
| windows (RDP) | admin | 12345 |
| windows (RDP) | admin | 1234 |
| windows (RDP) | admin | 123456 |
| windows (RDP) | instrument | instrument |
| windows (RDP) | admin | |
| windows (RDP) | nmt | 1234 | 
| windows (RDP) | admin | password | 
| windows (RDP) | IEUser | Passw0rd! |
| windows (RDP) | openhabian | openhabian |
| windows (RDP) | vagrant | vagrant |
| windows (RDP) | Administrator | vagrant |
| windows (RDP) | john | Password123! |
| 3com (ssh) | admin | admin | 
| topnet (web) | topadmin | topadmin | 
| orange livebox4  (web) | admin |  | 
| orange livebox4  (web) | admin | (blank) | 
| asus (ssh) | admin | admin | 
| asus (ssh) | admin | password | 
| asus (ssh) | root | root  | 
| asus (ssh) | Admin | Admin  | 
| billion (ssh) | admin | admin | 
| huawei (ssh) | admin | admin | 
| huawei (ssh) | admin |  | 
| huawei (ssh) | Admin | admin | 
| huawei (ssh) | user | user | 
| huawei (ssh) | vodafone | vodafone | 
| huawei (ssh) | user | HuaweiUser | 
| huawei (ssh) | telecomadmin | admintelecom | 
| huawei (ssh) | digicel | digicel | 
| juniper (ssh) | admin | abc123 | 
| juniper (ssh) | super | juniper123 | 
| juniper (ssh) | admin | <<< %s(un=\'%s\') = %u. | 
| Juniper (ssh) | admin | abc123 | 
| Juniper (ssh) | admin | netscreen | 
| Juniper (ssh) | admin | peribit | 
| Juniper (ssh) | netscreen | netscreen | 
| Juniper (ssh) | redline | redline | 
| Juniper (ssh) | serial# | serial# | 
| Konica Minolta (web)  |  | 0000 | 
| Konica Minolta (web)  |  | 1234 | 
| Konica Minolta (web)  |  |  | 
| Konica Minolta (web)  |  | MagiMFP | 
| Konica Minolta (web)  |  | sysAdmin | 
| Konica Minolta (web)  | <N/A> | 0 | 
| Konica Minolta (web)  | <N/A> | sysadm | 
| Konica Minolta (web)  | admin | administrator | 
| Kronos | SuperUser | kronites | 
| McAfee | admin | admin123 | 
| McAfee | scmadmin | scmchangeme | 
| McAfee | webshield | webshieldchangeme | 
| Mitel | <N/A> |  | 
| Mitel Networks | 1nstaller | 5X2000 | 
| Mitel Networks | installer | sx2000 | 
| Mitel Networks | maint1 | sx2000 | 
| Mitel Networks | maint2 | sx2000 | 
| Mitel Networks | s1stem | 5X2000 | 
| Mitel Networks | system | sx2000 | 
| Mitel | installer | 1000 | 
| Mitel | system | mnet | 
| Mitel | system | password | 
| RedHat (ssh) |  | AMIAMI | 
| RedHat (ssh) |  | AMIDECOD | 
| RedHat (ssh) | admin | admin | 
| RedHat (ssh) | piranha | piranha | 
| RedHat (ssh) | piranha | q | 
| SAP (web) | Administrator | manage | 
| SAP (web) | DDIC | 19920706 | 
| SAP (web) | Developer | isdev | 
| SAP (web) | EARLYWATCH | SUPPORT | 
| SAP (web) | Replicator | iscopy | 
| SAP (web) | SAP* | 06071992 | 
| SAP (web) | SAP* | 7061992 | 
| SAP (web) | SAP* | PASS | 
| SAP (web) | SAPCPIC | ADMIN | 
| SAP (web) | SAPCPIC | admin | 
| SAP (web) | SAPR3 | SAP | 
| SAP (web) | TMSADM |  | 
| SAP (web) | admin | axis2 | 
| SAP (web) client EARLYWATCH | admin | Support | 
| SAP (web) | ctb_admin | sap123 | 
| SAP (web) | itsadmin | init | 
| SAP (web) | xmi_demo | sap123 | 
| Symantec |    |  symantec |  
| Symantec |  <N/A> |  symantec |  
| Symantec |  admin |    |  
| Symantec |  admin |  symantec |  
| Symantec |  root |  brightmail |  
| Trend Micro |  admin |  admin |  
| Trend Micro |  admin |  imsa7.0 |  
| Trend Micro |  root |  trendimsa1.0 |  
| TrendMicro |  admin |  imss7.0 |  
| movistar (ssh) | admin | admin | 
| movistar (ssh) | 1234 | 1234 | 
| netsys (ssh) | admin | admin | 
| XAMPP (web) | newuser | wampp |
| Zebra |  admin |  1234 |  
| zoom | admin | zoomadsl |
| technicolor (ssh) | admin | admin | 
| ubiquiti (ssh) | admin | admin | 
| ubiquiti (ssh) | root | ubnt | 
| ubiquiti (ssh) | ubnt | ubnt | 
| acti (web) |  admin | 12345 |
| acti (web) |  admin | 123456 |
| acti (web) |  Admin | 12345 |
| acti (web) |  Admin | 123456 |
| avigilon (web) |  admin | admin   |
| avigilon (web) |  Administrator |  |
| basler (web) |  admin | admin |
| grandstream (web) |  admin | admin |
| siemens (web) |  admin | admin |
| vacron (web) |  admin | admin |
| american_dynamics (web) |  admin | admin |
| american_dynamics (web) |  admin | 9999 |
| avtech (web) |  admin | admin |
| brickcom (web) |  admin | admin |
| iqinvision (web) |  root | system |
| mobotix (web) |  admin | meinsm |
| samsung (web) |  admin | 1111111 |
| samsung (web) |  admin | 4321 |
| samsung (web) |  root | admin |
| speco (web) |  admin | 1234 |
| videoiq (web) |  supervisor | supervisor |
| arecont (web) |  admin |  |
| arecont (web) |   |  |
| canon (web) |  root | camera |
| geovision (web) |  admin | admin |
| honeywell (web) |  admin | 1234 |
| jvc (web) |  admin | jvc |
| sentry360 (web) |  admin | 1234 |
| stardot (web) |  admin | admin |
| db2 (db2) | ADONIS | BPMS | 
| db2 (db2) | db2inst1 | db2inst1 |
| db2 (db2) | db2inst1 | db2pass |
| db2 (db2) | db2inst1 | db2pw |
| db2 (db2) | db2inst1 | db2password |
| db2 (db2) | dasusr1 | dasusr1 |
| db2 (db2) | db2fenc1 | db2fenc1 |
| db2 (db2) | db2admin | db2admin |
| postgres (postgres) | dcmadmin | passw0rd |
| postgres (postgres) | postgres | amber |
| postgres (postgres) | postgres | postgres |
| postgres (postgres) | postgres | password |
| postgres (postgres) | postgres | admin |
| postgres (postgres) | admin | admin |
| postgres (postgres) | admin | password |
| postgres (postgres) | postgres | 123 |
| DELL IDARC (web) | root | calvin |
| Zyxel NWA/NAP/WAC wireless access point series (ftp) |  devicehaecived | 1234 |
| ftp (ftp) |  anonymous | None |
| ftp (ftp) |  ftp | ftp |
| ftp (ftp) |  guest | guest |
| SNMP (snmp) |  None | 0 |
| SNMP (snmp) |  None | 0392a0 |
| SNMP (snmp) |  None | 1234 |
| SNMP (snmp) |  None | 2read |
| SNMP (snmp) |  None | 4changes |
| SNMP (snmp) |  None | access |
| SNMP (snmp) |  None | adm |
| SNMP (snmp) |  None | admin |
| SNMP (snmp) |  None | Admin |
| SNMP (snmp) |  None | agent |
| SNMP (snmp) |  None | agent_steal |
| SNMP (snmp) |  None | all |
| SNMP (snmp) |  None | all |
| SNMP (snmp) |  None | private |
| SNMP (snmp) |  None | all |
| SNMP (snmp) |  None | ANYCOM |
| SNMP (snmp) |  None | apc |
| SNMP (snmp) |  None | bintec |
| SNMP (snmp) |  None | blue |
| SNMP (snmp) |  None | c |
| SNMP (snmp) |  None | C0de |
| SNMP (snmp) |  None | cable |
| SNMP (snmp) |  None | canon_admin |
| SNMP (snmp) |  None | cc |
| SNMP (snmp) |  None | cisco |
| SNMP (snmp) |  None | CISCO |
| SNMP (snmp) |  None | community |
| SNMP (snmp) |  None | core |
| SNMP (snmp) |  None | CR52401 |
| SNMP (snmp) |  None | debug |
| SNMP (snmp) |  None | default |
| SNMP (snmp) |  None | dilbert |
| SNMP (snmp) |  None | enable |
| SNMP (snmp) |  None | field |
| SNMP (snmp) |  None | field |
| SNMP (snmp) |  None | freekevin |
| SNMP (snmp) |  None | fubar |
| SNMP (snmp) |  None | guest |
| SNMP (snmp) |  None | hello |
| SNMP (snmp) |  None | hp_admin |
| SNMP (snmp) |  None | ibm |
| SNMP (snmp) |  None | IBM |
| SNMP (snmp) |  None | ilmi |
| SNMP (snmp) |  None | ILMI |
| SNMP (snmp) |  None | intermec |
| SNMP (snmp) |  None | Intermec |
| SNMP (snmp) |  None | internal |
| SNMP (snmp) |  None | l2 |
| SNMP (snmp) |  None | l3 |
| SNMP (snmp) |  None | manager |
| SNMP (snmp) |  None | mngt |
| SNMP (snmp) |  None | monitor |
| SNMP (snmp) |  None | netman |
| SNMP (snmp) |  None | network |
| SNMP (snmp) |  None | NoGaH$@! |
| SNMP (snmp) |  None | none |
| SNMP (snmp) |  None | openview |
| SNMP (snmp) |  None | OrigEquipMfr |
| SNMP (snmp) |  None | pass |
| SNMP (snmp) |  None | password |
| SNMP (snmp) |  None | pr1v4t3 |
| SNMP (snmp) |  None | Private |
| SNMP (snmp) |  None | PRIVATE |
| SNMP (snmp) |  None | proxy |
| SNMP (snmp) |  None | publ1c |
| SNMP (snmp) |  None | public |
| SNMP (snmp) |  None | Public |
| SNMP (snmp) |  None | PUBLIC |
| SNMP (snmp) |  None | read |
| SNMP (snmp) |  None | read |
| SNMP (snmp) |  None | readwrite |
| SNMP (snmp) |  None | read |
| SNMP (snmp) |  None | red |
| SNMP (snmp) |  None | regional |
| SNMP (snmp) |  None | rmon |
| SNMP (snmp) |  None | rmon_admin |
| SNMP (snmp) |  None | ro |
| SNMP (snmp) |  None | root |
| SNMP (snmp) |  None | router |
| SNMP (snmp) |  None | rw |
| SNMP (snmp) |  None | rwa |
| SNMP (snmp) |  None | s!a@m#n$p%c |
| SNMP (snmp) |  None | sanfran |
| SNMP (snmp) |  None | san |
| SNMP (snmp) |  None | scotty |
| SNMP (snmp) |  None | secret |
| SNMP (snmp) |  None | Secret |
| SNMP (snmp) |  None | SECRET |
| SNMP (snmp) |  None | security |
| SNMP (snmp) |  None | Security |
| SNMP (snmp) |  None | SECURITY |
| SNMP (snmp) |  None | seri |
| SNMP (snmp) |  None | snmp |
| SNMP (snmp) |  None | SNMP |
| SNMP (snmp) |  None | snmpd |
| SNMP (snmp) |  None | snmptrap |
| SNMP (snmp) |  None | SNMP_trap |
| SNMP (snmp) |  None | solaris |
| SNMP (snmp) |  None | sun |
| SNMP (snmp) |  None | SUN |
| SNMP (snmp) |  None | superuser |
| SNMP (snmp) |  None | switch |
| SNMP (snmp) |  None | Switch |
| SNMP (snmp) |  None | SWITCH |
| SNMP (snmp) |  None | system |
| SNMP (snmp) |  None | System |
| SNMP (snmp) |  None | SYSTEM |
| SNMP (snmp) |  None | tech |
| SNMP (snmp) |  None | test |
| SNMP (snmp) |  None | TEST |
| SNMP (snmp) |  None | test2 |
| SNMP (snmp) |  None | tiv0li |
| SNMP (snmp) |  None | tivoli |
| SNMP (snmp) |  None | trap |
| SNMP (snmp) |  None | world |
| SNMP (snmp) |  None | write |
| SNMP (snmp) |  None | xyzzy |
| SNMP (snmp) |  None | yellow |
| Cisco Guard (snmp) |  None | riverhead |
| EyesOfNetwork (snmp) |  None | EyesOfNetwork |
| publicprivate (snmp) |  None | public |
| publicprivate (snmp) |  None | private |
| APC SmartSlot (snmp) |  None | TENmanUFactOryPOWER |
| telnet (telnet) |  root | password |
| telnet (telnet) |  root | root |
| telnet (telnet) |  root | xc3511 |
| telnet (telnet) |  root | vizxv |
| telnet (telnet) |  root | admin |
| telnet (telnet) |  admin | admin |
| telnet (telnet) |  root | 888888 |
| telnet (telnet) |  root | xmhdipc |
| telnet (telnet) |  root | default |
| telnet (telnet) |  root | juantech |
| telnet (telnet) |  root | 123456 |
| telnet (telnet) |  root | 54321 |
| telnet (telnet) |  support | support |
| telnet (telnet) |  root | None |
| telnet (telnet) |  admin | password |
| telnet (telnet) |  root | 12345 |
| telnet (telnet) |  user | user |
| telnet (telnet) |  admin | None |
| telnet (telnet) |  root | pass |
| telnet (telnet) |  admin | admin1234 |
| telnet (telnet) |  root | 1111 |
| telnet (telnet) |  admin | smcadmin |
| telnet (telnet) |  admin | 1111 |
| telnet (telnet) |  root | 666666 |
| telnet (telnet) |  root | 1234 |
| telnet (telnet) |  root | klv123 |
| telnet (telnet) |  Administrator | admin |
| telnet (telnet) |  service | service |
| telnet (telnet) |  supervisor | supervisor |
| telnet (telnet) |  guest | guest |
| telnet (telnet) |  guest | 12345 |
| telnet (telnet) |  guest | 12345 |
| telnet (telnet) |  admin1 | password |
| telnet (telnet) |  administrator | 1234 |
| telnet (telnet) |  666666 | 666666 |
| telnet (telnet) |  888888 | 888888 |
| telnet (telnet) |  ubnt | ubnt |
| telnet (telnet) |  root | klv1234 |
| telnet (telnet) |  root | Zte521 |
| telnet (telnet) |  root | hi3518 |
| telnet (telnet) |  root | jvbzd |
| telnet (telnet) |  root | anko |
| telnet (telnet) |  root | zlxx. |
| telnet (telnet) |  root | 7ujMko0vizxv |
| telnet (telnet) |  root | 7ujMko0admin |
| telnet (telnet) |  root | system |
| telnet (telnet) |  root | ikwb |
| telnet (telnet) |  root | dreambox |
| telnet (telnet) |  root | user |
| telnet (telnet) |  root | realtek |
| telnet (telnet) |  root | 0 |
| telnet (telnet) |  admin | 1111111 |
| telnet (telnet) |  admin | 1234 |
| telnet (telnet) |  admin | 12345 |
| telnet (telnet) |  admin | 54321 |
| telnet (telnet) |  admin | 123456 |
| telnet (telnet) |  admin | 7ujMko0admin |
| telnet (telnet) |  admin | 1234 |
| telnet (telnet) |  admin | pass |
| telnet (telnet) |  admin | meinsm |
| telnet (telnet) |  tech | tech |
| telnet (telnet) |  mother | fucker |
| Duhua (telnet) |  root | 7ujMko0admin |
| Duhua (telnet) |  admin | 7ujMko0admin |
| Duhua (telnet) |  root | vizxv |
| Juniper ScreenOS/Netscreen (telnet) |  netscreen | <<< %s(un='%s') = %u |
| American Dynamics EDVR (telnet) |  admin | 9999 |
| ClearPass (general) |  admin | eTIPS123 |
| Grafana (general) |  admin | admin |
| Ubiquiti EdgeOS (web) |  ubnt | ubnt |
| CA APM Team Center (web) |  Admin |  |
| CA APM Team Center (web) |  Guest | Guest |
| CA NetQoS (web) |  nqadmin | nq |
| CA NetQoS (web) |  nquser | nq |
| AudioCodes Mediant 1000 (web) |  Admin | Admin |
| ActiveMQ (general) |  admin | admin |
| ActiveMQ (general) |   |  |
| Kanboard (web) |  admin | admin |
| IBM UrbanCode Deploy (web) |  admin | admin |
| IBM UrbanCode Deploy (web) |  ucdpadmin | ucdpadmin |
| JBoss AS 6 Alt (web) |  admin | admin |
| Odoo (general) |  admin | admin |
| Odoo (general) |  demo | demo |
| Teleopti WFM (web) |  admin@company.com | admin |
| Endpoint Protector (general) |  root | epp2011 |
| NetBackup OpsCenter Analytics (web) |  admin | password |
| Dynatrace (web) |  admin | admin |
| Jenkins (web) |   |  |
| Zabbix (web) |  Admin | zabbix |
| DataStax OpsCenter 6.0.x (web) |  admin | admin |
| JBoss AS 6 (web) |  admin | admin |
| IBM Netezza (web) |  admin | password |
| Dell iDRAC (web) |  root | calvin |
| APC Network Management Card (web) |  apc | apc |
| APC Network Management Card (web) |  device | apc |
| APC Network Management Card (web) |  readonly | apc |
| WebSphere (web) |  system | manager |
| Apache Tomcat Host Manager (web) |  tomcat | tomcat |
| Apache Tomcat Host Manager (web) |  admin | admin |
| Apache Tomcat Host Manager (web) |  ovwebusr | OvW*busr1 |
| Apache Tomcat Host Manager (web) |  j2deployer | j2deployer |
| Apache Tomcat Host Manager (web) |  cxsdk | kdsxc |
| Apache Tomcat Host Manager (web) |  ADMIN | ADMIN |
| Apache Tomcat Host Manager (web) |  xampp | xampp |
| Apache Tomcat Host Manager (web) |  tomcat | s3cret |
| Apache Tomcat Host Manager (web) |  QCC | QLogic66 |
| Apache Tomcat Host Manager (web) |  admin | None |
| Apache Tomcat Host Manager (web) |  admin | tomcat |
| Apache Tomcat Host Manager (web) |  root | root |
| Apache Tomcat Host Manager (web) |  role1 | role1 |
| Apache Tomcat Host Manager (web) |  role | changethis |
| Apache Tomcat Host Manager (web) |  tomcat | changethis |
| Apache Tomcat Host Manager (web) |  admin | j5Brn9 |
| Apache Tomcat Host Manager (web) |  role1 | tomcat |
| Nuxeo Server (general) |  Administrator | Administrator |
| Oracle Glassfish (web) |  admin | admin |
| Oracle Glassfish (web) |  admin |  |
| Cisco Systems (general) |  cisco | cisco |
| IBM IMM (web) |  USERID | PASSW0RD |
| Avaya Contact Center (web) |  webadmin | webadmin |
| Video Web Server (webcam) |  admin | admin |
| SonarQube (web) |  admin | admin |
| Supermicro (web) |  ADMIN | ADMIN |
| Nexus Repository Manager (web) |  admin | admin123 |
| Cisco Collaboration Endpoint (general) |  cisco | admin |
| TeamCity 9 Guest (web) |   |  |
| Haivision Makito X Decoder (web) |  admin | manager |
| HP Server Automation (web) |  Administrator | admin |
| HP Server Automation (web) |  admin | opsware_admin |
| JasperReports (web) |  jasperadmin | jasperadmin |
| JasperReports (web) |  jasperadmin | bitnami |
| Nortel Integrated Call Director (web) |  admin | admin |
| Elasticsearch (web) |   |  |
| elasticsearch (web) | elastic  | changeme  |
| vnc (vnc) | | 123456 |
| vnc (vnc) | | FELDTECH_VNC |
| vnc (vnc) | | vnc_pcc |
| vnc (vnc) | | elux |
| vnc (vnc) | | Passwort |
| vnc (vnc) | | visam |
| vnc (vnc) | | password |
| vnc (vnc) | | Amx1234! |
| vnc (vnc) | | 1988 |
| vnc (vnc) | | admin |
| vnc (vnc) | | Vision2 |
| vnc (vnc) | | ADMIN |
| vnc (vnc) | | TOUCHLON |
| vnc (vnc) | | EltakoFVS |
| vnc (vnc) | | Wyse#123 |
| vnc (vnc) | | muster |
| vnc (vnc) | | passwd11 |
| vnc (vnc) | | qwasyx21 |
| vnc (vnc) | | Administrator |
| vnc (vnc) | | ripnas |
| vnc (vnc) | | eyevis |
| vnc (vnc) | | fidel123 |
| vnc (vnc) | | Admin#1 |
| vnc (vnc) | | default |
| vnc (vnc) | | sigmatek |
| vnc (vnc) | | hapero |
| vnc (vnc) | | 1234 |
| vnc (vnc) | | pass |
| vnc (vnc) | | raspberry |
| vnc (vnc) | | user |
| vnc (vnc) | | solarfocus |
| vnc (vnc) | | AVStumpfl |
| vnc (vnc) | | m9ff.QW |
| vnc (vnc) | | maryland-dstar |
| vnc (vnc) | | pass1 |
| vnc (vnc) | | pass2 |
| vnc (vnc) | | instrument |
| vnc (vnc) | | beijer |
| vnc (vnc) | | vnc |
| vnc (vnc) | | yesco |
| vnc (vnc) | | protech |
| vnc (vnc) | | Wyse |
| Aruba (web) | admin | admin |
| Avaya  |  | Craftr4 | 
| Avaya  | <N/A> |  | 
| Avaya  | <N/A> | admin | 
| Avaya  | Administrator | ggdaseuaimhrke | 
| Avaya  | Craft | crftpw | 
| Avaya  | admin | admin |
| Avaya  | admin | admin123 | 
| Avaya  | admin | barney | 
| Avaya  | admin | password |
| Avaya  | craft |  | 
| Avaya  | craft | crftpw | 
| Avaya  | dadmin | dadmin | 
| Avaya  | dadmin | dadmin01 | 
| Avaya  | diag | danger | 
| Avaya  | manuf | xxyyzz | 
| Avaya  | root | ROOT500 | 
| Avaya  | root | cms500 | 
| Avaya  | root | ggdaseuaimhrke | 
| Avaya  | root | root |
| Atlassian | Crowd | password |
| Atlassian | Demo | password |
| Atlassian | Username | password |
| Atlassian | crowd­-openid-­server | password |
| Adobe  | admin | admin | 
| Adobe  | anonymous | anonymous | 
| Adobe  | aparker@geometrixx.info | aparker | 
| Adobe  | author | author | 
| Adobe  | jdoe@geometrixx.info | jdoe | 
| Adobe  | replication-receiver | 
| Adobe  | vgnadmin | vgnadmin | 
| Makito Decoder (web) |  admin | %89%F0%01%8F%D0%01%80%F0%01%85%D0%01%83%F0%01%83%E0%01%84%F0%01 |
| Heatmiser Wifi Thermostat (iot) |  admin | admin |
| Proliphix Thermostat (iot) |  admin | admin |
| XEROX Phaser 6700 (printer) |  admin | 1111 |
| HP LaserJet 600 (printer) |   |  |
| Xerox WorkCentre 5020/DN (printer) |  11111 |  |
| HP LaserJet No Password Legacy (printer) |   |  |
| Ricoh MP (printer) |  supervisor |  |
| HP LaserJet No Password (printer) |   |  |
| Brother HL Series (printer) |  admin | access |
| TRENDnet Internet Camera (webcam) |  admin | admin |
| MayGion Camera (webcam) |  admin | admin |
| Polycom VVX 500 (phone) |  User | 123 |
| Polycom VVX 500 (phone) |  Admin | 456 |
| icatch (camera) |  admin | 123456 |
| icatch (camera) |  root | icatch99 |
| Speco Technologies IP Camera (camera) |  admin | 1234 |
| Cisco (ssh) |  cisco | cisco |
| Cisco (ssh) |  pix | cisco |
| Cisco Aironet (ssh) |  Cisco | Cisco |
| raspberry Pi (ssh) |  pi | raspberry |
| Apple Jailbroken Device (ssh) |  root | alpine |
| Apple Jailbroken Device (ssh) |  root | dottie |
| ssh (ssh) |  root | 7ujMko0admin |
| ssh (ssh) |  nasadmin | nasadmin |
| ssh (ssh) |  root | ascend |
| IBM Storwize V7000 Unified (ssh) |  admin | admin0001 |
| IBM Storwize V7000 Unified (ssh) |  superuser | passw0rd |
| IBM Storwize V7000 Unified (ssh) |  root | Passw0rd |
| modern.ie (ssh) |  IEUser | D@rj33l1ng |
| HipChat Server (ssh) |  admin | hipchat |
| AT&T Arris NVG589 & NVG599 (SharknAT&To) (ssh) |  remotessh | 5SaP9I26 |
| antsle (ssh) |  root | antsle |
| MySQL (ssh) |  root | root |
| metasploit (ssh) |  msf | msf |
| metasploit (ssh) |  msfdev | msfdev |
| postgres (postgres) |  postgres | postgres |
| Bosch RPS (mssql) |  sa | RPSsql12345 |
| medo.check (mssql) |  mcUser | medocheck123 |
| Lenel OnGuard (mssql) |  LENEL | MULTIMEDIA |
| UTC FCWnx (mssql) |  sa | SecurityMaster08 |
| Telestream Vantage (mssql) |  sa | vantage12! |
| Video Insight (mssql) |  sa | V4in$ight |
| Micro Focus Silk Central (mssql) |  sa | SilkCentral12!34 |
| MSSQL (mssql) |  sa |  |
| MSSQL (mssql) |  sa | sa |
| MSSQL (mssql) |  sa | Password123 |
| MSSQL (mssql) |  sa | password |
| MSSQL (mssql) |  ADONI | BPMS |
| MSSQL (mssql) |  sa | sqlserver |
| Schlage SMS (mssql) |  sa | SECAdmin1 |
| Schlage SMS (mssql) |  SMSAdmin | SECAdmin1 |
| Wonderware Historian (mssql) |  aaAdmin | pwAdmin |
| Wonderware Historian (mssql) |  aaPower | pwPower |
| Wonderware Historian (mssql) |  aaUser | pwUser |
| Wonderware Historian (mssql) |  aadbo | pwddbo |
| Wonderware Historian (mssql) |  wwUser | wwUser |
| Wonderware Historian (mssql) |  wwPower | wwPower |
| Wonderware Historian (mssql) |  wwAdmin | wwAdmin |
| Wonderware Historian (mssql) |  wwdbo | wwdbo |
| SplendidCRM (mssql) |  sa | splendidcrm2005 |
| MediaPortal (mssql) |  sa | M3d!aP0rtal |
| i2b2 Workbench (mssql) |  I2b2metadata | i2b2metadata |
| i2b2 Workbench (mssql) |  I2b2demodata | i2b2demodata |
| i2b2 Workbench (mssql) |  I2b2workdata | i2b2workdata |
| i2b2 Workbench (mssql) |  I2b2metadata2 | i2b2metadata2 |
| i2b2 Workbench (mssql) |  I2b2demodata2 | i2b2demodata2 |
| i2b2 Workbench (mssql) |  I2b2workdata2 | i2b2workdata2 |
| i2b2 Workbench (mssql) |  I2b2hive | i2b2hive |
| Emerson AMS (mssql) |  sa | 42Emerson42Eme |
| NetXMS (mssql) |  admin | netxms |
| Aris (mssql) |  ARIS9 | *ARIS!1dm9n# |
| easyWinArt (mssql) |  sa | $easyWinArt4 |
| SafeNet Sentinel EMS (mssql) |  sa | DBA!sa@EMSDB123 |
| IHS Kingdom (mssql) |  sa | $ei$micMicro |
| Napco Continental Access (mssql) |  sa | cic |
| Napco Continental Access (mssql) |  cic | cic |
| Napco Continental Access (mssql) |  sa | cic!23456789 |
| Napco Continental Access (mssql) |  cic | cic!23456789 |
| Napco Continental Access (mssql) |  sa | Cic!23456789 |
| Napco Continental Access (mssql) |  cic | Cic!23456789 |
| IBM WAS (mssql) |  wasadmin | wasadmin |
| OpenGTS (mssql) |  gts | opengts |
| WelchAllyn CardioPerfect (mssql) |  sa | Cardio.Perfect |
| TimeForce (mssql) |  sa | Dr8gedog |
| TimeForce (mssql) |  sa | dr8gedog |
| GeoNetwork (mssql) |  admin | gnos |
| Lasa AIMS (mssql) |  ADMIN | AIMS |
| Lasa AIMS (mssql) |  FB | AIMS |
| CCH (mssql) |  sa | PracticeUser1 |
| IBM Maximo (mssql) |  maxadmin | maxadmin |
| IBM Maximo (mssql) |  mxintadm | mxintadm |
| IBM Maximo (mssql) |  maxreg | maxreg |
| SKF @ptitude Analyst (mssql) |  sa | skf_admin1 |
| Redis (redis) |  None | None |
| Mongodb noauth (mongodb) |  None | None |
