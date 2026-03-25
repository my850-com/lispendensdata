#!/usr/bin/env python3
"""Batch create all state pages for LisPendensData"""

STATES = [
    ('CT', 'Connecticut', 'Hartford, New Haven, Stamford', ['Hartford', 'New Haven', 'Bridgeport', 'Stamford', 'Waterbury'], '8'),
    ('DE', 'Delaware', 'Wilmington, Dover, Newark', ['Wilmington', 'Dover', 'Newark', 'Middletown'], '3'),
    ('HI', 'Hawaii', 'Honolulu, Maui, Big Island', ['Honolulu', 'Hilo', 'Kailua', 'Kahului', 'Kapolei'], '5'),
    ('IA', 'Iowa', 'Des Moines, Cedar Rapids, Davenport', ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City'], '99'),
    ('IL', 'Illinois', 'Chicago, Springfield, Peoria', ['Chicago', 'Springfield', 'Peoria', 'Rockford', 'Naperville'], '102'),
    ('IN', 'Indiana', 'Indianapolis, Fort Wayne, Evansville', ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend', 'Carmel'], '92'),
    ('KY', 'Kentucky', 'Louisville, Lexington, Bowling Green', ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington'], '120'),
    ('LA', 'Louisiana', 'New Orleans, Baton Rouge, Shreveport', ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Lake Charles'], '64'),
    ('ME', 'Maine', 'Portland, Lewiston, Bangor', ['Portland', 'Lewiston', 'Bangor', 'South Portland', 'Auburn'], '16'),
    ('ND', 'North Dakota', 'Fargo, Bismarck, Grand Forks', ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo'], '53'),
    ('NJ', 'New Jersey', 'Newark, Jersey City, Paterson', ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Trenton'], '21'),
    ('NM', 'New Mexico', 'Albuquerque, Santa Fe, Las Cruces', ['Albuquerque', 'Santa Fe', 'Las Cruces', 'Rio Rancho', 'Roswell'], '33'),
    ('NY', 'New York', 'NYC, Buffalo, Rochester, Syracuse', ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse'], '62'),
    ('OH', 'Ohio', 'Columbus, Cleveland, Cincinnati', ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron'], '88'),
    ('OK', 'Oklahoma', 'Oklahoma City, Tulsa, Norman', ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Lawton'], '77'),
    ('PA', 'Pennsylvania', 'Philadelphia, Pittsburgh, Allentown', ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading'], '67'),
    ('SC', 'South Carolina', 'Columbia, Charleston, Greenville', ['Columbia', 'Charleston', 'North Charleston', 'Mount Pleasant', 'Rock Hill'], '46'),
    ('VT', 'Vermont', 'Burlington, Rutland, Montpelier', ['Burlington', 'Rutland', 'Essex', 'South Burlington', 'Barre'], '14'),
    ('WI', 'Wisconsin', 'Milwaukee, Madison, Green Bay', ['Milwaukee', 'Madison', 'Green Bay', 'Kenosha', 'Racine'], '72'),
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{state_name} Lis Pendens Data | {major_cities} Foreclosures</title>
  <meta name="description" content="Fresh Lis Pendens filings from {state_name} counties. Daily and weekly pre-foreclosure data for {major_cities}. Real estate investor insights. Starting at $49.">
  <meta name="keywords" content="{state_name} lis pendens, {state_name} foreclosure data, {cities_for_meta}, {state_name} real estate investing">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%231a3a5c' width='32' height='32' rx='6'/%3E%3Ctext x='50%25' y='55%25' font-size='14' text-anchor='middle' fill='%23c9a227' font-weight='bold' dominant-baseline='middle'%3EL%3C/text%3E%3C/svg%3E">
  <style>
    :root {{ --navy: #1a3a5c; --gold: #c9a227; --white: #ffffff; --light: #f8f9fa; --text: #2c3e50; --blue: #1976d2; }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: var(--text); line-height: 1.6; }}
    .navbar {{ background: var(--navy); padding: 1rem 0; position: fixed; width: 100%; top: 0; z-index: 1000; }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ color: var(--white); font-size: 1.5rem; font-weight: 700; text-decoration: none; }}
    .logo span {{ color: var(--gold); }}
    .hamburger {{ display: none; flex-direction: column; justify-content: space-around; width: 30px; height: 24px; background: transparent; border: none; cursor: pointer; padding: 0; z-index: 1002; margin-left: auto; }}
    .hamburger span {{ width: 100%; height: 3px; background: var(--gold); border-radius: 2px; transition: all 0.3s; }}
    .hamburger.active span:nth-child(1) {{ transform: rotate(45deg) translate(5px, 5px); }}
    .hamburger.active span:nth-child(2) {{ opacity: 0; }}
    .hamburger.active span:nth-child(3) {{ transform: rotate(-45deg) translate(7px, -6px); }}
    .nav-menu {{ display: flex; }}
    .nav-link {{ color: var(--white); text-decoration: none; margin-left: 20px; font-weight: 500; }}
    @media (max-width: 768px) {{ .hamburger {{ display: flex; }} .nav-menu {{ display: none; position: fixed; top: 60px; left: 0; right: 0; bottom: 0; background: var(--navy); padding: 2rem; flex-direction: column; gap: 1.5rem; }} .nav-menu.active {{ display: flex; }} .nav-link {{ margin-left: 0; }} }}
    .hero {{ background: linear-gradient(135deg, var(--navy) 0%, #2a5298 100%); color: var(--white); padding: 130px 20px 60px; }}
    .hero-content {{ max-width: 900px; margin: 0 auto; }}
    .breadcrumb {{ color: rgba(255,255,255,0.7); font-size: 0.85rem; margin-bottom: 15px; }}
    .breadcrumb a {{ color: var(--gold); text-decoration: none; }}
    .hero h1 {{ font-size: 2.2rem; margin-bottom: 15px; }}
    .hero p {{ font-size: 1rem; opacity: 0.9; line-height: 1.6; }}
    .hero-cta {{ display: inline-block; padding: 14px 35px; background: var(--gold); color: var(--navy); border-radius: 8px; text-decoration: none; font-weight: 700; margin-top: 15px; }}
    .content {{ max-width: 900px; margin: 0 auto; padding: 50px 20px; }}
    .county-intro {{ background: var(--white); padding: 30px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-left: 4px solid var(--gold); }}
    .county-intro h2 {{ color: var(--navy); font-size: 1.4rem; margin-bottom: 15px; }}
    .county-intro p {{ color: #555; line-height: 1.7; margin-bottom: 12px; }}
    .cities-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin: 20px 0; }}
    .city-item {{ background: var(--white); padding: 15px; border-radius: 6px; text-align: center; border: 1px solid #ddd; }}
    .cta-box {{ background: linear-gradient(135deg, var(--navy) 0%, #2a5298 100%); color: white; padding: 40px; border-radius: 12px; text-align: center; margin: 40px 0; }}
    .cta-box h3 {{ font-size: 1.5rem; margin-bottom: 15px; }}
    .cta-btn {{ display: inline-block; padding: 14px 35px; background: var(--gold); color: var(--navy); border-radius: 8px; text-decoration: none; font-weight: 700; }}
  </style>
</head>
<body>
  <nav class="navbar">
    <div class="nav-container">
      <a href="../" class="logo">LisPendens<span>Data</span></a>
      <button class="hamburger" id="hamburgerBtn"><span></span><span></span><span></span></button>
      <div class="nav-menu" id="navMenu">
        <a href="../" class="nav-link">Home</a>
        <a href="../#pricing" class="nav-link">Pricing</a>
      </div>
    </div>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <div class="breadcrumb"><a href="../">Home</a> / {state_name}</div>
      <h1>{state_name} Lis Pendens Data</h1>
      <p>Fresh foreclosure filings from {top_cities}. Daily and weekly pre-foreclosure data for real estate investors across all {county_count} {state_name} counties.</p>
      <a href="../#pricing" class="hero-cta">Get {state_name} Data →</a>
    </div>
  </section>

  <section class="content">
    <div class="county-intro">
      <h2>Why {state_name} Pre-Foreclosures?</h2>
      <p>{state_name} offers unique real estate investment opportunities through its diverse housing markets. Major metro areas like {major_cities} consistently produce foreclosure filings that represent significant discount opportunities for prepared investors.</p>
      <p>Our daily Lis Pendens data tracks every filing from {state_name} county courthouses, delivering fresh pre-foreclosure leads within 24-48 hours of recording. Whether you're targeting urban revitalization or suburban growth markets, {state_name} delivers.</p>
    </div>
    
    <div class="county-intro">
      <h2>Major {state_name} Markets</h2>
      <div class="cities-grid">
        {city_items}
      </div>
    </div>
    
    <div class="cta-box">
      <h3>Get {state_name} Lis Pendens Data</h3>
      <p>Start at $49/month for weekly updates. Daily delivery available. No long-term contracts.</p>
      <a href="../#pricing" class="cta-btn">View Pricing</a>
    </div>
  </section>

  <script>
    document.getElementById('hamburgerBtn').addEventListener('click', function() {{
      this.classList.toggle('active');
      document.getElementById('navMenu').classList.toggle('active');
    }});
  </script>
</body>
</html>'''

import os

os.makedirs('/Users/sherlockhomes/.openclaw/workspace/lis-pendensdata/states', exist_ok=True)

for code, name, major_cities, cities, county_count in STATES:
    # Create URL-friendly filename
    filename = name.lower().replace(' ', '-')
    filepath = f'/Users/sherlockhomes/.openclaw/workspace/lis-pendensdata/states/{filename}.html'
    
    # Generate city items
    city_items = '\n        '.join([f'<div class="city-item"><strong>{c}</strong></div>' for c in cities[:5]])
    
    # Generate meta keywords cities
    cities_for_meta = ', '.join(cities[:3])
    top_cities = ', '.join(cities[:3])
    
    content = TEMPLATE.format(
        state_name=name,
        state_code=code,
        major_cities=major_cities,
        cities_for_meta=cities_for_meta,
        top_cities=top_cities,
        city_items=city_items,
        county_count=county_count
    )
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created: states/{filename}.html")

print(f"\n✅ Created {len(STATES)} state pages")
