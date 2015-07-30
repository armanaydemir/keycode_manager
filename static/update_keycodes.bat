echo OFF
set /p Customer=Enter Customer:
set /p ExpDate=Enter Exp Date:


c:\BTS\edge\btscmd.exe logon RENEW -keyfile:\\10.96.18.41\groups\keys\bts_private.pem -pass:bluetradesys -source:http://%Customer%/config/ -expiration:%ExpDate% > .\%Customer%-logon.conf

REM notepad .\%Customer%-logon.conf

plink.exe -i bts.ppk bts@%Customer% "hg add ./wwwroot/config/logon.conf"
plink.exe -i bts.ppk bts@%Customer% "hg commit -m 'new' ./wwwroot/config/logon.conf"
pscp -i bts.ppk .\%Customer%-logon.conf bts@%Customer%:./wwwroot/config/logon.conf
plink.exe -i bts.ppk bts@%Customer% "cd edge/current && ./btscmd configcheck"
PAUSE 
del .\%Customer%-logon.conf