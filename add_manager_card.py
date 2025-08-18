from pathlib import Path

# 讀取使用者上傳的 index_Version2.html
input_path = "/home/runner/work/hongyan-official/hongyan-official/index_Version2.html"
output_path = "/home/runner/work/hongyan-official/hongyan-official/index_Version2_with_manager.html"

html = Path(input_path).read_text(encoding="utf-8")

# 黑金卡片區塊
manager_card_block = """
<!-- 劉襄理｜黑金名片風格 -->
<section id="manager-card">
  <style>
    #manager-card{--bg:#0a0a0a;--card:#1a1a1a;--gold:#fbbf24;--gold2:#d97706;--text:#eaeaea;--muted:#9a9a9a;--line:#06C755;font-family:"Noto Sans TC","Microsoft JhengHei",system-ui}
    #manager-card .wrap{max-width:900px;margin:auto;padding:30px 18px}
    #manager-card .hero{display:grid;grid-template-columns:140px 1fr;gap:20px;background:linear-gradient(145deg,#111,#1a1a1a);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:24px;box-shadow:0 10px 24px rgba(0,0,0,.7);color:var(--text)}
    #manager-card .avatar{width:140px;height:140px;object-fit:cover;border-radius:8px;border:2px solid var(--gold);box-shadow:0 0 12px rgba(251,191,36,.5)}
    #manager-card h2{margin:0;font-size:26px;font-weight:800;color:var(--gold)}
    #manager-card .title{font-size:15px;color:var(--muted);margin:6px 0 14px}
    #manager-card .services{list-style:none;padding:0;margin:10px 0;display:grid;gap:6px}
    #manager-card .services li{font-size:14px;color:var(--text);padding-left:12px;position:relative}
    #manager-card .services li::before{content:"◆";color:var(--gold);position:absolute;left:0;font-size:12px;top:2px}
    #manager-card .cta{margin:16px 0;display:flex;gap:12px;flex-wrap:wrap}
    #manager-card .btn{padding:9px 16px;border-radius:10px;text-decoration:none;font-weight:600;transition:.25s;box-shadow:0 4px 12px rgba(0,0,0,.4)}
    #manager-card .btn.call{background:linear-gradient(45deg,var(--gold),var(--gold2));color:#000}
    #manager-card .btn.call:hover{filter:brightness(1.1);transform:translateY(-2px)}
    #manager-card .btn.line{background:var(--line);color:#fff}
    #manager-card .btn.line:hover{background:#05a84a;transform:translateY(-2px)}
    #manager-card .note{font-size:13px;color:var(--muted)}
    @media(max-width:768px){#manager-card .hero{grid-template-columns:1fr;text-align:center}#manager-card .avatar{margin:auto}#manager-card .services{justify-items:center}}
  </style>

  <div class="wrap">
    <div class="hero">
      <img class="avatar" src="assets/screenshot-1755493265551.png" alt="劉襄理">
      <div>
        <h2>劉家明 襄理</h2>
        <div class="title">鴻晏國際理財中心｜中大額資金規劃</div>
        <ul class="services">
          <li>房屋貸款</li>
          <li>企業貸款</li>
          <li>信用貸款</li>
          <li>汽車貸款</li>
          <li>債務整合</li>
        </ul>
        <div class="cta">
          <a class="btn call" href="tel:+886955376195">📞 0955-376-195</a>
          <a class="btn line" href="https://line.me/ti/p/~aydin1997" target="_blank">💬 LINE @aydin1997</a>
        </div>
        <div class="note">服務時段：每日 09:00–22:00（急件可提前告知）</div>
      </div>
    </div>
  </div>
</section>
"""

# 插入到 </section> 前，選擇一個合適的位置（例如客戶評價之後）
if "<!-- ===== 客戶評價 ===== -->" in html:
    parts = html.split("<!-- ===== 客戶評價 ===== -->")
    if len(parts) >= 2:
        # Find the end of the testimonials section
        testimonials_section = parts[1]
        section_end = testimonials_section.find("</section>")
        if section_end != -1:
            # Insert after the testimonials section ends
            section_end_with_tag = section_end + len("</section>")
            before_manager = parts[0] + "<!-- ===== 客戶評價 ===== -->" + testimonials_section[:section_end_with_tag]
            after_manager = testimonials_section[section_end_with_tag:]
            html = before_manager + manager_card_block + after_manager
        else:
            # Fallback: just add after the comment
            html = parts[0] + "<!-- ===== 客戶評價 ===== -->" + parts[1] + manager_card_block
    else:
        # Fallback: just add after the comment
        html = parts[0] + "<!-- ===== 客戶評價 ===== -->" + parts[1] + manager_card_block
else:
    # If no customer reviews section found, add before the contact section
    html = html.replace('<section class="contact-info">', manager_card_block + '\n<section class="contact-info">')

# 寫出新的檔案
Path(output_path).write_text(html, encoding="utf-8")
print(f"Manager card added successfully! Output saved to: {output_path}")