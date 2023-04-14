# BAW Project

Bezpieczeństwo Aplikacji Webowych - Projekt OWASP Juice Shop

# Purpose of the project

The goal of the project is to identify and exploit vulnerabilities that are available in the OWASP Juice Shop. This should cover issues that overlap with the subject of the student course on web application security.

# Creators' note for OWASP Juice Shop

This package contains a modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications!

***WARNING:*** Do not upload it to your hosting provider’s public html folder or any Internet facing servers, as they will be compromised.

## Installation

required Linux dependencies:
 - libc6
 - lsof
 - libgcc-s1
 - nodejs
 - libstdc++6
 - npm

Use the following command to download OWASP Juice Shop if you're using Kali Linux [recommended]:

```bash
sudo apt install juice-shop
```

For other Linux distributions or those that don't have option to download package with command:

```bash
sudo wget https://github.com/juice-shop/juice-shop/releases/download/v14.0.1/juice-shop-14.0.1_node14_linux_x64.tgz
```
Unpack file:

```bash
tar zxvf juice-shop-14.0.1_node14_linux_x64.tgz
```
Install NodeJS and NPM (as per [link](https://www.golinuxcloud.com/install-owasp-juice-shop-kali-linux/)):

```bash
sudo wget https://nodejs.org/download/release/v14.1.0/node-v14.1.0-linux-x64.tar.xz

sudo tar -xvf node-v14.1.0-linux-x64.tar.xz
```

Install Node dependencies:

```bash
npm install
npm start
```

Check the version:
```bash
node --version
npm --version
```


## Usage

```console
root@kali:~# juice-shop -h
[*] Please wait for the Juice-shop service to start.
[*]
[*] You might need to refresh your browser once it opens.
[*]
[*]  Web UI: http://127.0.0.1:42000
```

```console
root@kali:~# juice-shop-stop -h
* juice-shop.service - juice-shop web application
     Loaded: loaded (/lib/systemd/system/juice-shop.service; disabled; preset: disabled)
     Active: inactive (dead)

Mar 08 10:28:00 kali npm[3906641]: info: Required file runtime.js is present (OK)
Mar 08 10:28:00 kali npm[3906641]: info: Required file vendor.js is present (OK)
Mar 08 10:28:00 kali npm[3906641]: (node:3906641) [DEP0152] DeprecationWarning: Custom PerformanceEntry accessors are deprecated. Please use the detail property.
Mar 08 10:28:00 kali npm[3906641]: (Use `node --trace-deprecation ...` to show where the warning was created)
Mar 08 10:28:00 kali npm[3906641]: info: Port 42000 is available (OK)
Mar 08 10:28:05 kali npm[3906641]: info: Server listening on port 42000
Mar 08 10:28:13 kali systemd[1]: Stopping juice-shop.service - juice-shop web application...
Mar 08 10:28:13 kali systemd[1]: juice-shop.service: Deactivated successfully.
Mar 08 10:28:13 kali systemd[1]: Stopped juice-shop.service - juice-shop web application.
Mar 08 10:28:13 kali systemd[1]: juice-shop.service: Consumed 4.444s CPU time.
```

After whole process OWASP Juice Shop GUI should be visible at certain port of localhost:

![alt text](https://raw.githubusercontent.com/juice-shop/juice-shop/master/screenshots/screenshot02.png "OWASP Juice Shop Main Page")

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/juice-shop/juice-shop/blob/master/LICENSE)
