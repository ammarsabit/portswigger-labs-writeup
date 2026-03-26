# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-238-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--03--14-yellow) ![Level](https://img.shields.io/badge/Level-APPRENTICE-green) ![Vulnerability labs](https://img.shields.io/badge/Completed-88%25-purple)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

## Level progress
- **Apprentice**: 59 of 59
- **Practitioner**: 160 of 172
- **Expert**: 19 of 39

## Categories Covered
- **API Testing**: 4/5 lab
- **Information Disclosure**: 5/5 lab
- **Business logic vulnerabilities**: 6/11 lab
- **Authentication vulnerabilities**: 14/14 lab
- **Server-side template injection**: 6/7 lab
- **Path traversal**: 6/6 lab
- **File upload vulnerabilities**: 7/7 lab
- **Cross-site scripting**: 23/30 lab
- **SQL injection**: 18/18 lab
- **Race conditions**: 6/6 lab
- **Access control**: 13/13 lab
- **OS command injection**: 5/5 lab
- **Server-side request forgery (SSRF)**: 7/7 lab
- **JWT attacks**: 8/8 lab
- **Cross-site request forgery (CSRF)**: 11/12 lab
- **DOM-based vulnerabilities**: 7/7 lab
- **WebSockets**: 3/3 lab
- **GraphQL API vulnerabilities**: 5/5 lab
- **Insecure deserialization**: 7/10 lab
- **OAuth authentication**: 5/6 lab
- **Web cache deception**: 5/5 lab
- **Web cache poisoning**: 10/13 lab
- **Prototype pollution**: 10/10 lab
- **HTTP Host header attacks**: 6/7 lab
- **XXE injection**: 9/9 lab
- **Clickjacking**: 3/5 lab
- **NoSQL injection**: 4/4 lab
- **CORS**: 2/3 lab
- **Web LLM attacks**: 2/4 lab
- **Essential skills**: 2/2 lab
- **Request smuggling**: 19/22 lab

## Notes
- **Full Writeups**: Only for significant labs (e.g., chained exploits or scripted solutions). See `platforms/portswigger/` for details.
- **Tools Used**: Burp Suite

## How to Read
- **Columns**: 
  - `No`: Sequential lab number.
  - `Date`: When I solved it (YYYY-MM-DD).
  - `Topic`: Vulnerability category (e.g., API Testing, XSS).
  - `Lab Title`: Exact name from PortSwigger.
  - `Difficulty`: Apprentice, Practitioner, or Expert.
  - `Writeup Link`: Links to full writeup (if exists) or "N/A" for quick solves.

---

## Solved Labs

