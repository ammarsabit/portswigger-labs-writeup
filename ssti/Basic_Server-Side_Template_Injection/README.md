# Basic Server-Side Template Injection

## Lab Overview
- **Lab Link**: [https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic)
- **Difficulty**: Practitioner
- **Vulnerability**: Server-Side Template Injection (SSTI)
- **Date Solved**: 2025-10-08
- **Author**: Ammar Sabit

## Description
This lab features a template injection vulnerability in the `/?message=` endpoint. The application uses Ruby's ERB templating engine, which renders user-supplied input without sanitization. This allows arbitrary code execution, leading to remote command execution (RCE) and file manipulation—specifically, deleting a target file to solve the lab.

## Steps to Reproduce

1. **Identify the Injection Point**:
   - Click the first product in the shop; notice it generates a template saying the product is out of stock, hinting at dynamic templating.
   - Use Burp Repeater to send GET requests to `/?message=message-here`.
   - Observe that the server echoes the `message` parameter value inside a `<div>` in the response body.
   - Through trial and error with template syntax, test payloads like `{{7*7}}` (Jinja2-style) or `<%= 3*3 %>` (ERB-style).
   - When injecting `<%= 3*3 %>`, the response renders `9` instead of the literal string, confirming SSTI.

2. **Verify Template Engine**:
   - A quick Google search for the syntax `<%= %>` reveals it's Ruby's ERB (Embedded Ruby) engine.

3. **Exploit the Vulnerability**:
   - To achieve RCE, wrap OS commands in backticks (`` ` ``) inside `<%= %>`.
   - Send: `GET /?message=<%= `ls` %>`
     - Response: Lists directory contents, revealing `morale.txt` is present.
   - To solve the lab, delete the file: `GET /?message=<%= `rm morale.txt` %>`
     - Verify success by re-running `ls`—the file is gone, completing the challenge.

## Impact
- Full RCE on the server, enabling file reads/deletes, data exfiltration, or further compromise (e.g., privilege escalation).

## Prevention
- Avoid passing user input directly to template engines.
- Use safe rendering (e.g., ERB's `html_safe` or equivalent) and whitelist allowed expressions.
- Implement input validation/sanitization to strip template syntax.

## References
- [PortSwigger SSTI Lab](https://portswigger.net/web-security/server-side-template-injection)
- [ssti-payloads](https://github.com/payloadbox/ssti-payloads)

---
