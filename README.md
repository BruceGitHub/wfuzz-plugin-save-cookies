# wfuzz-plugin-save-cookies
plugin for wfuzz tools - save cookie to file of response header

# Setup
according to wfuzz documentation place this script at home folder under .wfuzz/scripts directory 

# Run 
call from cli like this 

```bash
wfuzz --script=save-response-cookies  -z list,index.php -z list,1-2  -d "fuckhtml=FUZ2Z" docker.hackthebox.eu:46177/FUZZ
```
# Note 
"WFUZZ" does not start custom script scripts if you do not use the FUZZ keyword in the URL a trick is to use two payloads with FUZ2Z

# Output like this

```bash
********************************************************
* Wfuzz 2.3 - The Web Fuzzer                           *
********************************************************

Target: http://www.host.com/FUZZ
Total requests: 2

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================

000002:  C=404     38 L	     137 W	   1317 Ch	  "2"
 |_  Cookie - cookier0
000001:  C=200   1171 L	    2799 W	  69502 Ch	  "1"
 |_  Cookie - cookie1
 |_  Cookie - cookie2 
 
Total time: 1.824699
Processed Requests: 2
Filtered Requests: 0
Requests/sec.: 1.096070
```

Under folder wfuzz will be created the folder save "saved-cookies" with file request_number_1, request_number_2 etc