| No | Date       | Topic          | Lab Title                                   | Difficulty  | Writeup Link |
|----|------------|----------------|---------------------------------------------|-------------|--------------|
| 1  | 2025-09-26 | API Testing    | Exploiting an API endpoint using documentation | Apprentice | N/A |
| 2  | 2025-09-26 | API Testing    | Finding and exploiting an unused API endpoint | Practitioner | N/A |
| 3  | 2025-09-27 | API Testing    | Exploiting a mass assignment vulnerability | Practitioner | N/A |
| 4  | 2025-09-28 | Information Disclosure    | Information disclosure in error messages | Apprentice | N/A |
| 5  | 2025-09-28 | Business logic vulnerabilities | Excessive trust in client-side controls | Apprentice | N/A |
| 6  | 2025-09-30 | Business logic vulnerabilities | High-level logic vulnerability | Apprentice | N/A |
| 7  | 2025-09-30 | Authentication vulnerabilities | Username enumeration via different responses | Apprentice | N/A |
| 8  | 2025-09-30 | Authentication vulnerabilities | Username enumeration via subtly different responses | Practitioner | N/A |
| 9  | 2025-09-30 | Authentication vulnerabilities | 2FA simple bypass | Apprentice | N/A |
| 10 | 2025-09-30 | Authentication vulnerabilities | Password reset broken logic | Apprentice | N/A |
| 11 | 2025-09-30 | Authentication vulnerabilities | Password brute-force via password change | Practitioner | N/A |
| 12 | 2025-09-30 | Information disclosure | Authentication bypass via information disclosure | Apprentice | N/A |
| 13 | 2025-09-30 | Information disclosure | Information disclosure on debug page | Apprentice | N/A |
| 14 | 2025-09-30 | Information disclosure | Source code disclosure via backup files | Apprentice | N/A |
| 15 | 2025-09-30 | Information disclosure | Information disclosure in version control history | Apprentice | N/A |
| 16 | 2025-09-30 | Server-side template injection | Basic server-side template injection | Practitioner | [writeup](https://github.com/ammarsabit/portswigger-labs-writeup/blob/main/ssti/basic-server-side-template-injection.md) |
| 17 | 2025-09-30 | Server-side template injection | Basic server-side template injection (code context) | Practitioner | N/A |
| 18 | 2025-10-9 | Server-side template injection | Server-side template injection in an unknown language with a documented exploit | Practitioner | N/A |
| 19 | 2025-10-9 | Authentication vulnerabilities | Username enumeration via account lock | Practitioner | N/A |
| 20 | 2025-10-10 | Server-side template injection | Server-side template injection with information disclosure via user-supplied objects | Practitioner | N/A |
| 21 | 2025-10-14 | Path traversal | File path traversal, simple case | Apprentice | N/A |
| 22 | 2025-10-14 | Path traversal | File path traversal, traversal sequences blocked with absolute path bypass | Practitioner | N/A |
| 23 | 2025-10-14 | Path traversal | File path traversal, traversal sequences stripped non-recursively | Practitioner | N/A |
| 24 | 2025-10-16 | Path traversal | File path traversal, traversal sequences stripped with superfluous URL-decode | Practitioner | N/A |
| 25 | 2025-10-16 | Path traversal | File path traversal, validation of start of path | Practitioner | N/A |
| 26 | 2025-10-16 | Path traversal | File path traversal, validation of file extension with null byte bypass | Practitioner | N/A |
| 27 | 2025-10-17 | File upload vulnerabilities | Remote code execution via web shell upload | Apprentice | N/A |
| 28 | 2025-10-17 | File upload vulnerabilities | Web shell upload via Content-Type restriction bypass | Apprentice | N/A |
| 29 | 2025-10-19 | File upload vulnerabilities | Web shell upload via path traversal | Practitioner | N/A |
| 30 | 2025-10-20 | Cross-site scripting | Reflected XSS into HTML context with nothing encoded | Apprentice | N/A |
| 31 | 2025-10-20 | Cross-site scripting | Stored XSS into HTML context with nothing encoded | Apprentice | N/A |
| 32 | 2025-10-20 | SQL injection | SQL injection vulnerability allowing login bypass | Apprentice | N/A |
| 33 | 2025-10-20 | SQL injection | SQL injection vulnerability in WHERE clause allowing retrieval of hidden data | Apprentice | N/A |
| 34 | 2025-10-22 | File upload vulnerabilities | Web shell upload via extension blacklist bypass | Practitioner | N/A |
| 35 | 2025-10-22 | File upload vulnerabilities | Web shell upload via obfuscated file extension | Practitioner | N/A |
| 36 | 2025-10-24 | Race conditions | Limit overrun race conditions | Apprentice | N/A |
| 37 | 2025-10-24 | Race conditions | Bypassing rate limits via race conditions | Practitioner | N/A |
| 38 | 2025-10-25 | Access control | Unprotected admin functionality | Apprentice | N/A |
| 39 | 2025-10-25 | Access control | Unprotected admin functionality with unpredictable URL | Apprentice | N/A |
| 40 | 2025-10-25 | Access control | User role controlled by request parameter | Apprentice | N/A |
| 41 | 2025-10-25 | Access control | User ID controlled by request parameter  | Apprentice | N/A |
| 42 | 2025-10-25 | Access control | User ID controlled by request parameter, with unpredictable user IDs | Apprentice | N/A |
| 43 | 2025-10-25 | Access control | User ID controlled by request parameter with data leakage in redirect  | Apprentice | N/A |
| 44 | 2025-10-26 | Access control | User ID controlled by request parameter with password disclosure  | Apprentice | N/A |
| 45 | 2025-10-26 | Access control | Insecure direct object references  | Apprentice | N/A |
| 46 | 2025-10-26 | Access control | Referer-based access control   | Practitioner | N/A |
| 47 | 2025-10-26 | Access control | Multi-step process with no access control on one step | Practitioner | N/A |
| 48 | 2025-10-27 | OS command injection | Multi-step process with no access control on one step   | Practitioner | N/A |
| 49 | 2025-10-27 | OS command injection | Blind OS command injection with output redirection | Practitioner | N/A |
| 50 | 2025-10-27 | OS command injection | Blind OS command injection with time delays | Practitioner | N/A |
| 51 | 2025-10-28 | SQL injection | SQL injection UNION attack, determining the number of columns returned by the query | Practitioner | N/A |
| 52 | 2025-10-28 | SQL injection | SQL injection UNION attack, finding a column containing text | Practitioner | N/A |
| 53 | 2025-10-28 | SQL injection | SQL injection UNION attack, retrieving data from other tables | Practitioner | N/A |
| 54 | 2025-10-28 | SQL injection | SQL injection UNION attack, retrieving multiple values in a single column | Practitioner | N/A |
| 55 | 2025-10-28 | SQL injection | SQL injection attack, querying the database type and version on Oracle | Practitioner | N/A |
| 56 | 2025-10-29 | SQL injection | SQL injection attack, querying the database type and version on MySQL and Microsoft | Practitioner | N/A |
| 57 | 2025-10-29 | SQL injection | SQL injection attack, listing the database contents on non-Oracle databases | Practitioner | N/A |
| 58 | 2025-10-29 | SQL injection | SQL injection attack, listing the database contents on Oracle | Practitioner | N/A |
| 59 | 2025-10-29 | Server-side request forgery (SSRF) | Basic SSRF against the local server | Apprentice | N/A |
| 60 | 2025-10-29 | Server-side request forgery (SSRF) | Basic SSRF against another back-end system | Apprentice | N/A |
| 61 | 2025-10-29 | Server-side request forgery (SSRF) | Blind SSRF with out-of-band detection | Practitioner | N/A |
| 62 | 2025-10-31 | SQL injection | Blind SQL injection with conditional responses | Practitioner | N/A |
| 63 | 2025-10-31 | SQL injection | Blind SQL injection with conditional errors | Practitioner | N/A |
| 64 | 2025-11-3 | SQL injection | Blind SQL injection with time delays | Practitioner | N/A |
| 65 | 2025-11-3 | OS command injection | Blind OS command injection with out-of-band interaction | Practitioner | N/A |
| 66 | 2025-11-3 | OS command injection | Blind OS command injection with out-of-band data exfiltration | Practitioner | N/A |
| 67 | 2025-11-6 | Server-side request forgery (SSRF) | SSRF with blacklist-based input filter | Practitioner | N/A |
| 68 | 2025-11-8 | Cross-site scripting | Exploiting cross-site scripting to steal cookies | Practitioner | N/A |
| 69 | 2025-11-8 | Cross-site scripting | Reflected XSS into attribute with angle brackets HTML-encoded | Apprentice | N/A |
| 70 | 2025-11-10 | Cross-site scripting | DOM XSS in document.write sink using source location.search | Apprentice | N/A |
| 71 | 2025-11-10 | Server-side template injection | Server-side template injection using documentation | Practitioner | N/A |
| 72 | 2025-11-23 | JWT attacks | JWT authentication bypass via unverified signature | Apprentice | N/A |
| 73 | 2025-11-23 | JWT attacks | JWT authentication bypass via flawed signature verification | Apprentice | N/A |
| 74 | 2025-11-23 | JWT attacks | JWT authentication bypass via weak signing key | Practitioner | N/A |
| 75 | 2025-11-23 | JWT attacks | JWT authentication bypass via jwk header injection | Practitioner | N/A |
| 76 | 2025-11-24 | JWT attacks | JWT authentication bypass via jku header injection | Practitioner | N/A |
| 77 | 2025-11-24 | JWT attacks | JWT authentication bypass via kid header path traversal | Practitioner | N/A |
| 78 | 2025-11-24 | JWT attacks | JWT authentication bypass via algorithm confusion | Expert | N/A |
| 79 | 2025-11-24 | JWT attacks | JWT authentication bypass via algorithm confusion with no exposed key | Expert | N/A |
| 80 | 2025-11-25 | Cross-site scripting | DOM XSS in document.write sink using source location.search inside a select element | Practitioner | N/A |
| 81 | 2025-11-25 | Cross-site scripting | DOM XSS in innerHTML sink using source location.search | Apprentice | N/A |
| 82 | 2025-11-26 | Cross-site scripting | DOM XSS in jQuery anchor href attribute sink using location.search source | Apprentice | N/A |
| 83 | 2025-11-26 | Cross-site scripting | DOM XSS in jQuery selector sink using a hashchange event | Apprentice | N/A |
| 84 | 2025-11-27 | Cross-site scripting | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | Practitioner | N/A |
| 85 | 2025-11-27 | Cross-site scripting | Stored DOM XSS | Practitioner | N/A |
| 86 | 2025-11-28 | Authentication vulnerabilities | Offline password cracking | Practitioner | N/A |
| 87 | 2025-11-28 | Authentication vulnerabilities | Brute-forcing a stay-logged-in cookie | Practitioner | [writeup](https://github.com/ammarsabit/portswigger-labs-writeup/tree/main/Authentication_vulnerabilities) |
| 88 | 2025-12-2 | Cross-site request forgery | CSRF vulnerability with no defenses | Apprentice | N/A |
| 89 | 2025-12-2 | Cross-site request forgery | CSRF where token validation depends on token being present | Practitioner | N/A |
| 90 | 2025-12-2 | Cross-site request forgery | CSRF where token is not tied to user session | Practitioner | N/A |
| 91 | 2025-12-2 | Cross-site request forgery | CSRF where token validation depends on request method | Practitioner | N/A |
| 92 | 2025-12-2 | Cross-site request forgery | CSRF where Referer validation depends on header being present | Practitioner | N/A |
| 93 | 2025-12-2 | Cross-site request forgery | CSRF with broken Referer validation | Practitioner | N/A |
| 94 | 2025-12-3 | Cross-site request forgery | SameSite Lax bypass via method override | Practitioner | N/A |
| 95 | 2025-12-3 | Cross-site request forgery | SameSite Lax bypass via cookie refresh | Practitioner | N/A |
| 96 | 2025-12-3 | DOM-based vulnerabilities | DOM XSS using web messages | Practitioner | N/A |
| 97 | 2025-12-4 | DOM-based vulnerabilities | DOM XSS using web messages and a JavaScript URL | Practitioner | N/A |
| 98 | 2025-12-4 | DOM-based vulnerabilities | DOM XSS using web messages and JSON.parse | Practitioner | N/A |
| 99 | 2025-12-4 | DOM-based vulnerabilities | DOM-based open redirection | Practitioner | N/A |
| 100 | 2025-12-10 | File upload vulnerabilities | Remote code execution via polyglot web shell upload | Practitioner | N/A |
| 101 | 2025-12-10 | File upload vulnerabilities |  Web shell upload via race condition | Expert | N/A |
| 102 | 2025-12-11 | WebSockets |  Manipulating WebSocket messages to exploit vulnerabilities | Apprentice | N/A |
| 103 | 2025-12-11 | Cross-site scripting |  Reflected XSS into HTML context with most tags and attributes blocked | Practitioner | N/A |
| 104 | 2025-12-11 | Cross-site scripting |  Reflected XSS into HTML context with all tags blocked except custom ones | Practitioner | N/A |
| 105 | 2025-12-11 | Cross-site scripting |  Stored XSS into anchor href attribute with double quotes HTML-encoded | Apprentice | N/A |
| 106 | 2025-12-11 | Cross-site scripting |  Reflected XSS into a JavaScript string with angle brackets HTML encoded | Apprentice | N/A |
| 107 | 2025-12-13 | GraphQL API vulnerabilities |  Accessing private GraphQL posts | Apprentice | N/A |
| 108 | 2025-12-13 | GraphQL API vulnerabilities |  Accidental exposure of private GraphQL fields | Practitioner | N/A |
| 109 | 2025-12-13 | GraphQL API vulnerabilities |  Bypassing GraphQL brute force protections | Practitioner | N/A |
| 110 | 2025-12-16 | Insecure deserialization |  Modifying serialized objects | Apprentice | N/A |
| 111 | 2025-12-16 | Insecure deserialization |  Modifying serialized data types | Practitioner | N/A |
| 112 | 2025-12-16 | Insecure deserialization |  Using application functionality to exploit insecure deserialization | Practitioner | N/A |
| 113 | 2025-12-16 | GraphQL API vulnerabilities |  Finding a hidden GraphQL endpoint | Practitioner | N/A |
| 114 | 2025-12-16 | GraphQL API vulnerabilities |  Performing CSRF exploits over GraphQL | Practitioner | N/A |
| 115 | 2025-12-17 | OAuth authentication |  Authentication bypass via OAuth implicit flow | Apprentice | N/A |
| 116 | 2025-12-17 | Authentication vulnerabilities |  Broken brute-force protection, multiple credentials per request | Expert | N/A |
| 117 | 2025-12-17 | Authentication vulnerabilities |  Username enumeration via response timing | Practitioner | N/A |
| 118 | 2026-01-21 | Web cache deception |  Exploiting path mapping for web cache deception | Apprentice | N/A |
| 119 | 2026-01-21 | Web cache deception |  Exploiting path delimiters for web cache deception | Practitioner | N/A |
| 120 | 2026-01-21 | Web cache deception |  Exploiting origin server normalization for web cache deception | Practitioner | N/A |
| 121 | 2026-01-21 | Web cache deception |  Exploiting cache server normalization for web cache deception | Practitioner | N/A |
| 122 | 2026-01-22 | Web cache deception |  Exploiting exact-match cache rules for web cache deception | Expert | N/A |
| 123 | 2026-01-22 | Web cache poisoning |  Web cache poisoning with an unkeyed header | Practitioner | N/A |
| 124 | 2026-01-22 | Web cache poisoning |  Web cache poisoning with an unkeyed cookie | Practitioner | N/A |
| 125 | 2026-01-22 | Web cache poisoning |  Web cache poisoning with multiple headers | Practitioner | N/A |
| 126 | 2026-01-22 | Web cache poisoning |  Targeted web cache poisoning using an unknown header | Practitioner | N/A |
| 127 | 2026-01-22 | Web cache poisoning |  Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria | Expert | N/A |
| 128 | 2026-01-23 | Web cache poisoning |  Web cache poisoning via an unkeyed query string | Practitioner | N/A |
| 129 | 2026-01-23 | Web cache poisoning |  Web cache poisoning via an unkeyed query parameter | Practitioner | N/A |
| 130 | 2026-01-25 | Prototype pollution |  Privilege escalation via server-side prototype pollution | Practitioner | N/A |
| 131 | 2026-01-25 | Prototype pollution |  Detecting server-side prototype pollution without polluted property reflection | Practitioner | N/A |
| 132 | 2026-01-25 | Prototype pollution |  Bypassing flawed input filters for server-side prototype pollution | Practitioner | N/A |
| 133 | 2026-01-25 | Prototype pollution |  Remote code execution via server-side prototype pollution | Practitioner | N/A |
| 134 | 2026-01-25 | HTTP Host header attacks |  Basic password reset poisoning | Apprentice | N/A |
| 135 | 2026-01-25 | HTTP Host header attacks |  Password reset poisoning via middleware | Practitioner | N/A |
| 136 | 2026-01-25 | HTTP Host header attacks |  Host header authentication bypass | Apprentice | N/A |
| 137 | 2026-01-25 | HTTP Host header attacks |  Routing-based SSRF | Practitioner | N/A |
| 138 | 2026-01-25 | HTTP Host header attacks |  SSRF via flawed request parsing | Practitioner | N/A |
| 139 | 2026-01-26 | HTTP Host header attacks |  Host validation bypass via connection state attack | Practitioner | N/A |
| 140 | 2026-01-26 | HTTP Host header attacks |  Web cache poisoning via ambiguous requests | Practitioner | N/A |
| 141 | 2026-01-27 | Prototype pollution |  Exfiltrating sensitive data via server-side prototype pollution | Expert | N/A |
| 142 | 2026-01-27 | XXE injection |  Exploiting XXE using external entities to retrieve files | Apprentice | N/A |
| 143 | 2026-01-27 | XXE injection |  Exploiting XXE to perform SSRF attacks | Apprentice | N/A |
| 144 | 2026-01-27 | XXE injection |  Blind XXE with out-of-band interaction | Practitioner | N/A |
| 145 | 2026-01-27 | XXE injection |  Blind XXE with out-of-band interaction via XML parameter entities | Practitioner | N/A |
| 146 | 2026-01-27 | XXE injection |  Exploiting blind XXE to exfiltrate data using a malicious external DTD | Practitioner | N/A |
| 147 | 2026-01-27 | XXE injection |  Exploiting blind XXE to retrieve data via error messages | Practitioner | N/A |
| 148 | 2026-01-27 | XXE injection |  Exploiting XXE via image file upload | Practitioner | N/A |
| 149 | 2026-01-28 | Clickjacking |  Basic clickjacking with CSRF token protection | Apprentice | N/A |
| 150 | 2026-01-28 | Clickjacking |  Clickjacking with form input data prefilled from a URL parameter | Apprentice | N/A |
| 151 | 2026-01-28 | Clickjacking |  Clickjacking with a frame buster script | Apprentice | N/A |
| 152 | 2026-01-29 | NoSQL injection |  Detecting NoSQL injection | Apprentice | N/A |
| 153 | 2026-01-29 | NoSQL injection |  Exploiting NoSQL operator injection to bypass authentication | Apprentice | N/A |
| 154 | 2026-01-29 | NoSQL injection |  Exploiting NoSQL injection to extract data | Practitioner | N/A |
| 155 | 2026-01-29 | NoSQL injection |  Exploiting NoSQL operator injection to extract unknown fields | Practitioner | N/A |
| 156 | 2026-02-2 | CORS |  CORS vulnerability with basic origin reflection | Apprentice | N/A |
| 157 | 2026-02-2 | CORS |  CORS vulnerability with trusted null origin | Apprentice | N/A |
| 158 | 2026-02-2 | Web LLM attacks |  Exploiting LLM APIs with excessive agency | Apprentice | N/A |
| 159 | 2026-02-2 | Web LLM attacks |  Exploiting vulnerabilities in LLM APIs | Practitioner | N/A |
| 160 | 2026-02-2 | Essential skills |  Discovering vulnerabilities quickly with targeted scanning | Practitioner | N/A |
| 161 | 2026-02-2 | XXE injection |  Exploiting XInclude to retrieve files | Practitioner | N/A |
| 162 | 2026-02-2 | XXE injection |  Exploiting XXE to retrieve data by repurposing a local DTD | Expert | N/A |
| 163 | 2026-02-2 | Essential skills |  Scanning non-standard data structures | Practitioner | N/A |
| 164 | 2026-02-3 | Cross-site scripting |  Reflected XSS with some SVG markup allowed | Practitioner | N/A |
| 165 | 2026-02-3 | Cross-site scripting |  Exploiting XSS to bypass CSRF defenses | Practitioner | N/A |
| 166 | 2026-02-3 | Cross-site scripting |  Exploiting cross-site scripting to capture passwords | Practitioner | N/A |
| 167 | 2026-02-3 | Authentication vulnerabilities |  Broken brute-force protection, IP block | Practitioner | N/A |
| 168 | 2026-02-3 | Access control |  User role can be modified in user profile | Apprentice | N/A |
| 169 | 2026-02-3 | Access control |  User role can be modified in user profile | Practitioner | N/A |
| 170 | 2026-02-3 | Access control |  Method-based access control can be circumvented | Practitioner | N/A |
| 171 | 2026-02-4 | Business logic vulnerabilities |  Inconsistent security controls | Apprentice | N/A |
| 172 | 2026-02-4 | Business logic vulnerabilities |  Flawed enforcement of business rules | Apprentice | N/A |
| 173 | 2026-02-4 | SQL injection |  Visible error-based SQL injection | Practitioner | N/A |
| 174 | 2026-02-4 | SQL injection |  Blind SQL injection with time delays and information retrieval | Practitioner | N/A |
| 175 | 2026-02-4 | SQL injection |  Blind SQL injection with out-of-band interaction | Practitioner | N/A |
| 176 | 2026-02-4 | SQL injection |  Blind SQL injection with out-of-band data exfiltration | Practitioner | N/A |
| 177 | 2026-02-4 | SQL injection |  SQL injection with filter bypass via XML encoding | Practitioner | N/A |
| 178 | 2026-02-5 | API Testing |  Exploiting server-side parameter pollution in a query string | Practitioner | N/A |
| 179 | 2026-02-6 | Request smuggling |  HTTP request smuggling, confirming a CL.TE vulnerability via differential responses | Practitioner | N/A |
| 180 | 2026-02-6 | Request smuggling |  HTTP request smuggling, confirming a TE.CL vulnerability via differential responses | Practitioner | N/A |
| 181 | 2026-02-6 | Request smuggling |  Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability | Practitioner | N/A |
| 182 | 2026-02-6 | Request smuggling |  Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability | Practitioner | N/A |
| 183 | 2026-02-7 | Request smuggling |  Exploiting HTTP request smuggling to reveal front-end request rewriting | Practitioner | N/A |
| 184 | 2026-02-7 | Request smuggling |  Exploiting HTTP request smuggling to capture other users' requests | Practitioner | N/A |
| 185 | 2026-02-7 | Request smuggling |  Exploiting HTTP request smuggling to deliver reflected XSS | Practitioner | N/A |
| 186 | 2026-02-7 | Request smuggling |  Exploiting HTTP request smuggling to perform web cache poisoning | Expert | [writeup](https://github.com/ammarsabit/portswigger-labs-writeup/tree/main/Request_smuggling/Exploiting_HTTP_request_smuggling_to_perform_web_cache_poisoning) |
| 187 | 2026-02-8 | Request smuggling |  HTTP request smuggling, basic CL.TE vulnerability | Practitioner | N/A |
| 188 | 2026-02-8 | Request smuggling |  HTTP request smuggling, basic TE.CL vulnerability | Practitioner | N/A |
| 189 | 2026-02-8 | Request smuggling |  HTTP request smuggling, obfuscating the TE header | Practitioner | N/A |
| 190 | 2026-02-8 | Request smuggling |  Exploiting HTTP request smuggling to perform web cache deception | Expert | N/A |
| 191 | 2026-02-10 | Request smuggling |  H2.CL request smuggling | Practitioner | N/A |
| 192 | 2026-02-10 | Request smuggling |  Response queue poisoning via H2.TE request smuggling | Practitioner | N/A |
| 193 | 2026-02-10 | Request smuggling |  HTTP/2 request smuggling via CRLF injection | Practitioner | N/A |
| 194 | 2026-02-10 | Request smuggling |  HTTP/2 request splitting via CRLF injection | Practitioner | N/A |
| 195 | 2026-02-11 | Request smuggling |  CL.0 request smuggling | Practitioner | N/A |
| 196 | 2026-02-11 | Request smuggling |  Client-side desync | Expert | N/A |
| 197 | 2026-02-17 | Request smuggling |  Bypassing access controls via HTTP/2 request tunnelling | Expert | N/A |
| 198 | 2026-02-26 | OAuth authentication |  Forced OAuth profile linking | Practitioner | N/A |
| 199 | 2026-02-26 | OAuth authentication |  OAuth account hijacking via redirect_uri | Practitioner | N/A |
| 200 | 2026-02-26 | OAuth authentication |  Stealing OAuth access tokens via an open redirect | Practitioner | N/A |
| 201 | 2026-02-27 | OAuth authentication |  SSRF via OpenID dynamic client registration | Practitioner | N/A |
| 202 | 2026-02-27 | Server-side request forgery (SSRF) |  SSRF with filter bypass via open redirection vulnerability | Practitioner | N/A |
| 203 | 2026-02-27 | Server-side request forgery (SSRF) |  Blind SSRF with Shellshock exploitation | Expert | N/A |
| 204 | 2026-03-01 | Authentication vulnerabilities |  2FA broken logic | Practitioner | N/A |
| 205 | 2026-03-01 | Business logic vulnerabilities |  Insufficient workflow validation | Practitioner | N/A |
| 206 | 2026-03-01 | Authentication vulnerabilities |  2FA bypass using a brute-force attack | Expert | N/A |
| 207 | 2026-03-02 | Race conditions |  Multi-endpoint race conditions | Practitioner | N/A |
| 208 | 2026-03-02 | Race conditions |  Single-endpoint race conditions | Practitioner | N/A |
| 209 | 2026-03-02 | Race conditions |  Exploiting time-sensitive vulnerabilities | Practitioner | N/A |
| 210 | 2026-03-02 | Race conditions |  Partial construction race conditions | Expert | N/A |
| 211 | 2026-03-03 | WebSockets |  Cross-site WebSocket hijacking | Practitioner | N/A |
| 212 | 2026-03-03 | WebSockets |  Manipulating the WebSocket handshake to exploit vulnerabilities | Practitioner | N/A |
| 213 | 2026-03-03 | Cross-site scripting |  Reflected XSS in canonical link tag | Practitioner | N/A |
| 214 | 2026-03-04 | Server-side request forgery (SSRF) |  Reflected XSS in canonical link tag | Expert | N/A |
| 215 | 2026-03-04 | DOM-based vulnerabilities |  DOM-based cookie manipulation | Practitioner | N/A |
| 216 | 2026-03-04 | DOM-based vulnerabilities |  Exploiting DOM clobbering to enable XSS | Expert | N/A |
| 217 | 2026-03-04 | DOM-based vulnerabilities |  Clobbering DOM attributes to bypass HTML filters | Expert | N/A |
| 218 | 2026-03-06 | Cross-site scripting |  Reflected XSS into a JavaScript string with single quote and backslash escaped | Practitioner | N/A |
| 219 | 2026-03-06 | Cross-site scripting |  Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped | Practitioner | N/A |
| 220 | 2026-03-06 | Cross-site scripting |  Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped | Practitioner | N/A |
| 221 | 2026-03-06 | Cross-site scripting |  Reflected DOM XSS | Practitioner | N/A |
| 222 | 2026-03-06 | Cross-site request forgery (CSRF) |  SameSite Strict bypass via client-side redirect | Practitioner | N/A |
| 223 | 2026-03-07 | Cross-site request forgery (CSRF) |  CSRF where token is tied to non-session cookie | Practitioner | N/A |
| 224 | 2026-03-07 | Cross-site request forgery (CSRF) |  CSRF where token is duplicated in cookie | Practitioner | N/A |
| 225 | 2026-03-09 | Insecure deserialization |  Arbitrary object injection in PHP | Practitioner | N/A |
| 226 | 2026-03-09 | Web cache poisoning |  Parameter cloaking | Practitioner | N/A |
| 227 | 2026-03-09 | Web cache poisoning |  Web cache poisoning via a fat GET request | Practitioner | N/A |
| 228 | 2026-03-09 | Web cache poisoning |  URL normalization | Practitioner | N/A |
| 229 | 2026-03-12 | Insecure deserialization |  Exploiting Java deserialization with Apache Commons | Practitioner | N/A |
| 230 | 2026-03-13 | Insecure deserialization |  Exploiting PHP deserialization with a pre-built gadget chain | Practitioner | N/A |
| 231 | 2026-03-13 | Insecure deserialization |  Exploiting Ruby deserialization using a documented gadget chain | Practitioner | N/A |
| 232 | 2026-03-13 | Business logic vulnerabilities |  Weak isolation on dual-use endpoint | Practitioner | N/A |
| 233 | 2026-03-14 | Prototype pollution |  DOM XSS via client-side prototype pollution | Practitioner | N/A |
| 234 | 2026-03-14 | Prototype pollution |  DOM XSS via an alternative prototype pollution vector | Practitioner | N/A |
| 235 | 2026-03-14 | Prototype pollution |  Client-side prototype pollution via flawed sanitization | Practitioner | N/A |
| 236 | 2026-03-14 | Prototype pollution |  Client-side prototype pollution in third-party libraries | Practitioner | N/A |
| 237 | 2026-03-14 | Prototype pollution |  Client-side prototype pollution via browser API | Practitioner | N/A |
| 238 | 2026-03-14 | Server-side template injection |  Server-side template injection in a sandboxed environment | Expert | N/A |
