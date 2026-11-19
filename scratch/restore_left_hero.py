import re

original_left_col = '''            <div class="col-lg-6">
              <p class="eyebrow">
                Cybersecurity · IT Solutions · Professional Training
              </p>
              <h1 class="display-5 fw-bold mb-3">
                Security you can plan for. Skills you can prove.
              </h1>
              <p class="hero__lead lead mb-4">
                CBBL helps organisations reduce technology risk and helps
                professionals build careers in IT and cybersecurity. Every
                engagement starts with a written scope. Every course ends with
                an assessment you can show an employer.
              </p>
              <div class="btn-row mb-4">
                <a class="btn btn-primary" href="contact.html"
                  >Request a Security Consultation</a
                >
                <a class="btn btn-secondary" href="training.html"
                  >Explore Training</a
                >
              </div>
              <div class="hero__meta">
                <span>◆ Operating since 2016</span>
                <span>◆ Dhaka, Bangladesh</span>
                <span>◆ Online, on-site and lab delivery</span>
              </div>
            </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div class="col-lg-6">\s*<!-- Live Pulse Eyebrow Pill -->.*?</div>\s*</div>\s*(?=<div class="col-lg-6">)'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + original_left_col + '\n            ' + html[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESS: Restored original left hero column in index.html!")
else:
    print("ERROR: Could not find left column pattern in index.html")
