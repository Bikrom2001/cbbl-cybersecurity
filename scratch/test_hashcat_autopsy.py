import xml.etree.ElementTree as ET

hashcat_svg = '''<svg viewBox="0 0 32 32" width="24" height="24">
  <rect x="2" y="2" width="28" height="28" rx="7" fill="#111827"/>
  <!-- Hashcat cat head silhouette with ears -->
  <path d="M 7.5 10 L 10.5 18 C 12 21.5 20 21.5 21.5 18 L 24.5 10 L 20 13 C 17.8 11.8 14.2 11.8 12 13 Z" fill="#F43F5E"/>
  <path d="M 8.2 9.5 L 11 17 C 12.5 20 19.5 20 21 17 L 23.8 9.5 L 19.5 12.2 C 17.5 11.2 14.5 11.2 12.5 12.2 Z" fill="#FFFFFF"/>
  <!-- Eyes -->
  <ellipse cx="13.2" cy="16" rx="1.2" ry="1.6" fill="#111827"/>
  <ellipse cx="18.8" cy="16" rx="1.2" ry="1.6" fill="#111827"/>
  <!-- Nose -->
  <polygon points="16,17.8 14.8,19.2 17.2,19.2" fill="#F43F5E"/>
  <!-- Hash Whisker Marks -->
  <line x1="8.5" y1="16.5" x2="10.5" y2="17" stroke="#F43F5E" stroke-width="1" stroke-linecap="round"/>
  <line x1="23.5" y1="16.5" x2="21.5" y2="17" stroke="#F43F5E" stroke-width="1" stroke-linecap="round"/>
</svg>'''

autopsy_svg = '''<svg viewBox="0 0 32 32" width="24" height="24">
  <rect x="2" y="2" width="28" height="28" rx="7" fill="#FFFBEB"/>
  <!-- Autopsy Bloodhound Dog Mascot (Digital Forensics) -->
  <path d="M10 15.5 C8 15.5 7 17.5 7 19.5 C7 22 9 23 12 23 C14 23 16 22 17 21 L19.5 21 C22.5 21 24.5 18.5 24.5 15.5 C24.5 12.5 22 9.5 18 9.5 C15 9.5 13 11 11 12.5 Z" fill="#D97706"/>
  <!-- Floppy Brown Ear -->
  <path d="M17 11 C14.5 11 13.5 13.5 13.5 16.5 C13.5 20.5 15.5 23.5 17.5 24.2 C19.2 25 21.2 23 21.2 19.5 C21.2 15.5 20 11 17 11 Z" fill="#78350F"/>
  <!-- Eye -->
  <circle cx="12.8" cy="14" r="1.3" fill="#1F2937"/>
  <circle cx="13.2" cy="13.6" r="0.5" fill="#FFFFFF"/>
  <!-- Nose -->
  <ellipse cx="7.8" cy="19" rx="1.7" ry="1.3" fill="#1F2937"/>
  <!-- Muzzle Line -->
  <path d="M8 20.5 Q10 21.8 12 20.5" stroke="#78350F" stroke-width="1" fill="none" stroke-linecap="round"/>
</svg>'''

ET.fromstring(hashcat_svg)
print("SUCCESS: Hashcat SVG is valid XML!")

ET.fromstring(autopsy_svg)
print("SUCCESS: Autopsy SVG is valid XML!")
