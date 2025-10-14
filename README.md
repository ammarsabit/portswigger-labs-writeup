# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-21-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2025--10--14-yellow)

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
| 20  | 2025-10-14 | Path traversal | File path traversal, simple case | Apprentice | N/A |

## Level progress
- **Apprentice**: 11 of 59
- **Practitioner**: 10 of 171
- **Expert**: 0 of 40

## Categories Covered
- **API Testing**: 3/5 lab
- **Information Disclosure**: 5/5 lab
- **Business logic vulnerabilities**: 2/11 lab
- **Authentication vulnerabilities**: 6/14 lab
- **Server-side template injection**: 4/7 lab
- **Path traversal**: 1/6 lab

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
