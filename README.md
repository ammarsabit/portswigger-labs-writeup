# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-72-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2025--11--23-yellow)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

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
| 10  | 2025-09-30 | Authentication vulnerabilities | Password reset broken logic | Apprentice | N/A |
| 11  | 2025-09-30 | Authentication vulnerabilities | Password brute-force via password change | Practitioner | N/A |
| 12  | 2025-09-30 | Information disclosure | Authentication bypass via information disclosure | Apprentice | N/A |
| 13  | 2025-09-30 | Information disclosure | Information disclosure on debug page | Apprentice | N/A |
| 14  | 2025-09-30 | Information disclosure | Source code disclosure via backup files | Apprentice | N/A |
| 15  | 2025-09-30 | Information disclosure | Information disclosure in version control history | Apprentice | N/A |
| 16  | 2025-09-30 | Server-side template injection | Basic server-side template injection | Practitioner | [writeup](https://github.com/ammarsabit/portswigger-labs-writeup/blob/main/ssti/basic-server-side-template-injection.md) |
| 17  | 2025-09-30 | Server-side template injection | Basic server-side template injection (code context) | Practitioner | N/A |
| 18  | 2025-10-9 | Server-side template injection | Server-side template injection in an unknown language with a documented exploit | Practitioner | N/A |
| 19  | 2025-10-9 | Authentication vulnerabilities | Username enumeration via account lock | Practitioner | N/A |
| 20  | 2025-10-10 | Server-side template injection | Server-side template injection with information disclosure via user-supplied objects | Practitioner | N/A |
| 21  | 2025-10-14 | Path traversal | File path traversal, simple case | Apprentice | N/A |
| 22  | 2025-10-14 | Path traversal | File path traversal, traversal sequences blocked with absolute path bypass | Practitioner | N/A |
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

## Level progress
- **Apprentice**: 32 of 59
- **Practitioner**: 40 of 171
- **Expert**: 0 of 40

## Categories Covered
- **API Testing**: 3/5 lab
- **Information Disclosure**: 5/5 lab
- **Business logic vulnerabilities**: 2/11 lab
- **Authentication vulnerabilities**: 6/14 lab
- **Server-side template injection**: 5/7 lab
- **Path traversal**: 6/6 lab
- **File upload vulnerabilities**: 5/7 lab
- **Cross-site scripting**: 5/30 lab
- **SQL injection**: 13/18 lab
- **Race conditions**: 2/6 lab
- **Access control**: 10/13 lab
- **OS command injection**: 5/5 lab
- **Server-side request forgery (SSRF)**: 4/7 lab
- **JWT attacks**: 1/8 lab

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
- 
---
