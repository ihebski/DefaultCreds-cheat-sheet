
# Default Credentials Cheat Sheet

<p align="center">
  <img src="sc/default-credentials-cheat-sheet-6444.jpeg"/>
</p>

**One place for all the default credentials to assist pentesters/blue Teamers during engagements, featuring default login/password details for various products sourced from multiple references.**

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
| **count**	| 3711	| 3711	| 3711 |
| **unique** |	1398	| 1121 |	1680 |
| **top** |	Oracle| <blank> | <blank> |
| **freq** |	235 |	814 |	479 |

#### Sources

- [Changeme](https://github.com/ztgrace/changeme "Changeme project")
- [Routersploit]( https://github.com/threat9/routersploit "Routersploit project")
- [betterdefaultpasslist]( https://github.com/govolution/betterdefaultpasslist "betterdefaultpasslist")
- [Seclists]( https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials "Seclist project")
- [ics-default-passwords](https://github.com/arnaudsoullie/ics-default-passwords) (thanks to @noraj)
- Vendors documentations/blogs

## Installation & Usage

The Default Credentials Cheat Sheet tool is available on [pypi](https://pypi.org/project/defaultcreds-cheat-sheet/)

```bash
$ pip3 install defaultcreds-cheat-sheet
$ creds search tomcat
```

| Operating System   | Tested         |
|---------------------|-------------------|
| Linux(Kali,Ubuntu,Lubuntu)             | ✔️                |
| Windows(10,11)               | ✔️                |
| macOS               | ✔️               |

##### Manual Installation

```bash
$ git clone https://github.com/ihebski/DefaultCreds-cheat-sheet
$ pip3 install -r requirements.txt
$ cp creds /usr/bin/ && chmod +x /usr/bin/creds
$ creds search tomcat
```

## Creds script

### Usage Guide
```bash
# Search for product creds
➤ creds search tomcat
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+

# Update records
➤ creds update
Check for new updates...🔍
New updates are available 🚧
[+] Download database...

# Export Creds to files (could be used for brute force attacks)
➤ creds search tomcat export
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+

[+] Creds saved to /tmp/tomcat-usernames.txt , /tmp/tomcat-passwords.txt 📥
```

**Run creds through proxy**
```bash
# Search for product creds
➤ creds search tomcat --proxy=http://localhost:8080

# update records
➤ creds update --proxy=http://localhost:8080

# Search for Tomcat creds and export results to /tmp/tomcat-usernames.txt , /tmp/tomcat-passwords.txt
➤ creds search tomcat --proxy=http://localhost:8080 export
```

> **Proxy option** is only available from version 0.5.2
  
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


## 🌐 Web Resources & Aesthetic Symbols Index
- [SYM 1D405](https://scholarly-rune-symbols-33.pages.dev/symbol/sym-1d405/)
- [FREEFIRE NAMES](https://coquette-aesthetic-symbols-63.pages.dev/ru/freefire-names/)
- [SYM 26A3](https://angelic-coquette-text-10.pages.dev/symbol/sym-26a3/)
- [SYM 1D4A2](https://minimal-star-symbols-43.pages.dev/symbol/sym-1d4a2/)
- [SYM 268A](https://glitch-mecha-kaomoji-69.pages.dev/symbol/sym-268a/)
- [SYM 26F8](https://zen-unicode-symbols-89.pages.dev/symbol/sym-26f8/)
- [SYM 2644](https://synthwave-text-vault-95.pages.dev/symbol/sym-2644/)
- [SYM 1D473](https://pastel-moe-emoticons-55.pages.dev/symbol/sym-1d473/)
- [SYM 1D40F](https://anime-sparkle-text-81.pages.dev/symbol/sym-1d40f/)
- [SYM 1D464](https://arcane-symbol-vault-32.pages.dev/symbol/sym-1d464/)
- [SYM 26AB](https://baroque-unicode-decor-43.pages.dev/symbol/sym-26ab/)
- [SYM 1F63F](https://pink-bow-fonts-37.pages.dev/symbol/sym-1f63f/)
- [SYM 1F64A](https://kawaii-kaomoji-hub-31.pages.dev/symbol/sym-1f64a/)
- [DAGGER BLADE](https://kawaii-kaomoji-hub-31.pages.dev/symbol/dagger-blade/)
- [SYM 1D41C](https://clean-sparkle-text-75.pages.dev/symbol/sym-1d41c/)
- [SKULL AND CROSSBONES](https://neon-glitch-fonts-20.pages.dev/symbol/skull-and-crossbones/)
- [SYM 1F62F](https://clean-sparkle-text-75.pages.dev/symbol/sym-1f62f/)
- [SYM 26D7](https://mecha-gamer-fonts-53.pages.dev/symbol/sym-26d7/)
- [SYM 2741](https://minimal-star-symbols-32.pages.dev/symbol/sym-2741/)
- [KAOMOJI](https://kawaii-kaomoji-hub-31.pages.dev/kaomoji/)
- [SYM 2642](https://cute-face-emoticons-66.pages.dev/symbol/sym-2642/)
- [RIGHTWARDS PAIRED HARPOON](https://kawaii-kaomoji-hub-31.pages.dev/symbol/rightwards-paired-harpoon/)
- [CLOCKWISE OPEN CIRCLE ARROW](https://kawaii-kaomoji-hub-31.pages.dev/symbol/clockwise-open-circle-arrow/)
- [SYM 1D4A2](https://modern-bullet-symbols-45.pages.dev/symbol/sym-1d4a2/)
- [ARROWS LINES](https://pastel-moe-emoticons-55.pages.dev/es/arrows-lines/)
- [INSTAGRAM BIO](https://clean-sparkle-text-75.pages.dev/vi/instagram-bio/)
- [SYM 1D45D](https://soft-angel-unicode-43.pages.dev/symbol/sym-1d45d/)
- [NATURE FLOWERS](https://coquette-aesthetic-symbols-51.pages.dev/vi/nature-flowers/)
- [SYM 2659](https://angelic-soft-text-59.pages.dev/symbol/sym-2659/)
- [SYM 1D451](https://coquette-aesthetic-symbols-78.pages.dev/symbol/sym-1d451/)
- [SYM 1D47D](https://coquette-aesthetic-symbols-63.pages.dev/symbol/sym-1d47d/)
- [SYM 26CF](https://coquette-aesthetic-symbols-51.pages.dev/symbol/sym-26cf/)
- [STARRY LOVE AURA](https://coquette-aesthetic-symbols-84.pages.dev/symbol/starry-love-aura/)
- [SYM 1D43A](https://kawaii-kaomoji-hub-31.pages.dev/symbol/sym-1d43a/)
- [SYM 1F635 200D 1F4AB](https://zen-unicode-symbols-89.pages.dev/symbol/sym-1f635-200d-1f4ab/)
- [SYM 26AE](https://gothic-bio-fonts-98.pages.dev/symbol/sym-26ae/)
- [SYM 26D8](https://kawaii-kaomoji-hub-51.pages.dev/symbol/sym-26d8/)
- [SYM 2663](https://subtle-sparkle-text-86.pages.dev/symbol/sym-2663/)
- [ROBLOX NAMES](https://clean-sparkle-text-75.pages.dev/vi/roblox-names/)
- [SYM 26CB](https://fairy-lace-symbols-92.pages.dev/symbol/sym-26cb/)
- [SYM 1D436](https://anime-sparkle-text-45.pages.dev/symbol/sym-1d436/)
- [SYM 262E](https://anime-sparkle-text-81.pages.dev/symbol/sym-262e/)
- [SYM 2764 FE0F](https://neon-futuristic-symbols-62.pages.dev/symbol/sym-2764-fe0f/)
- [SYM 1D44F](https://zen-aesthetic-fonts-87.pages.dev/symbol/sym-1d44f/)
- [VIRGO ZODIAC MAIDEN](https://clean-sparkle-text-75.pages.dev/symbol/virgo-zodiac-maiden/)
- [SYM 263A FE0F](https://anime-sparkle-text-45.pages.dev/symbol/sym-263a-fe0f/)
- [NATURE FLOWERS](https://kawaii-kaomoji-hub-31.pages.dev/pt/nature-flowers/)
- [SYM 1F970](https://minimal-star-symbols-32.pages.dev/symbol/sym-1f970/)
- [SYM 1F62D](https://coquette-aesthetic-symbols-84.pages.dev/symbol/sym-1f62d/)
- [LEFT WING CLAN FLARE](https://soft-angel-unicode-43.pages.dev/symbol/left-wing-clan-flare/)
- [BEAMED EIGHTH NOTES](https://alchemist-symbol-hub-29.pages.dev/symbol/beamed-eighth-notes/)
- [SYM 1D487](https://pastel-moe-emoticons-55.pages.dev/symbol/sym-1d487/)
- [GEMINI ZODIAC TWINS](https://clean-sparkle-text-75.pages.dev/symbol/gemini-zodiac-twins/)
- [SYM 1D495](https://neon-glitch-fonts-20.pages.dev/symbol/sym-1d495/)
- [TIKTOK CAPTIONS](https://chibi-emoticon-lab-65.pages.dev/tiktok-captions/)
- [SYM 2666](https://coquette-aesthetic-symbols-78.pages.dev/symbol/sym-2666/)
- [SYM 1F635](https://soft-angel-unicode-43.pages.dev/symbol/sym-1f635/)
- [BORDERS DIVIDERS](https://coquette-aesthetic-symbols-51.pages.dev/vi/borders-dividers/)
- [BRACKETS](https://vintage-runes-text-63.pages.dev/pt/brackets/)
- [SYM 1F642 200D 2195 FE0F](https://moe-soft-emoticons-41.pages.dev/symbol/sym-1f642-200d-2195-fe0f/)
- [SAGITTARIUS ZODIAC ARCHER](https://coquette-aesthetic-symbols-84.pages.dev/symbol/sagittarius-zodiac-archer/)
- [KAOMOJI](https://vintage-script-symbols-65.pages.dev/ja/kaomoji/)
- [SYM 1F975](https://gothic-bio-fonts-69.pages.dev/symbol/sym-1f975/)
- [SYM 2675](https://coquette-aesthetic-symbols-63.pages.dev/symbol/sym-2675/)
- [SYM 267C](https://anime-sparkle-text-45.pages.dev/symbol/sym-267c/)
- [HEARTS](https://coquette-aesthetic-symbols-84.pages.dev/hearts/)
- [BLACK HEART](https://anime-sparkle-text-45.pages.dev/symbol/black-heart/)
- [NATURE FLOWERS](https://kawaii-kaomoji-hub-31.pages.dev/nature-flowers/)
- [SYM 1D46C](https://pastel-moe-emoticons-55.pages.dev/symbol/sym-1d46c/)
- [SYM 2764 FE0F 200D 1F525](https://coquette-aesthetic-symbols-62.pages.dev/symbol/sym-2764-fe0f-200d-1f525/)
- [EIGHT POINTED BLACK STAR](https://clean-sparkle-text-75.pages.dev/symbol/eight-pointed-black-star/)
- [SYM 1F622](https://zen-unicode-symbols-89.pages.dev/symbol/sym-1f622/)
- [FLUTTERING BUTTERFLY](https://sleek-line-unicode-29.pages.dev/symbol/fluttering-butterfly/)
- [SYM 2732](https://coquette-aesthetic-symbols-78.pages.dev/symbol/sym-2732/)
- [SYM 1D43E](https://pastel-moe-emoticons-55.pages.dev/symbol/sym-1d43e/)
- [PT](https://clean-sparkle-text-75.pages.dev/pt/)
- [SYM 1F924](https://coquette-aesthetic-symbols-51.pages.dev/symbol/sym-1f924/)
- [SYM 2647](https://synth-dystopia-text-20.pages.dev/symbol/sym-2647/)
- [SYM 2620 FE0F](https://coquette-aesthetic-symbols-62.pages.dev/symbol/sym-2620-fe0f/)
- [SYM 1D43E](https://matrix-terminal-fonts-30.pages.dev/symbol/sym-1d43e/)
- [CAPRICORN ZODIAC GOAT](https://coquette-aesthetic-symbols-63.pages.dev/symbol/capricorn-zodiac-goat/)
- [SYM 2639 FE0F](https://alchemist-symbol-hub-29.pages.dev/symbol/sym-2639-fe0f/)
- [LEFT MATHEMATICAL WHITE SQUARE BRACKET](https://chibi-bunny-symbols-82.pages.dev/symbol/left-mathematical-white-square-bracket/)
- [SYM 26CC](https://cyber-clan-tags-20.pages.dev/symbol/sym-26cc/)
- [SYM 1D40B](https://neon-glitch-fonts-20.pages.dev/symbol/sym-1d40b/)
- [SYM 2686](https://sleek-bio-fonts-25.pages.dev/symbol/sym-2686/)
- [STARRY LOVE AURA](https://aesthetic-spacing-fonts-10.pages.dev/symbol/starry-love-aura/)
- [SYM 1FAE4](https://minimal-star-symbols-32.pages.dev/symbol/sym-1fae4/)
- [SYM 1F60E](https://synth-dystopia-text-20.pages.dev/symbol/sym-1f60e/)
- [SYM 1F63B](https://neon-glitch-fonts-20.pages.dev/symbol/sym-1f63b/)
- [STARS](https://minimal-star-symbols-22.pages.dev/ja/stars/)
- [SYM 1F608](https://fairy-lace-symbols-92.pages.dev/symbol/sym-1f608/)
- [SYM 268F](https://anime-sparkle-text-45.pages.dev/symbol/sym-268f/)
- [LATIN CROSS FAITH](https://chibi-kaomoji-vault-58.pages.dev/symbol/latin-cross-faith/)
- [SYM 1F480](https://fairy-lace-symbols-92.pages.dev/symbol/sym-1f480/)
- [SYM 2613](https://aesthetic-spacing-fonts-10.pages.dev/symbol/sym-2613/)
- [SYM 1D432](https://clean-sparkle-text-75.pages.dev/symbol/sym-1d432/)
- [SYM 1F47D](https://alchemist-symbol-hub-29.pages.dev/symbol/sym-1f47d/)
- [ROBLOX NAMES](https://soft-angel-unicode-43.pages.dev/es/roblox-names/)
- [SYM 2673](https://ballet-core-symbols-11.pages.dev/symbol/sym-2673/)
- [SYM 26F8](https://fairy-lace-symbols-92.pages.dev/symbol/sym-26f8/)
- [SYM 1D453](https://synth-dystopia-text-20.pages.dev/symbol/sym-1d453/)
- [SIXTEEN POINTED STAR](https://clean-sparkle-text-75.pages.dev/symbol/sixteen-pointed-star/)
- [SYM 2617](https://chibi-emoticon-lab-65.pages.dev/symbol/sym-2617/)
- [SYM 1D40D](https://clean-sparkle-text-75.pages.dev/symbol/sym-1d40d/)
- [INSTAGRAM BIO](https://anime-sparkle-text-45.pages.dev/ru/instagram-bio/)
- [OPEN CENTRE STAR](https://chibi-emoticon-lab-65.pages.dev/symbol/open-centre-star/)
- [AQUARIUS ZODIAC WATER BEARER](https://minimal-star-symbols-32.pages.dev/symbol/aquarius-zodiac-water-bearer/)
- [SYM 273B](https://coquette-aesthetic-symbols-84.pages.dev/symbol/sym-273b/)
- [SYM 267E](https://sleek-arrow-symbols-42.pages.dev/symbol/sym-267e/)
- [SYM 1D43A](https://pastel-manga-symbols-57.pages.dev/symbol/sym-1d43a/)
- [SYM 1F637](https://vintage-script-symbols-65.pages.dev/symbol/sym-1f637/)
- [SYM 1D48A](https://anime-sparkle-text-73.pages.dev/symbol/sym-1d48a/)
- [GREEK PSI TRIDENT](https://pastel-moe-kaomoji-91.pages.dev/symbol/greek-psi-trident/)
- [SYM 1D462](https://clean-line-emojis-93.pages.dev/symbol/sym-1d462/)
- [SYM 1D45E](https://minimal-star-symbols-32.pages.dev/symbol/sym-1d45e/)
- [SYM 1F639](https://coquette-aesthetic-symbols-62.pages.dev/symbol/sym-1f639/)
- [SYM 1D42D](https://chibi-emoticon-lab-65.pages.dev/symbol/sym-1d42d/)
- [SYM 2662](https://neon-glitch-fonts-20.pages.dev/symbol/sym-2662/)
- [SPARKLE DOT FLARE](https://coquette-aesthetic-symbols-63.pages.dev/symbol/sparkle-dot-flare/)
- [SYM 260F](https://kawaii-kaomoji-hub-88.pages.dev/symbol/sym-260f/)
- [SYM 1F640](https://minimal-star-symbols-43.pages.dev/symbol/sym-1f640/)
- [BORDERS DIVIDERS](https://sleek-arrow-symbols-42.pages.dev/ja/borders-dividers/)
- [SYM 1D491](https://coquette-aesthetic-symbols-51.pages.dev/symbol/sym-1d491/)
- [SYM 26E2](https://coquette-aesthetic-symbols-63.pages.dev/symbol/sym-26e2/)
- [SYM 1D446](https://chibi-kaomoji-vault-58.pages.dev/symbol/sym-1d446/)
- [CUTE BUNNY RABBIT FACE](https://anime-sparkle-text-45.pages.dev/symbol/cute-bunny-rabbit-face/)
- [SYM 26D0](https://sleek-line-unicode-29.pages.dev/symbol/sym-26d0/)
- [VIRGO ZODIAC MAIDEN](https://minimal-star-symbols-32.pages.dev/symbol/virgo-zodiac-maiden/)
- [SYM 1F971](https://gothic-bio-fonts-69.pages.dev/symbol/sym-1f971/)
