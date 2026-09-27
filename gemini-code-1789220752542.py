# Create a dedicated visual cheat sheet for Unit 1
unit1_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @page {
        size: A4 landscape;
        margin: 10mm;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 8pt;
        line-height: 1.35;
        color: #0f172a;
        background: #f8fafc;
        margin: 0;
        padding: 0;
    }
    .header {
        background: #0284c7;
        color: #ffffff;
        padding: 8px 14px;
        border-radius: 4px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header h1 {
        margin: 0;
        font-size: 14pt;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .grid-container {
        column-count: 2;
        column-gap: 12px;
    }
    .card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 5px;
        padding: 8px 10px;
        margin-bottom: 10px;
        break-inside: avoid;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .card-title {
        font-size: 9pt;
        font-weight: 800;
        color: #0369a1;
        border-bottom: 1.5px solid #e0f2fe;
        padding-bottom: 3px;
        margin-bottom: 6px;
    }
    .badge {
        background: #0284c7;
        color: white;
        padding: 1px 5px;
        border-radius: 3px;
        font-size: 7pt;
        font-weight: bold;
        margin-right: 4px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 7.5pt;
        margin-top: 4px;
    }
    th, td {
        border: 1px solid #cbd5e1;
        padding: 4px 6px;
        text-align: left;
    }
    th {
        background: #f1f5f9;
        color: #0f172a;
    }
    code {
        font-family: Consolas, monospace;
        font-size: 7.5pt;
        background: #f1f5f9;
        padding: 1px 3px;
        border-radius: 2px;
        border: 1px solid #e2e8f0;
    }
    pre {
        background: #0f172a;
        color: #38bdf8;
        padding: 6px;
        border-radius: 4px;
        font-family: Consolas, monospace;
        font-size: 7pt;
        margin: 4px 0;
        white-space: pre-wrap;
    }
    ul {
        margin: 3px 0 3px 14px;
        padding: 0;
    }
    li {
        margin-bottom: 2px;
    }
</style>
</head>
<body>

<div class="header">
    <h1>Unit 1: Foundations of Penetration Testing — Visual Reference Sheet</h1>
    <div>Exam Quick-Revision Card</div>
</div>

<div class="grid-container">

    <div class="card">
        <div class="card-title"><span class="badge">Q1</span> Vulnerability Assessment (VA) vs. Penetration Testing (PT)</div>
        <table>
            <tr><th>Metric</th><th>VA (Breadth)</th><th>PT (Depth)</th></tr>
            <tr><td><strong>Goal</strong></td><td>List all known flaws.</td><td>Simulate real-world attack & exploit flaws.</td></tr>
            <tr><td><strong>Action</strong></td><td>Automated scan; non-destructive.</td><td>Active exploitation; chains weaknesses.</td></tr>
            <tr><td><strong>Output</strong></td><td>CVSS list + patch links.</td><td>Proof of Concept (PoC) + business impact.</td></tr>
        </table>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">Q2 & Q3</span> Burp Suite Modules & Intruder Attack Modes</div>
        <ul>
            <li><strong>Proxy (127.0.0.1:8080):</strong> Intercepts & tampers HTTP/S traffic in flight.</li>
            <li><strong>Repeater:</strong> Manual replay & iterative request testing.</li>
            <li><strong>Intruder:</strong> Automated fuzzing, brute-forcing, and rate-limit testing.</li>
            <li><strong>Decoder:</strong> Instant conversion between URL, Base64, Hex, and HTML.</li>
            <li><strong>Comparer:</strong> Visual side-by-side diff tool for response changes.</li>
        </ul>
        <table>
            <tr><th>Intruder Mode</th><th>Payload Markers</th><th>Payload Wordlists</th></tr>
            <tr><td><strong>Sniper</strong></td><td>Multiple (sequential)</td><td>1 wordlist (cycles one marker at a time)</td></tr>
            <tr><td><strong>Battering Ram</strong></td><td>Multiple (simultaneous)</td><td>1 wordlist (injects identical value in all)</td></tr>
            <tr><td><strong>Pitchfork</strong></td><td>Multiple (lockstep)</td><td>Multiple (List 1A with 2A, 1B with 2B)</td></tr>
            <tr><td><strong>Cluster Bomb</strong></td><td>Multiple (matrix)</td><td>Multiple (Cartesian product / all permutations)</td></tr>
        </table>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">Q4</span> STRIDE Threat Modeling Framework</div>
        <table>
            <tr><th>Threat</th><th>Security Goal</th><th>Web Attack Example</th></tr>
            <tr><td><strong>Spoofing</strong></td><td>Authentication</td><td>Replaying stolen session cookies / JWT tampering</td></tr>
            <tr><td><strong>Tampering</strong></td><td>Integrity</td><td>Modifying hidden price fields in HTTP POST</td></tr>
            <tr><td><strong>Repudiation</strong></td><td>Non-Repudiation</td><td>Lack of audit logs for financial transfers</td></tr>
            <tr><td><strong>Information Disc.</strong></td><td>Confidentiality</td><td>Verbose SQL syntax errors exposing schema/passwords</td></tr>
            <tr><td><strong>Denial of Service</strong></td><td>Availability</td><td>Billion Laughs XML nested entity exhaustion</td></tr>
            <tr><td><strong>Elevation of Priv.</strong></td><td>Authorization</td><td>Forced browsing to administrative URL endpoints</td></tr>
        </table>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">Q5</span> DREAD Risk Evaluation Model</div>
        <p>Formula: <code>Risk = (D + R + E + A + D) / 5</code></p>
        <ul>
            <li><strong>D - Damage Potential:</strong> Severity of total loss if exploited.</li>
            <li><strong>R - Reproducibility:</strong> How consistently the attack executes (100% vs flaky).</li>
            <li><strong>E - Exploitability:</strong> Skill and tools needed (web browser vs custom zero-day).</li>
            <li><strong>A - Affected Users:</strong> Fraction of user base impacted.</li>
            <li><strong>D - Discoverability:</strong> Ease of identifying the flaw in the wild.</li>
        </ul>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">Q6</span> SQL Injection (In-Band vs. Blind) & Mitigations</div>
        <ul>
            <li><strong>Error-Based (In-band):</strong> Forces DB syntax errors returning sensitive tables.</li>
            <li><strong>UNION-Based (In-band):</strong> Appends attacker data: <code>' UNION SELECT null, username, password FROM users--</code></li>
            <li><strong>Boolean Blind:</strong> Injects conditions: <code>' AND SUBSTRING(pass,1,1)='a'--</code> (True/False checks).</li>
            <li><strong>Time-Based Blind:</strong> Injects delay commands: <code>'; WAITFOR DELAY '0:0:5'--</code> or <code>pg_sleep(5)</code>.</li>
        </ul>
        <pre>// Defense: Parameterized Queries / Prepared Statements (Never concatenate!)
$stmt = $pdo->prepare('SELECT id FROM users WHERE user = :u AND pass = :p');
$stmt->execute(['u' => $userInput, 'p' => $passInput]);</pre>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">Q7</span> Kali Linux Toolkit Workflow</div>
        <ul>
            <li><code>nmap -sC -sV -p- -oN scan.txt &lt;IP&gt;</code>: Port discovery, service fingerprinting, scripts.</li>
            <li><code>gobuster dir -u http://&lt;IP&gt; -w common.txt</code>: Discover unlinked directories & endpoints.</li>
            <li><code>hydra -l admin -P rockyou.txt &lt;IP&gt; ssh / http-post-form</code>: Network credential brute-forcing.</li>
            <li><code>sqlmap -u "http://&lt;IP&gt;/item?id=1" --dbs --batch</code>: Automated SQL injection extraction.</li>
        </ul>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">10M</span> Penetration Testing Lifecycle (PTES / NIST SP 800-115)</div>
        <ol>
            <li><strong>Pre-engagement & Scoping:</strong> RoE, NDA, IP ranges, legal sign-off.</li>
            <li><strong>Reconnaissance & OSINT:</strong> WHOIS, DNS queries, Shodan, Google dorks.</li>
            <li><strong>Scanning & Enumeration:</strong> Port scanning (<code>nmap</code>), banner grabbing.</li>
            <li><strong>Vulnerability Analysis:</strong> CVE mapping, scanning with Nessus/Nikto.</li>
            <li><strong>Exploitation:</strong> Trigger PoC exploits (<code>searchsploit</code>, Metasploit).</li>
            <li><strong>Post-Exploitation:</strong> PrivEsc, pivoting to internal subnets, credential dumps.</li>
            <li><strong>Reporting:</strong> Executive summary, CVSS scoring, technical remediation steps.</li>
        </ol>
    </div>

    <div class="card">
        <div class="card-title"><span class="badge">10M</span> Thought Experiment: "Delete FB Photo Without Credentials"</div>
        <ul>
            <li><strong>Vector 1 (Session Hijacking):</strong> Sniff unencrypted Wi-Fi or steal session cookie via XSS.</li>
            <li><strong>Vector 2 (SQL Injection):</strong> Inject into public forms to execute backend <code>DELETE FROM photos...</code></li>
            <li><strong>Vector 3 (Social Engineering):</strong> Spear phishing or vishing victim to trigger action.</li>
            <li><strong>Vector 4 (OSINT / Dark Web):</strong> Credential stuffing using leaked databases and Google dorks.</li>
            <li><strong>Remediation:</strong> <code>HttpOnly</code> cookies, MFA (FIDO2), Prepared Statements, strict RBAC ownership checks.</li>
        </ul>
    </div>

</div>

</body>
</html>
"""

with open("unit1_visual_cheatsheet.html", "w") as f:
    f.write(unit1_html)

from weasyprint import HTML
HTML("unit1_visual_cheatsheet.html").write_pdf("Unit_1_Foundations_Visual_Cheatsheet.pdf")