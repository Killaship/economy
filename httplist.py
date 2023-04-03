TIMEOUT=10
httplist = []
for i in range(1000):
	httplist.append("Web Server Returned an Unknown Error")
httplist[100] = "Continue"
httplist[101] = "Switching Protocols"
httplist[102] = "Processing"
httplist[103] = "Early Hints"

httplist[200] = "OK"
httplist[201] = "Created"
httplist[202] = "Accepted"
httplist[203] = "Non-Authoritative Information"
httplist[204] = "No Content"
httplist[205] = "Reset Content"
httplist[206] = "Partial Content"
httplist[207] = "Multi-Status"
httplist[208] = "Already Reported"
httplist[226] = "IM used"

httplist[300] = "Multiple Choices"
httplist[301] = "Moved Permanently"
httplist[302] = "Found"
httplist[303] = "See Other"
httplist[304] = "Not Modified"
httplist[305] = "Use Proxy"
httplist[306] = "Switch Proxy"
httplist[307] = "Temporary Redirect"
httplist[308] = "Permanent Redirect"

httplist[400] = "Bad Request"
httplist[401] = "Unauthorized"
httplist[402] = "Payment Required"
httplist[403] = "Forbidden"
httplist[404] = "Not Found"
httplist[405] = "Method Not Allowed"
httplist[406] = "Not Acceptable"
httplist[407] = "Proxy Authentication Required"
httplist[408] = "Request Timeout"
httplist[409] = "Conflict"
httplist[410] = "Gone"
httplist[411] = "Length Required"
httplist[412] = "Precondition Failed"
httplist[413] = "Request Entity Too Large"
httplist[414] = "Request-URI Too Long"
httplist[415] = "Unsupported Media Type"
httplist[416] = "Requested Range Not Satisfiable"
httplist[417] = "Expectation Failed"
httplist[418] = "I'm a teapot"
httplist[421] = "Misdirected Reques"
httplist[422] = "Unprocessable Entity"
httplist[423] = "Locked"
httplist[424] = "Failed Dependency"
httplist[425] = "Too Early"
httplist[426] = "Upgrade Required"
httplist[428] = "Precondition Required"
httplist[429] = "Too Many Requests"
httplist[431] = "Request Header Fields Too Large"
httplist[451] = "Unavailable For Legal Reasons"

httplist[500] = "Internal Server Error"
httplist[501] = "Not Implemented"
httplist[502] = "Bad Gateway"
httplist[503] = "Service Unavailable"
httplist[504] = "Gateway Timeout"
httplist[505] = "HTTP Version Not Supported"
httplist[506] = "Variant Also Negotiates"
httplist[507] = "Insufficient Storage"
httplist[508] = "Loop Detected"
httplist[510] = "Not Extended"
httplist[511] = "Network Authentication Required"

# NON-STANDARD CODES

httplist[419] = "CSRF Token Missing or Expired"
httplist[420] = "Enhance Your Calm"
httplist[440] = "Login Time-out"
httplist[444] = "No Response"
httplist[449] = "Retry With"
httplist[450] = "Blocked by Windows Parental Controls"
httplist[460] = "Client closed the connection with AWS Elastic Load Balancer"
httplist[463] = "The load balancer received an X-Forwarded-For request header with more than 30 IP addresses"
httplist[494] = "Request header too large"
httplist[495] = "SSL Certificate Error"
httplist[496] = "SSL Certificate Required"
httplist[497] = "HTTP Request Sent to HTTPS Port"
httplist[498] = "Invalid Token (Esri)"
httplist[499] = "Client Closed Request"

httplist[520] = "Web Server Returned an Unknown Error"
httplist[521] = "Web Server Is Down"
httplist[522] = "Connection Timed out"
httplist[523] = "Origin Is Unreachable"
httplist[524] = "A Timeout Occurred"
httplist[525] = "SSL Handshake Failed"
httplist[526] = "Invalid SSL Certificate"
httplist[527] = "Railgun Error"
httplist[530] = "Origin DNS Error"
httplist[561] = "Unauthorized (AWS Elastic Load Balancer)"

httplist[609] = "Nice."
httplist[999] = "The connection timed out after 10 seconds. This means the server most likely is down, or it spun out into an infinite loop. (The bot killed urlcheck() after {sec} seconds!)".format(sec=TIMEOUT)
