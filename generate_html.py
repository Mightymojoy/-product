import json, os, sys

with open('D:/ITO产品手册/product_images.json', 'r', encoding='utf-8') as f:
    imgs = json.load(f)

# HTML Head with complete CSS styles
HTML_HEAD = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ITO 伊稻（上海）商业有限公司</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --color-black: #000000;
      --color-white: #FFFFFF;
      --color-gray-light: #EDEFEA;
      --color-gray-mid: #8A8A8A;
      --color-gray-dark: #262626;
      --color-blue: #0075B3;
      --color-blue-light: #E6F3FA;
      --color-care-green: #2E7D32;
      --color-care-light: #E8F5E9;
      --font-cn: "Noto Sans SC", "Source Han Sans SC", sans-serif;
      --font-en: "Helvetica Neue", "Arial", sans-serif;
      --transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      --nav-height: 72px;
    }
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth;font-size:16px}
    body{font-family:var(--font-cn);color:var(--color-black);background:var(--color-white);line-height:1.6;overflow-x:hidden}
    img{display:block;max-width:100%}
    a{text-decoration:none;color:inherit}
    ul{list-style:none}

    .nav{position:fixed;top:0;left:0;right:0;height:var(--nav-height);background:var(--color-white);border-bottom:1px solid rgba(0,0,0,0.08);display:flex;align-items:center;justify-content:space-between;padding:0 5%;z-index:1000;transition:var(--transition)}
    .nav.scrolled{box-shadow:0 2px 20px rgba(0,0,0,0.08)}
    .nav-logo{display:flex;align-items:center;gap:12px}
    .nav-logo-mark{width:44px;height:44px;background:var(--color-black);display:flex;align-items:center;justify-content:center;border-radius:2px}
    .nav-logo-mark span{color:var(--color-white);font-size:18px;font-weight:700;letter-spacing:2px;font-family:var(--font-en)}
    .nav-logo-text{display:flex;flex-direction:column;line-height:1.2}
    .nav-logo-text .brand-en{font-size:14px;font-weight:700;letter-spacing:4px;font-family:var(--font-en);color:var(--color-black)}
    .nav-logo-text .brand-cn{font-size:10px;color:var(--color-gray-mid);letter-spacing:1px}
    .nav-links{display:flex;align-items:center;gap:40px}
    .nav-links a{font-size:14px;font-weight:400;letter-spacing:1px;color:var(--color-gray-dark);position:relative;transition:var(--transition)}
    .nav-links a::after{content:"";position:absolute;bottom:-4px;left:0;width:0;height:1px;background:var(--color-black);transition:width 0.3s ease}
    .nav-links a:hover{color:var(--color-black)}
    .nav-links a:hover::after{width:100%}
    .nav-links a.active{color:var(--color-black);font-weight:500}
    .nav-links a.active::after{width:100%}
    .nav-cta{background:var(--color-black);color:var(--color-white)!important;padding:10px 24px;border-radius:2px;font-size:13px!important;letter-spacing:2px;transition:var(--transition)!important}
    .nav-cta:hover{background:var(--color-blue)!important;color:var(--color-white)!important}
    .nav-cta::after{display:none!important}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:5px}
    .nav-hamburger span{width:24px;height:2px;background:var(--color-black);transition:var(--transition)}

    .page{display:none}
    .page.active{display:block}
    .section{padding:100px 5%}
    .container{max-width:1200px;margin:0 auto}
    .section-label{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-gray-mid);margin-bottom:20px;font-family:var(--font-en)}
    .section-label.green{color:var(--color-care-green)}
    .section-title{font-size:clamp(32px,4vw,52px);font-weight:700;line-height:1.15;letter-spacing:-0.5px;color:var(--color-black)}
    .section-title.white{color:var(--color-white)}
    .section-subtitle{font-size:16px;color:var(--color-gray-mid);line-height:1.8;max-width:600px;margin-top:20px}
    .btn{display:inline-flex;align-items:center;gap:10px;padding:14px 32px;font-size:13px;letter-spacing:2px;font-weight:500;cursor:pointer;transition:var(--transition);border:none;outline:none;font-family:var(--font-cn)}
    .btn-primary{background:var(--color-black);color:var(--color-white)}
    .btn-primary:hover{background:var(--color-blue)}
    .btn-care{background:var(--color-care-green);color:var(--color-white)}
    .btn-care:hover{background:#1B5E20}
    .btn-care-outline{background:transparent;color:var(--color-care-green);border:1px solid var(--color-care-green)}
    .btn-care-outline:hover{background:var(--color-care-green);color:var(--color-white)}
    .btn-outline{background:transparent;color:var(--color-black);border:1px solid var(--color-black)}
    .btn-outline:hover{background:var(--color-black);color:var(--color-white)}
    .btn-arrow::after{content:"\\2192";font-size:16px}

    .hero{min-height:100vh;background:var(--color-black);display:flex;align-items:center;padding:0 5%;padding-top:var(--nav-height);position:relative;overflow:hidden}
    .hero-bg-text{position:absolute;top:50%;right:-5%;transform:translateY(-50%);font-size:clamp(120px,18vw,220px);font-weight:900;color:rgba(255,255,255,0.03);font-family:var(--font-en);letter-spacing:-10px;white-space:nowrap;pointer-events:none;user-select:none}
    .hero-grid-lines{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.03) 1px,transparent 1px);background-size:80px 80px;pointer-events:none}
    .hero-content{position:relative;z-index:2;max-width:800px}
    .hero-label{display:inline-flex;align-items:center;gap:12px;font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-blue);margin-bottom:32px;font-family:var(--font-en)}
    .hero-label::before{content:"";width:40px;height:1px;background:var(--color-blue)}
    .hero-title{font-size:clamp(48px,6vw,88px);font-weight:700;color:var(--color-white);line-height:1.05;letter-spacing:-2px;margin-bottom:32px}
    .hero-title em{font-style:normal;color:var(--color-blue)}
    .hero-desc{font-size:17px;color:rgba(255,255,255,0.6);line-height:1.8;max-width:520px;margin-bottom:48px;font-weight:300}
    .hero-actions{display:flex;gap:16px;flex-wrap:wrap}
    .btn-white{background:var(--color-white);color:var(--color-black)}
    .btn-white:hover{background:var(--color-blue);color:var(--color-white)}
    .btn-ghost{background:transparent;color:var(--color-white);border:1px solid rgba(255,255,255,0.3)}
    .btn-ghost:hover{border-color:var(--color-white);background:rgba(255,255,255,0.1)}
    .hero-scroll{position:absolute;bottom:40px;left:5%;display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.4);font-size:11px;letter-spacing:3px;text-transform:uppercase;font-family:var(--font-en)}
    .hero-scroll-line{width:40px;height:1px;background:rgba(255,255,255,0.2)}

    .stats-bar{background:var(--color-gray-light);padding:48px 5%}
    .stats-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:40px}
    .stat-item{text-align:center}
    .stat-number{font-size:42px;font-weight:700;color:var(--color-black);font-family:var(--font-en);line-height:1;margin-bottom:8px}
    .stat-number span{color:var(--color-blue);font-size:28px}
    .stat-label{font-size:13px;color:var(--color-gray-mid);letter-spacing:1px}

    .features{padding:100px 5%;background:var(--color-white)}
    .features-header{max-width:1200px;margin:0 auto 64px;display:flex;justify-content:space-between;align-items:flex-end}
    .features-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(0,0,0,0.06)}
    .feature-card{background:var(--color-white);padding:48px 40px;transition:var(--transition);cursor:default}
    .feature-card:hover{background:var(--color-black)}
    .feature-card:hover .feature-icon{border-color:rgba(255,255,255,0.2)}
    .feature-card:hover .feature-icon svg{stroke:var(--color-white)}
    .feature-card:hover .feature-title{color:var(--color-white)}
    .feature-card:hover .feature-desc{color:rgba(255,255,255,0.6)}
    .feature-card:hover .feature-num{color:rgba(255,255,255,0.15)}
    .feature-icon{width:52px;height:52px;border:1px solid rgba(0,0,0,0.15);border-radius:4px;display:flex;align-items:center;justify-content:center;margin-bottom:32px;transition:var(--transition)}
    .feature-icon svg{width:24px;height:24px;stroke:var(--color-black);fill:none;stroke-width:1.5;transition:var(--transition)}
    .feature-num{font-size:64px;font-weight:700;color:rgba(0,0,0,0.04);font-family:var(--font-en);line-height:1;margin-bottom:-20px;transition:var(--transition)}
    .feature-title{font-size:20px;font-weight:600;margin-bottom:16px;transition:var(--transition)}
    .feature-desc{font-size:14px;color:var(--color-gray-mid);line-height:1.8;transition:var(--transition)}

    .products-showcase{padding:100px 5%;background:var(--color-gray-light)}
    .products-showcase-header{max-width:1200px;margin:0 auto 64px}
    .products-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr;grid-template-rows:auto auto;gap:16px}
    .product-card{background:var(--color-white);overflow:hidden;position:relative;cursor:pointer;transition:var(--transition)}
    .product-card:hover{transform:translateY(-4px);box-shadow:0 20px 60px rgba(0,0,0,0.12)}
    .product-card.large{grid-row:span 2}
    .product-card-inner{padding:48px 36px;display:flex;flex-direction:column;height:100%}
    .product-card.large .product-card-inner{min-height:500px;justify-content:space-between}
    .product-card-visual{flex:1;display:flex;align-items:center;justify-content:center;background:var(--color-gray-light);margin:0 -36px;padding:40px;min-height:200px;position:relative;overflow:hidden}
    .product-card.large .product-card-visual{min-height:320px}
    .product-card-info{padding-top:28px}
    .product-tag{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--color-blue);font-family:var(--font-en);margin-bottom:12px}
    .product-name{font-size:22px;font-weight:600;margin-bottom:8px}
    .product-card.large .product-name{font-size:28px}
    .product-desc{font-size:13px;color:var(--color-gray-mid);line-height:1.7}
    .products-view-all{max-width:1200px;margin:40px auto 0;text-align:center}

    .brand-story{padding:100px 5%;background:var(--color-black);overflow:hidden}
    .brand-story-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
    .brand-story-label{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-blue);margin-bottom:20px;font-family:var(--font-en)}
    .brand-story-title{font-size:clamp(32px,4vw,52px);font-weight:700;color:var(--color-white);line-height:1.15;margin-bottom:32px}
    .brand-story-text{font-size:15px;color:rgba(255,255,255,0.6);line-height:1.9;margin-bottom:24px;font-weight:300}
    .brand-story-visual{position:relative}
    .brand-story-box{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);padding:48px;position:relative}
    .brand-story-box::before{content:'"';font-size:120px;line-height:1;color:rgba(255,255,255,0.05);position:absolute;top:10px;left:24px;font-family:Georgia,serif}
    .brand-story-quote{font-size:22px;font-weight:300;color:var(--color-white);line-height:1.6;position:relative;z-index:1}
    .brand-story-quote em{font-style:normal;color:var(--color-blue)}
    .brand-story-quote-author{margin-top:24px;font-size:12px;letter-spacing:3px;color:rgba(255,255,255,0.4);text-transform:uppercase;font-family:var(--font-en)}

    .page-hero{height:400px;background:var(--color-black);display:flex;align-items:flex-end;padding:0 5% 60px;margin-top:var(--nav-height);position:relative;overflow:hidden}
    .page-hero-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px);background-size:60px 60px}
    .page-hero-content{position:relative;z-index:2;max-width:1200px;width:100%;margin:0 auto}
    .page-hero-label{font-size:11px;letter-spacing:4px;color:var(--color-blue);text-transform:uppercase;font-family:var(--font-en);margin-bottom:16px}
    .page-hero-title{font-size:clamp(40px,5vw,68px);font-weight:700;color:var(--color-white);letter-spacing:-1px}

    .about-intro{padding:100px 5%;background:var(--color-white)}
    .about-intro-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1.5fr;gap:80px;align-items:start}
    .about-intro-sticky{position:sticky;top:100px}
    .about-intro-text{font-size:15px;color:var(--color-gray-dark);line-height:1.9;margin-bottom:24px}
    .about-intro-highlight{font-size:22px;font-weight:500;line-height:1.6;color:var(--color-black);border-left:3px solid var(--color-blue);padding-left:20px;margin:40px 0}

    .mvv{padding:100px 5%;background:var(--color-gray-light)}
    .mvv-inner{max-width:1200px;margin:0 auto}
    .mvv-header{margin-bottom:64px}
    .mvv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(0,0,0,0.08)}
    .mvv-card{background:var(--color-white);padding:52px 40px;transition:var(--transition)}
    .mvv-card:hover{background:var(--color-black)}
    .mvv-card:hover .mvv-en{color:rgba(255,255,255,0.15)}
    .mvv-card:hover .mvv-cn{color:var(--color-blue)}
    .mvv-card:hover .mvv-title{color:var(--color-white)}
    .mvv-card:hover .mvv-text{color:rgba(255,255,255,0.6)}
    .mvv-en{font-size:48px;font-weight:800;color:rgba(0,0,0,0.05);font-family:var(--font-en);line-height:1;transition:var(--transition)}
    .mvv-cn{font-size:12px;letter-spacing:3px;color:var(--color-blue);margin:8px 0 24px;transition:var(--transition)}
    .mvv-title{font-size:24px;font-weight:700;margin-bottom:16px;transition:var(--transition)}
    .mvv-text{font-size:14px;color:var(--color-gray-mid);line-height:1.8;transition:var(--transition)}

    .values{padding:100px 5%;background:var(--color-white)}
    .values-inner{max-width:1200px;margin:0 auto}
    .values-header{margin-bottom:64px}
    .values-list{display:flex;flex-direction:column;gap:0;border-top:1px solid rgba(0,0,0,0.08)}
    .value-item{display:grid;grid-template-columns:80px 240px 1fr;gap:40px;padding:48px 0;border-bottom:1px solid rgba(0,0,0,0.08);align-items:start;transition:var(--transition)}
    .value-item:hover{background:var(--color-gray-light);padding-left:20px;padding-right:20px;margin:0 -20px}
    .value-num{font-size:13px;font-weight:700;color:var(--color-blue);font-family:var(--font-en);padding-top:4px}
    .value-title{font-size:22px;font-weight:700}
    .value-title small{display:block;font-size:12px;letter-spacing:3px;color:var(--color-gray-mid);font-weight:400;margin-top:4px;font-family:var(--font-en)}
    .value-text{font-size:14px;color:var(--color-gray-mid);line-height:1.9}

    .products-intro{padding:80px 5%;background:var(--color-white)}
    .products-intro-inner{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:flex-end;gap:40px}
    .products-filter{display:flex;gap:8px;flex-wrap:wrap}
    .filter-btn{padding:8px 20px;font-size:12px;letter-spacing:1px;border:1px solid rgba(0,0,0,0.15);background:transparent;cursor:pointer;transition:var(--transition);font-family:var(--font-cn)}
    .filter-btn.active,.filter-btn:hover{background:var(--color-black);color:var(--color-white);border-color:var(--color-black)}
    .filter-cat-count{display:inline-block;background:rgba(0,0,0,0.06);color:var(--color-gray-mid);font-size:10px;padding:2px 6px;border-radius:10px;margin-left:6px;font-family:var(--font-en)}
    .filter-btn.active .filter-cat-count{background:rgba(255,255,255,0.2);color:var(--color-white)}

    .products-full-grid{padding:0 5% 100px;background:var(--color-white)}
    .products-full-grid-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
    .product-full-card{background:var(--color-white);border:1px solid rgba(0,0,0,0.06);overflow:hidden;transition:var(--transition);cursor:pointer}
    .product-full-card:hover{border-color:var(--color-black);transform:translateY(-4px);box-shadow:0 20px 60px rgba(0,0,0,0.1)}
    .product-full-visual{height:240px;background:var(--color-gray-light);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
    .product-full-visual img{width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply}

    .product-full-info{padding:20px}
    .product-full-cat{font-size:10px;letter-spacing:2px;color:var(--color-blue);text-transform:uppercase;font-family:var(--font-en);margin-bottom:8px}
    .product-full-name{font-size:16px;font-weight:600;margin-bottom:8px}
    .product-full-desc{font-size:12px;color:var(--color-gray-mid);line-height:1.6;margin-bottom:12px}
    .product-full-features{display:flex;gap:6px;flex-wrap:wrap}
    .feature-tag{font-size:10px;padding:3px 8px;background:var(--color-gray-light);color:var(--color-gray-dark)}
    .product-detail-toggle{display:flex;align-items:center;gap:8px;margin-top:16px;cursor:pointer;color:var(--color-blue);font-size:12px;letter-spacing:1px;transition:color 0.2s}
    .product-detail-toggle:hover{color:var(--color-black)}
    .toggle-icon{font-size:16px;font-weight:700;line-height:1;transition:transform 0.2s;flex-shrink:0}
    .product-detail-panel{max-height:0;overflow:hidden;transition:max-height 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)}
    .product-detail-panel.open{max-height:600px}
    .detail-label{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--color-gray-mid);margin-bottom:8px;font-family:var(--font-en);margin-top:12px}
    .detail-content{font-size:12px;color:var(--color-gray-dark);line-height:1.8;padding:16px;background:var(--color-gray-light);border-radius:0 0 12px 12px}
    .detail-content .detail-item{display:flex;padding:8px 0;border-bottom:1px solid rgba(0,0,0,0.06)}
    .detail-content .detail-item:last-child{border-bottom:none}
    .detail-content .detail-label{font-weight:600;color:var(--color-black);min-width:80px;flex-shrink:0}
    .detail-content .detail-value{color:var(--color-gray-dark)}
    .detail-content .detail-highlight{background:linear-gradient(135deg,var(--color-blue) 0%,#1a1a2e 100%);color:#fff;padding:12px;border-radius:8px;margin-top:12px}
    .detail-content .detail-highlight .detail-label{color:rgba(255,255,255,0.7)}
    .detail-content .detail-highlight .detail-value{color:#fff;font-weight:600}

    .why-choose{padding:100px 5%;background:var(--color-black)}
    .why-choose-inner{max-width:1200px;margin:0 auto}
    .why-choose-header{margin-bottom:64px}
    .why-choose-header .section-label{color:rgba(255,255,255,0.4)}
    .why-choose-header .section-title{color:var(--color-white)}
    .why-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:2px;background:rgba(255,255,255,0.05)}
    .why-item{background:var(--color-black);padding:48px;display:flex;gap:24px;transition:var(--transition)}
    .why-item:hover{background:rgba(255,255,255,0.04)}
    .why-item-num{font-size:48px;font-weight:800;color:rgba(255,255,255,0.06);font-family:var(--font-en);line-height:1;flex-shrink:0}
    .why-item-title{font-size:18px;font-weight:600;color:var(--color-white);margin-bottom:12px}
    .why-item-text{font-size:14px;color:rgba(255,255,255,0.5);line-height:1.8}

    .contact-section{padding:100px 5%;background:var(--color-white)}
    .contact-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px}
    .contact-info-label{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-gray-mid);margin-bottom:20px;font-family:var(--font-en)}
    .contact-info-title{font-size:clamp(28px,3vw,44px);font-weight:700;line-height:1.15;margin-bottom:24px}
    .contact-info-text{font-size:15px;color:var(--color-gray-mid);line-height:1.8;margin-bottom:48px}
    .contact-details{display:flex;flex-direction:column;gap:0;border-top:1px solid rgba(0,0,0,0.08)}
    .contact-detail-item{display:flex;gap:20px;padding:24px 0;border-bottom:1px solid rgba(0,0,0,0.08);align-items:flex-start}
    .contact-detail-icon{width:40px;height:40px;background:var(--color-gray-light);display:flex;align-items:center;justify-content:center;flex-shrink:0;border-radius:2px}
    .contact-detail-icon svg{width:18px;height:18px;stroke:var(--color-black);fill:none;stroke-width:1.5}
    .contact-detail-label{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--color-gray-mid);font-family:var(--font-en);margin-bottom:4px}
    .contact-detail-value{font-size:15px;color:var(--color-black);font-weight:500}

    .contact-form-title{font-size:24px;font-weight:700;margin-bottom:32px}
    .form-group{margin-bottom:24px}
    .form-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .form-label{display:block;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--color-gray-mid);font-family:var(--font-en);margin-bottom:10px}
    .form-input,.form-select,.form-textarea{width:100%;padding:14px 16px;border:1px solid rgba(0,0,0,0.12);background:var(--color-white);font-family:var(--font-cn);font-size:14px;color:var(--color-black);outline:none;transition:var(--transition);border-radius:0;-webkit-appearance:none}
    .form-input:focus,.form-select:focus,.form-textarea:focus{border-color:var(--color-black)}
    .form-textarea{height:140px;resize:vertical}
    .form-submit{width:100%;padding:16px;background:var(--color-black);color:var(--color-white);font-size:13px;letter-spacing:3px;text-transform:uppercase;font-family:var(--font-cn);border:none;cursor:pointer;transition:var(--transition)}
    .form-submit:hover{background:var(--color-blue)}
    .form-success{display:none;text-align:center;padding:40px;background:var(--color-gray-light)}
    .form-success.show{display:block}
    .form-success-icon{width:60px;height:60px;background:var(--color-black);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 20px}
    .form-success-icon svg{width:28px;height:28px;stroke:white;fill:none;stroke-width:2}
    .form-success-title{font-size:20px;font-weight:700;margin-bottom:8px}
    .form-success-text{font-size:14px;color:var(--color-gray-mid)}

    .map-section{padding:0 5% 100px;background:var(--color-white)}
    .map-inner{max-width:1200px;margin:0 auto}
    .map-placeholder{height:400px;background:var(--color-gray-light);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
    .map-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,0.04) 1px,transparent 1px);background-size:40px 40px}
    .map-pin{position:relative;z-index:1;text-align:center}
    .map-pin-dot{width:16px;height:16px;background:var(--color-blue);border-radius:50%;margin:0 auto 8px;position:relative}
    .map-pin-dot::after{content:"";position:absolute;inset:-6px;border:2px solid rgba(0,117,179,0.3);border-radius:50%;animation:ping 2s ease-in-out infinite}
    @keyframes ping{0%{transform:scale(1);opacity:1}100%{transform:scale(2);opacity:0}}
    .map-pin-label{font-size:13px;font-weight:600;background:var(--color-white);padding:8px 16px;box-shadow:0 4px 20px rgba(0,0,0,0.1)}

    .footer{background:var(--color-black);padding:80px 5% 40px}
    .footer-inner{max-width:1200px;margin:0 auto}
    .footer-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:60px;padding-bottom:60px;border-bottom:1px solid rgba(255,255,255,0.08)}
    .footer-logo{display:flex;align-items:center;gap:12px;margin-bottom:20px}
    .footer-logo-mark{width:40px;height:40px;background:var(--color-white);display:flex;align-items:center;justify-content:center;border-radius:2px}
    .footer-logo-mark span{font-size:16px;font-weight:700;letter-spacing:2px;color:var(--color-black);font-family:var(--font-en)}
    .footer-brand-name{font-size:16px;font-weight:700;color:var(--color-white)}
    .footer-brand-text{font-size:13px;color:rgba(255,255,255,0.4);line-height:1.8;margin-bottom:32px}
    .footer-col-title{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:24px;font-family:var(--font-en)}
    .footer-links{display:flex;flex-direction:column;gap:14px}
    .footer-links a{font-size:14px;color:rgba(255,255,255,0.6);transition:var(--transition)}
    .footer-links a:hover{color:var(--color-white)}
    .footer-bottom{display:flex;justify-content:space-between;align-items:center;padding-top:40px;gap:20px;flex-wrap:wrap}
    .footer-copyright{font-size:12px;color:rgba(255,255,255,0.3);letter-spacing:0.5px}
    .footer-icp{font-size:12px;color:rgba(255,255,255,0.3)}

    .mobile-menu{display:none;position:fixed;top:var(--nav-height);left:0;right:0;background:var(--color-white);padding:24px 5%;border-top:1px solid rgba(0,0,0,0.08);z-index:999;box-shadow:0 20px 40px rgba(0,0,0,0.1)}
    .mobile-menu.open{display:flex;flex-direction:column;gap:4px}
    .mobile-menu a{padding:14px 0;font-size:16px;color:var(--color-gray-dark);border-bottom:1px solid rgba(0,0,0,0.06);transition:var(--transition)}
    .mobile-menu a:last-child{border-bottom:none}
    .mobile-menu a:hover{color:var(--color-black);padding-left:8px}

    .fade-in{opacity:0;transform:translateY(30px);transition:opacity 0.7s ease,transform 0.7s ease}
    .fade-in.visible{opacity:1;transform:translateY(0)}
    .fade-in-delay-1{transition-delay:0.1s}
    .fade-in-delay-2{transition-delay:0.2s}
    .fade-in-delay-3{transition-delay:0.3s}

    @media(max-width:1200px){.products-full-grid-inner{grid-template-columns:repeat(3,1fr)}}
    @media(max-width:1024px){
      .stats-grid{grid-template-columns:repeat(2,1fr)}
      .features-grid,.products-grid{grid-template-columns:repeat(2,1fr)}
      .product-card.large{grid-row:auto}
      .brand-story-inner,.about-intro-inner{grid-template-columns:1fr}
      .about-intro-sticky{position:static}
      .mvv-grid,.why-grid,.contact-inner{grid-template-columns:1fr}
      .value-item{grid-template-columns:60px 1fr}
      .value-title{grid-column:2}
      .value-text{grid-column:1/-1}
      .products-full-grid-inner{grid-template-columns:repeat(2,1fr)}
      .footer-top{grid-template-columns:1fr 1fr}
    }
    @media(max-width:768px){
      .nav-links{display:none}.nav-hamburger{display:flex}
      .features-grid,.products-grid,.products-full-grid-inner,.footer-top{grid-template-columns:1fr}
      .form-row{grid-template-columns:1fr}
      .footer-top{gap:40px}
      .footer-bottom{flex-direction:column;align-items:flex-start}
      .products-intro-inner{flex-direction:column}
    }

    /* ITO CARE Service Styles */
    .nav-links a.care-link{color:var(--color-care-green);font-weight:500}
    .nav-links a.care-link::after{background:var(--color-care-green)}
    .nav-links a.care-link:hover{color:var(--color-care-green)}
    .care-section{background:var(--color-black);padding:120px 5%;position:relative;overflow:hidden}
    .care-section::before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,var(--color-black) 0%,#1a3a1a 50%,var(--color-black) 100%);}
    .care-section-inner{max-width:1200px;margin:0 auto;position:relative;z-index:2}
    .care-hero{display:grid;grid-template-columns:1.2fr 1fr;gap:80px;align-items:center;margin-bottom:80px}
    .care-hero-content{}
    .care-hero-label{display:inline-flex;align-items:center;gap:12px;font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-care-green);margin-bottom:24px;font-family:var(--font-en)}
    .care-hero-label::before{content:"";width:40px;height:1px;background:var(--color-care-green)}
    .care-hero-title{font-size:clamp(36px,4vw,56px);font-weight:700;color:var(--color-white);line-height:1.15;letter-spacing:-1px;margin-bottom:24px}
    .care-hero-title em{font-style:normal;color:var(--color-care-green)}
    .care-hero-desc{font-size:15px;color:rgba(255,255,255,0.6);line-height:1.8;margin-bottom:32px;font-weight:300}
    .care-hero-actions{display:flex;gap:16px;flex-wrap:wrap}
    .btn-care-ghost{background:transparent;color:var(--color-white);border:1px solid rgba(255,255,255,0.3)}
    .btn-care-ghost:hover{border-color:var(--color-care-green);background:rgba(46,125,50,0.2)}
    .care-hero-visual{position:relative}
    .care-hero-box{background:linear-gradient(135deg,rgba(46,125,50,0.15) 0%,rgba(46,125,50,0.05) 100%);border:1px solid rgba(46,125,50,0.3);padding:48px;border-radius:4px;position:relative;overflow:hidden}
    .care-hero-box::before{content:"360";position:absolute;top:-20px;right:-20px;font-size:100px;font-weight:800;color:rgba(46,125,50,0.1);font-family:var(--font-en);line-height:1}
    .care-hero-box .care-icon{width:64px;height:64px;background:var(--color-care-green);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px}
    .care-hero-box .care-icon svg{width:32px;height:32px;stroke:var(--color-white);fill:none;stroke-width:1.5}
    .care-hero-box h3{font-size:22px;font-weight:700;color:var(--color-white);margin-bottom:12px}
    .care-hero-box p{font-size:14px;color:rgba(255,255,255,0.6);line-height:1.7}
    .care-warranty-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;background:rgba(255,255,255,0.05)}
    .care-warranty-item{background:var(--color-black);padding:40px 24px;text-align:center;transition:var(--transition);border:1px solid transparent}
    .care-warranty-item:hover{border-color:var(--color-care-green);background:rgba(46,125,50,0.1)}
    .care-warranty-years{font-size:48px;font-weight:800;color:var(--color-care-green);font-family:var(--font-en);line-height:1;margin-bottom:8px}
    .care-warranty-years span{font-size:20px}
    .care-warranty-product{font-size:15px;font-weight:600;color:var(--color-white);margin-bottom:4px}
    .care-warranty-range{font-size:11px;color:rgba(255,255,255,0.4);letter-spacing:1px}
    .care-warranty-badge{display:inline-block;background:var(--color-care-green);color:var(--color-white);font-size:9px;padding:3px 10px;border-radius:20px;margin-top:12px;letter-spacing:1px}

    .care-services{padding:100px 5%;background:var(--color-white)}
    .care-services-inner{max-width:1200px;margin:0 auto}
    .care-services-header{margin-bottom:64px;text-align:center}
    .care-services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
    .care-service-card{background:var(--color-white);border:1px solid rgba(0,0,0,0.08);padding:40px;transition:var(--transition)}
    .care-service-card:hover{border-color:var(--color-care-green);transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,0,0,0.08)}
    .care-service-icon{width:56px;height:56px;background:var(--color-care-light);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:24px}
    .care-service-icon svg{width:28px;height:28px;stroke:var(--color-care-green);fill:none;stroke-width:1.5}
    .care-service-title{font-size:20px;font-weight:700;margin-bottom:12px}
    .care-service-desc{font-size:14px;color:var(--color-gray-mid);line-height:1.8;margin-bottom:20px}
    .care-service-highlight{background:var(--color-care-light);padding:16px;border-radius:4px}
    .care-service-highlight p{font-size:13px;color:var(--color-care-green);font-weight:500;margin:0}

    .care-products{padding:100px 5%;background:var(--color-gray-light)}
    .care-products-inner{max-width:1200px;margin:0 auto}
    .care-products-header{margin-bottom:48px}
    .care-products-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
    .care-product-card{background:var(--color-white);border:1px solid rgba(0,0,0,0.06);overflow:hidden;transition:var(--transition)}
    .care-product-card:hover{border-color:var(--color-care-green);transform:translateY(-4px)}
    .care-product-visual{height:180px;background:var(--color-white);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;border-bottom:1px solid rgba(0,0,0,0.04)}
    .care-product-visual img{width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply}
    .care-product-info{padding:16px}

    .care-product-name{font-size:14px;font-weight:600;margin-bottom:4px}
    .care-product-series{font-size:11px;color:var(--color-care-green);letter-spacing:1px;font-family:var(--font-en)}
    .care-product-warranty{font-size:11px;color:var(--color-gray-mid);margin-top:8px}

    .care-cta{background:var(--color-black);padding:100px 5%;text-align:center;position:relative;overflow:hidden}
    .care-cta::before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,var(--color-black) 0%,#1a3a1a 50%,var(--color-black) 100%);}
    .care-cta-inner{max-width:800px;margin:0 auto;position:relative;z-index:2}
    .care-cta-title{font-size:clamp(32px,4vw,48px);font-weight:700;color:var(--color-white);margin-bottom:24px}
    .care-cta-title em{color:var(--color-care-green);font-style:normal}
    .care-cta-desc{font-size:16px;color:rgba(255,255,255,0.6);margin-bottom:40px;line-height:1.8}
    .care-cta-btn{display:inline-flex;align-items:center;gap:12px;padding:18px 48px;font-size:14px;letter-spacing:2px;font-weight:500;background:var(--color-care-green);color:var(--color-white);border:none;cursor:pointer;transition:var(--transition);font-family:var(--font-cn);border-radius:2px}
    .care-cta-btn:hover{background:#1B5E20;transform:translateY(-2px)}
    .care-cta-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2}

    @media(max-width:1024px){
      .care-hero{grid-template-columns:1fr}
      .care-warranty-grid{grid-template-columns:repeat(2,1fr)}
      .care-services-grid{grid-template-columns:1fr}
      .care-products-grid{grid-template-columns:repeat(2,1fr)}
    }
    @media(max-width:768px){
      .care-warranty-grid,.care-products-grid{grid-template-columns:1fr}
    }
  </style>
</head>
<body>
'''

HTML_TAIL = '''
</body>
</html>'''

products = [
    # CLASSIC系列
    {'id': 'classic-wave-2025', 'name': 'CLASSIC WAVE 2025', 'cn': '经典波浪2025新色', 'cat': 'luggage', 'series': 'CLASSIC', 'key': 'CLASSICWAVE2025新色', 'desc': '2025全新色彩版本，波浪纹路经典设计，延续东西方美学的融合，春夏清新配色。', 'tags': ['2025新色', '波浪设计', '限量色系'], 'detail': '材质：100% PC材质 | 颜色：珊红/春绿/青蓝/墨灰 | 全体尺寸：525×365×240mm(20寸)/665×445×275mm(25寸)/755×530×295mm(29寸) | 容积：42L/75L/116L | 重量：3.0kg(20寸)/4.0kg(25寸)/5.0kg(29寸) | 售价：20寸 ￥898 / 25寸 ￥998 / 29寸 ￥1098 | 卖点：波浪纹路设计 + 2025春夏限定四色 + 轻盈坚固PC材质'},
    # PISTACHIO系列
    {'id': 'pistachio-striped', 'name': 'PISTACHIO STRIPED', 'cn': '开心果条纹行李箱', 'cat': 'luggage', 'series': 'PISTACHIO', 'key': 'PISTACHIOSTRIPED', 'desc': 'PISTACHIO条纹系列，经典条纹设计搭配PEBBLE圆锁设计，荣获德国IF设计大奖，质感与功能兼备。', 'tags': ['条纹设计', 'PEBBLE圆锁', 'IF设计奖'], 'detail': '材质：100% PC材质 + PEBBLE圆锁 | 颜色：烟白/森绿/炭黑 | 全体尺寸：565×360×210mm(20寸)/670×440×260mm(24寸)/780×520×280mm(28寸) | 容积：37L/62L/99L | 重量：2.7kg(20寸)/3.4kg(24寸)/4.5kg(28寸) | 售价：20寸 ￥1098 / 24寸 ￥1398 / 28寸 ￥1698 | 卖点：德国IF设计大奖 + PEBBLE圆锁设计 + 经典条纹美学'},
    {'id': 'pistachio-2-striped', 'name': 'PISTACHIO 2 STRIPED', 'cn': '开心果2条纹行李箱', 'cat': 'luggage', 'series': 'PISTACHIO', 'key': 'PISTACHIO2STRIPED', 'desc': 'PISTACHIO条纹系列新一代，升级版设计语言，延续经典条纹元素，荣获德国IF设计大奖。', 'tags': ['条纹设计', '升级版', 'IF设计奖'], 'detail': '材质：100% PC材质 | 颜色：梦境粉/平原灰/数字紫/冷血绿 | 全体尺寸：565×360×210mm(20寸)/670×440×260mm(24寸)/780×520×280mm(28寸) | 容积：37L/62L/99L | 重量：2.8kg(20寸)/3.6kg(24寸)/4.5kg(28寸) | 售价：20寸 ￥1390 / 24寸 ￥1690 / 28寸 ￥1990 | 卖点：德国IF设计大奖 + 升级版条纹设计 + 三种尺寸可选'},
    {'id': 'pistachio-2-striped-trunk', 'name': 'PISTACHIO 2 STRIPED TRUNK', 'cn': '开心果2条纹服饰箱', 'cat': 'luggage', 'series': 'PISTACHIO', 'key': 'PISTACHIO2STRIPEDTRUNK', 'desc': 'PISTACHIO条纹系列服饰箱，特别设计的挂衣舱，保持西装礼服平整，适合商务出差，荣获德国IF设计大奖。', 'tags': ['挂衣设计', '防皱保护', '商务出行'], 'detail': '材质：100% PC材质 + PEBBLE圆锁 | 颜色：梦境粉/平原灰/数字紫/冷血绿 | 全体尺寸：640×360×330mm(22寸)/730×380×370mm(26寸)/800×380×400mm(30寸) | 容积：56L/77L/112L | 重量：3.6kg(22寸)/4.2kg(26寸)/4.9kg(30寸) | 售价：22寸 ￥1690 / 26寸 ￥1990 / 30寸 ￥2290 | 卖点：德国IF设计大奖 + 特别挂衣舱设计 + 保持西装礼服平整'},
    {'id': 'pistachio-2-striped-2026-limited', 'name': 'PISTACHIO 2 STRIPED 2026 S/S Limited', 'cn': '开心果2条纹2026季节限量版', 'cat': 'luggage', 'series': 'PISTACHIO', 'key': 'PISTACHIO2STRIPED2026SSLimitedEdition', 'desc': '2026春夏限定三色：气泡粉/波子绿/苏打橙。荣获德国IF设计大奖，全新PEBBLE翻盖锁，轻至2.9kg。', 'tags': ['季节限量', 'IF设计奖', '春夏限定三色'], 'detail': '材质：100%全新PC材质 + PEBBLE翻盖锁(内置海关锁) | 颜色：气泡粉/波子绿/苏打橙 | 全体尺寸：555×330×265mm(20寸)/730×380×370mm(26寸)/800×380×400mm(30寸) | 容积：42L/77L/112L | 重量：2.9kg(20寸)/4.2kg(26寸)/4.9kg(30寸) | 售价：20寸 ￥1590 / 26寸 ￥1990 / 30寸 ￥2290 | 卖点：德国IF设计大奖 + 春夏限定三色 + 全新PEBBLE翻盖锁'},
    # GINKGO系列
    {'id': 'ginkgo-4-striped', 'name': 'GINKGO 4 STRIPED', 'cn': '银杏4条纹行李箱', 'cat': 'luggage', 'series': 'GINKGO', 'key': 'GINKGO4STRIPED10.23', 'desc': 'ITO全新推出银杏系列旅行箱，斜纹设计呼应细节，重塑东方美学。三种色彩钴蓝、赭红、砾灰。', 'tags': ['条纹设计', '东方美学', '三色可选'], 'detail': '材质：100% PC材质 | 颜色：钴蓝/赭红/砾灰 | 全体尺寸：570×365×215mm(20寸)/735×415×335mm(26寸)/785×445×350mm(30寸) | 容积：35L/79L/103L | 重量：4.0kg(20寸)/5.4kg(26寸)/6.2kg(30寸) | 售价：20寸 ￥2990 / 26寸 ￥3990 / 30寸 ￥4990 | 卖点：斜纹设计呼应细节 + 钴蓝/赭红/砾灰三色 + 重塑东方美学'},
    # 双肩背包系列
    {'id': 'porcini-backpack', 'name': 'PORCINI BACKPACK', 'cn': '波奇尼双肩背包', 'cat': 'backpack', 'series': 'PORCINI', 'key': 'PORCINIBACKPACK', 'desc': 'PORCINI系列双肩背包，采用camira羊毛面料，90%羊毛含量，防泼水设计，适合城市通勤与旅行。', 'tags': ['camira面料', '双肩设计', '防泼水'], 'detail': '材质：camira羊毛面料(90%羊毛含量) + Teflon三防涂层 | 颜色：暮棕/绯杏 | 尺寸：410×290×140mm(16L)/440×310×150mm(20L) | 全体尺寸：490×320×160mm | 容积：16L/20L | 重量：1.1kg(16L)/1.2kg(20L) | 售价：16L ￥1890 / 20L ￥2190 | 卖点：camira面料90%羊毛 + Teflon三防 + 7A抗菌里布 + RFID防伪标'},
    {'id': 'truffle-backpack-2', 'name': 'TRUFFLE BACKPACK 2', 'cn': '松露双肩背包2', 'cat': 'backpack', 'series': 'TRUFFLE', 'key': 'TRUFFLEBACKPACK2', 'desc': 'TRUFFLE新一代双肩背包，全新升级设计语言，更优化的背负系统与收纳空间。', 'tags': ['升级版', '人体工学', '全新设计'], 'detail': '材质：camira羊毛面料(90%羊毛含量) + Teflon三防涂层 | 颜色：岩白/松褐/黛蓝/稻黄 | 尺寸：420×300×130mm(12L)/460×330×150mm(18L) | 全体尺寸：490×320×160mm | 容积：12L/18L | 重量：0.67kg(12L)/0.77kg(18L) | 售价：12L ￥798 / 18L ￥998 | 卖点：全新升级设计语言 + 更优化的背负系统与收纳空间'},
    {'id': 'truffle-travel-backpack', 'name': 'TRUFFLE TRAVEL BACKPACK', 'cn': '松露旅行双肩背包', 'cat': 'backpack', 'series': 'TRUFFLE', 'key': 'TRUFFLETRAVELBACKPACK', 'desc': 'TRUFFLE旅行版背包，专为旅行设计，大容量主仓，隐藏防盗口袋，可扩展设计。', 'tags': ['旅行设计', '防盗口袋', '可扩展'], 'detail': '材质：camira羊毛面料(90%羊毛含量) + Teflon三防涂层 | 颜色：霜地白/远山绿/海隅黑 | 尺寸：470×350×150mm | 全体尺寸：490×320×160mm | 容积：16L | 重量：0.91kg | 售价：￥1190 | 卖点：隐藏防盗口袋 + 可扩展设计 + 专为旅行设计'},
    {'id': 'mycena-backpack-2026', 'name': 'MYCENA BACKPACK LITE', 'cn': '伞菌折叠双肩背包', 'cat': 'backpack', 'series': 'MYCENA', 'key': 'MYCENABACKPACK2026', 'desc': 'ITO FUNGI系列小伞菌折叠双肩包，以「收」为留白，以「展」为表达。户外随行，无拘无束。可折叠设计，自重仅0.32kg。', 'tags': ['FUNGI系列', '可折叠', 'CORDURA面料'], 'detail': '材质：CORDURA® Naturalle升级面料(耐磨抗撕裂) + Teflon三防涂层 | 颜色：羽白/芽绿/瑾紫/晴蓝/屿灰 | 尺寸：480×280×110mm | 全体尺寸：300×220×140mm | 容积：15L | 重量：仅0.32kg | 售价：￥590 | 卖点：可折叠设计 + CORDURA面料 + RFID防伪标 + 荣获设计大奖'},
    {'id': 'pistachio-backpack', 'name': 'PISTACHIO BACKPACK', 'cn': '开心果双肩背包', 'cat': 'backpack', 'series': 'PISTACHIO', 'key': 'PISTACHIOBACKPACK', 'desc': 'PISTACHIO系列双肩背包，NUTS系列设计语言，帆布与皮革结合，时尚与功能兼备。', 'tags': ['帆布皮革', '城市通勤', '多隔层'], 'detail': '材质：帆布与皮革结合 + PC硬壳保护 | 颜色：烟白/炭黑/枣红 | 尺寸：370×290×130mm | 全体尺寸：490×320×160mm | 容积：6L | 重量：1.2kg | 售价：￥1390 | 卖点：帆布皮革结合 + NUTS设计语言 + 多隔层收纳'},
    {'id': 'porcini-tote', 'name': 'PORCINI TOTE', 'cn': '波奇尼托特手提袋', 'cat': 'backpack', 'series': 'PORCINI', 'key': 'PORCINITOTE', 'desc': 'PORCINI托特手提袋，TIMELESS经典设计，camira羊毛面料，90%羊毛含量，防泼水耐用。', 'tags': ['托特设计', 'camira面料', '经典永恒'], 'detail': '材质：camira羊毛面料(90%羊毛含量) + Teflon三防涂层 | 颜色：暮棕/绯杏 | 尺寸：430×310×140mm | 全体尺寸：490×320×160mm | 容积：14L | 重量：1.0kg | 售价：￥1890 | 卖点：TIMELESS经典设计 + 7A抗菌里布 + 适合搭配旅行箱'},
    # 旅行袋系列
    {'id': 'chanterelle-duffle-2', 'name': 'CHANTERELLE DUFFLE BAG 2', 'cn': '金针菇旅行袋2', 'cat': 'bag', 'series': 'CHANTERELLE', 'key': 'CHANTERELLEDUFFLEBAG2', 'desc': 'CHANTERELLE新一代旅行袋，1+1双隔层设计理念，camira面料100,000次耐磨认证。', 'tags': ['双隔层', 'camira面料', '升级版'], 'detail': '材质：camira面料(100,000次耐磨认证) + Teflon三防涂层 + 7A抗菌里布 | 颜色：黛蓝/岩白/蜡粉 | 尺寸：300×150×140mm(6L)/400×200×200mm(16L)/450×255×190mm(20L) | 全体尺寸：495×320×155mm(6L)/500×320×220mm(16L/20L) | 容积：6L/16L/20L | 重量：0.52kg(6L)/0.65kg(16L)/0.85kg(20L) | 售价：6L ￥690 / 16L ￥990 / 20L ￥1190 | 卖点：1+1双隔层设计 + 100,000次耐磨认证 + 三色可选'},
    {'id': 'mushroom-organizer-2-no-care', 'name': 'MUSHROOM ORGANIZER 2', 'cn': '蘑菇收纳包2', 'cat': 'bag', 'series': 'MUSHROOM', 'key': 'MUSHROOMORGANIZER2', 'no_care': True, 'desc': 'MUSHROOM收纳包第二代，升级版分区设计，85%尼龙+15%涤纶面料，适合搭配TRUNK行李箱使用。', 'tags': ['升级版', 'TRUNK搭配', '便携收纳'], 'detail': '材质：85%尼龙+15%涤纶面料 + 抗菌面料 | 颜色：轻石白/橡木灰/冰川蓝/网球绿 | 尺寸：200×130×90mm(2L)/200×180×130mm(4L)/310×130×130mm(5L)/310×230×130mm(9L)/360×310×130mm(14L) | 全体尺寸：490×320×160mm | 容积：2L/4L/5L/9L/14L | 重量：0.10kg(2L)/0.14kg(4L)/0.23kg(5L)/0.31kg(9L)/0.41kg(14L) | 售价：2L-4L ￥490 / 5L-14L ￥650 | 卖点：升级版分区设计 + 抗菌面料'},
]

def get_img(key):
    if key in imgs:
        return f"data:image/png;base64,{imgs[key]}"
    return ''

def get_warranty_years(series):
    """根据产品系列返回保修年限"""
    warranty_map = {
        'GINKGO': '10年保修',
        'PISTACHIO': '5年保修',
        'CLASSIC': '2年保修',
        'PORCINI': '5年保修',
        'TRUFFLE': '5年保修',
        'MYCENA': '5年保修',
        'CHANTERELLE': '5年保修',
        'MUSHROOM': '5年保修',
    }
    return warranty_map.get(series, '2年保修')

def get_care_label(series):
    """根据产品系列返回换新天数"""
    if series == 'GINKGO':
        return '720天换新'
    return '360天换新'

def format_detail(detail_str):
    """将详情字符串格式化为HTML表格"""
    if not detail_str:
        return ''
    items = detail_str.split(' | ')
    html = ''
    for item in items:
        if '：' in item:
            label, value = item.split('：', 1)
            html += f'<div class="detail-item"><span class="detail-label">{label}</span><span class="detail-value">{value}</span></div>\n'
    return html

cat_labels = {'luggage': '行李箱', 'backpack': '背包', 'bag': '旅行袋'}
cat_tags = {'luggage': 'LUGGAGE', 'backpack': 'BACKPACK', 'bag': 'TRAVEL BAG'}

# Generate product cards
product_cards_html = ''
for i, p in enumerate(products):
    delays = ['', 'fade-in-delay-1', 'fade-in-delay-2', 'fade-in-delay-3']
    delay = delays[i % 4]
    img_src = get_img(p['key'])
    tag_class = 'blue' if p['cat'] == 'backpack' else ''
    tag_text = cat_tags[p['cat']]
    features_html = ''.join([f'<span class="feature-tag">{t}</span>' for t in p['tags']])
    detail_html = format_detail(p.get('detail', ''))
    warranty_years = get_warranty_years(p['series'])
    care_label = get_care_label(p['series'])
    
    card = '<div class="product-full-card fade-in ' + delay + '" data-cat="' + p['cat'] + '" data-series="' + p['series'] + '">'
    card += '<div class="product-full-visual">'
    card += '<img src="' + img_src + '" alt="' + p['name'] + '" loading="lazy">'
    card += '</div>'
    card += '<div class="product-full-info">'

    card += '<div class="product-full-cat">' + p['series'] + ' · ' + cat_labels[p['cat']] + '</div>'
    card += '<div class="product-full-name">' + p['name'] + '</div>'
    card += '<div class="product-full-desc">' + p['desc'] + '</div>'
    card += '<div class="product-full-features">' + features_html + '</div>'
    # 检查是否有 no_care 标记（用于 MUSHROOM ORGANIZER 2 等不需要显示 ITO CARE 标签的产品）
    if not p.get('no_care', False):
        card += '<div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap;">'
        card += '<span style="font-size:11px;padding:4px 10px;background:var(--color-care-light);color:var(--color-care-green);border-radius:2px;">' + care_label + '</span>'
        card += '<span style="font-size:11px;padding:4px 10px;background:var(--color-gray-light);color:var(--color-gray-dark);border-radius:2px;">' + warranty_years + '</span>'
        card += '</div>'
    card += '<div class="product-detail-toggle" onclick="toggleDetail(this)">'
    card += '<span class="toggle-icon">+</span>'
    card += '<span class="toggle-text">查看详细参数</span>'
    card += '</div>'
    card += '<div class="product-detail-panel">'
    card += '<div class="detail-label">产品详情</div>'
    card += '<div class="detail-content">' + detail_html + '</div>'
    card += '</div>'
    card += '</div>'
    card += '</div>'
    product_cards_html += card

nav = '''
  <nav class="nav" id="mainNav">
    <a href="#" class="nav-logo" onclick="showPage('home'); return false;">
      <div class="nav-logo-mark"><span>ITO</span></div>
      <div class="nav-logo-text">
        <span class="brand-en">ITO</span>
        <span class="brand-cn">伊稻（上海）商业有限公司</span>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="#" onclick="showPage('home'); return false;" id="nav-home" class="active">首页</a></li>
      <li><a href="#" onclick="showPage('products'); return false;" id="nav-products">产品中心</a></li>
      <li><a href="ito-care.html" id="nav-care" class="care-link">ITO CARE</a></li>
      <li><a href="#" onclick="showPage('about'); return false;" id="nav-about">关于我们</a></li>
      <li><a href="#" onclick="showPage('contact'); return false;" id="nav-contact" class="nav-cta">联系我们</a></li>
    </ul>
    <div class="nav-hamburger" id="hamburger" onclick="toggleMobileMenu()">
      <span></span><span></span><span></span>
    </div>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <a href="#" onclick="showPage('home'); toggleMobileMenu(); return false;">首页</a>
    <a href="#" onclick="showPage('products'); toggleMobileMenu(); return false;">产品中心</a>
    <a href="ito-care.html" onclick="toggleMobileMenu(); return false;">ITO CARE</a>
    <a href="#" onclick="showPage('about'); toggleMobileMenu(); return false;">关于我们</a>
    <a href="#" onclick="showPage('contact'); toggleMobileMenu(); return false;">联系我们</a>
  </div>
'''

home_page = f'''
  <div id="page-home" class="page active">
    <section class="hero">
      <div class="hero-grid-lines"></div>
      <div class="hero-bg-text">ITO</div>
      <div class="hero-content">
        <div class="hero-label">旅行箱包专业品牌</div>
        <h1 class="hero-title">探索世界<br>从<em>一件好箱</em>开始</h1>
        <p class="hero-desc">ITO 伊稻，专注于旅行箱包的设计与制造。<br>行李箱、背包、旅行袋——每一件产品，都是一次旅程的伙伴。</p>
        <div class="hero-actions">
          <a href="#" class="btn btn-white btn-arrow" onclick="showPage('products'); return false;">探索产品</a>
          <a href="#" class="btn btn-ghost" onclick="showPage('about'); return false;">了解品牌</a>
        </div>
      </div>
      <div class="hero-scroll">
        <div class="hero-scroll-line"></div>SCROLL
      </div>
    </section>

    <section class="stats-bar">
      <div class="stats-grid">
        <div class="stat-item fade-in">
          <div class="stat-number">15<span>+</span></div>
          <div class="stat-label">产品系列</div>
        </div>
        <div class="stat-item fade-in fade-in-delay-1">
          <div class="stat-number">28</div>
          <div class="stat-label">SKU 款式</div>
        </div>
        <div class="stat-item fade-in fade-in-delay-2">
          <div class="stat-number">100<span>万+</span></div>
          <div class="stat-label">消费者信赖</div>
        </div>
        <div class="stat-item fade-in fade-in-delay-3">
          <div class="stat-number">上海</div>
          <div class="stat-label">总部所在地</div>
        </div>
      </div>
    </section>

    <section class="features">
      <div class="features-header container fade-in">
        <div>
          <div class="section-label">Why ITO</div>
          <h2 class="section-title">品质，是我们的<br>核心承诺</h2>
        </div>
        <a href="#" class="btn btn-outline" onclick="showPage('about'); return false;">了解更多</a>
      </div>
      <div class="features-grid container">
        <div class="feature-card fade-in">
          <div class="feature-icon"><svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div>
          <div class="feature-num">01</div>
          <div class="feature-title">精选材质</div>
          <div class="feature-desc">严选航空级PC材质、camira羊毛面料等多种优质材料，每种材质均经严格测试，确保耐用与美观并存。</div>
        </div>
        <div class="feature-card fade-in fade-in-delay-1">
          <div class="feature-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
          <div class="feature-num">02</div>
          <div class="feature-title">专注设计</div>
          <div class="feature-desc">融合东西方美学，简洁现代的外观设计与人体工学内构相结合，满足现代旅行者对品质生活的追求。</div>
        </div>
        <div class="feature-card fade-in fade-in-delay-2">
          <div class="feature-icon"><svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
          <div class="feature-num">03</div>
          <div class="feature-title">品质保障</div>
          <div class="feature-desc">每件产品出厂前经历多道工序严格检验，我们以客户满意为最终标准，提供完善的售后服务体系。</div>
        </div>
      </div>
    </section>

    <section class="products-showcase">
      <div class="products-showcase-header fade-in">
        <div class="section-label">Our Products</div>
        <h2 class="section-title">旅行全品类，<br>伊稻都有</h2>
        <p class="section-subtitle">从商务出行到休闲旅游，从短途到长途，ITO 为每一种旅行方式提供合适的装备。</p>
      </div>
      <div class="products-grid container">
        <div class="product-card large fade-in" onclick="showPage('products'); return false;">
          <div class="product-card-inner">
            <div class="product-card-visual">
              <img src="{get_img('PISTACHIO2STRIPEDTRUNK')}" alt="行李箱" style="width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply;">
            </div>
            <div class="product-card-info">
              <div class="product-tag">LUGGAGE · 箱类</div>
              <div class="product-name">行李箱 / 手提箱 / 服装箱</div>
              <div class="product-desc">专为现代旅行者设计，PC材质轻盈坚固，PEBBLE圆锁极简仪式感，多色多尺寸可选。</div>
            </div>
          </div>
        </div>
        <div class="product-card fade-in fade-in-delay-1" onclick="showPage('products'); return false;">
          <div class="product-card-inner">
            <div class="product-card-visual">
              <img src="{get_img('TRUFFLEBACKPACK2')}" alt="双肩背包" style="width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply;">
            </div>
            <div class="product-card-info">
              <div class="product-tag">BACKPACK · 双肩背包</div>
              <div class="product-name">双肩背包</div>
              <div class="product-desc">camira面料，90%羊毛含量，防泼水设计，兼顾日常与旅行，收纳空间合理，背负舒适。</div>
            </div>
          </div>
        </div>
        <div class="product-card fade-in fade-in-delay-2" onclick="showPage('products'); return false;">
          <div class="product-card-inner">
            <div class="product-card-visual">
              <img src="{get_img('PORCINIBACKPACK')}" alt="波奇尼双肩背包" style="width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply;">
            </div>
            <div class="product-card-info">
              <div class="product-tag">BACKPACK · 双肩背包</div>
              <div class="product-name">波奇尼双肩背包</div>
              <div class="product-desc">camira羊毛面料，90%羊毛含量，Teflon三防涂层，7A抗菌里布，TIMELESS经典设计。</div>
            </div>
          </div>
        </div>
      </div>
      <div class="products-view-all fade-in">
        <a href="#" class="btn btn-primary btn-arrow" onclick="showPage('products'); return false;">查看全部产品</a>
      </div>
    </section>

    <section class="care-section">
      <div class="care-section-inner">
        <div class="care-hero fade-in">
          <div class="care-hero-content">
            <div class="care-hero-label">ITO CARE 服务体系</div>
            <h2 class="care-hero-title">让每一次旅行<br>都有<em>安心守护</em></h2>
            <p class="care-hero-desc">"ITO CARE"是ITO为用户提供便捷、可视的高品质服务品牌，服务涵盖360 CARE换新、2/5/10年免费保修、以旧换新等全生命周期的服务权益，始终以客户为导向，让信赖一路随行。</p>
            <div class="care-hero-actions">
              <a href="ito-care.html" class="btn btn-care btn-arrow">了解服务详情</a>
              <a href="#" class="btn btn-care-ghost" onclick="showPage('products'); return false;">查看支持产品</a>
            </div>
          </div>
          <div class="care-hero-visual">
            <div class="care-hero-box">
              <div class="care-icon">
                <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <h3>360 CARE</h3>
              <p>购买360天内（GINKGO系列720天）可享受一次免费换新服务</p>
            </div>
          </div>
        </div>
        <div class="care-warranty-grid">
          <div class="care-warranty-item fade-in">
            <div class="care-warranty-years">10<span>年</span></div>
            <div class="care-warranty-product">GINKGO 系列</div>
            <div class="care-warranty-range">高端定位 · 十年质保</div>
            <span class="care-warranty-badge">旗舰服务</span>
          </div>
          <div class="care-warranty-item fade-in fade-in-delay-1">
            <div class="care-warranty-years">5<span>年</span></div>
            <div class="care-warranty-product">PISTACHIO 系列</div>
            <div class="care-warranty-range">经典系列 · 五年质保</div>
            <span class="care-warranty-badge">长期保障</span>
          </div>
          <div class="care-warranty-item fade-in fade-in-delay-2">
            <div class="care-warranty-years">5<span>年</span></div>
            <div class="care-warranty-product">包袋系列</div>
            <div class="care-warranty-range">配饰系列 · 五年质保</div>
            <span class="care-warranty-badge">长期保障</span>
          </div>
          <div class="care-warranty-item fade-in fade-in-delay-3">
            <div class="care-warranty-years">2<span>年</span></div>
            <div class="care-warranty-product">CLASSIC 系列</div>
            <div class="care-warranty-range">入门系列 · 二年质保</div>
            <span class="care-warranty-badge">基础保障</span>
          </div>
        </div>
      </div>
    </section>

    <section class="brand-story">
      <div class="brand-story-inner container">
        <div>
          <div class="brand-story-label fade-in">Brand Story</div>
          <h2 class="brand-story-title fade-in">成为千万消费者<br>最值得信赖的<br>旅行品牌</h2>
          <p class="brand-story-text fade-in">伊稻（ITO），诞生于上海，专注于旅行箱包品类的深耕与创新。我们相信，每一次旅行都值得最好的装备，每一件产品都应当经得起时间的检验。</p>
          <p class="brand-story-text fade-in">从产品设计到材质工艺，从品质管控到服务体验，ITO 始终以消费者的真实需求为出发点，以创新为驱动，以卓越为目标。</p>
          <a href="#" class="btn btn-white fade-in" onclick="showPage('about'); return false;">了解品牌故事</a>
        </div>
        <div class="brand-story-visual fade-in">
          <div class="brand-story-box">
            <div class="brand-story-quote">为人们提供<em>喜欢、好用</em>的旅行产品，是我们永恒的使命。</div>
            <div class="brand-story-quote-author">ITO Brand Mission · 伊稻品牌使命</div>
          </div>
        </div>
      </div>
    </section>
  </div>
'''

care_page = '''
  <div id="page-care" class="page">
    <section class="care-section">
      <div class="hero-grid-lines"></div>
      <div class="care-section-inner">
        <div class="care-hero fade-in" style="grid-template-columns:1fr;">
          <div class="care-hero-content" style="text-align:center;">
            <div class="care-hero-label" style="justify-content:center;">ITO CARE 服务体系</div>
            <h2 class="care-hero-title" style="font-size:clamp(40px,5vw,72px);">让每一次旅行<br>都有<em>安心守护</em></h2>
            <p class="care-hero-desc" style="max-width:700px;margin:0 auto 40px;">"ITO CARE"是ITO为用户提供便捷、可视的高品质服务品牌，服务涵盖360 CARE换新、2/5/10年免费保修、以旧换新等全生命周期的服务权益，始终以客户为导向，让信赖一路随行。</p>
            <div class="care-hero-actions" style="justify-content:center;">
              <a href="#" class="btn btn-care btn-arrow" onclick="showPage('products'); return false;">探索支持产品</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="care-services">
      <div class="care-services-inner">
        <div class="care-services-header fade-in">
          <div class="section-label green">服务详情</div>
          <h2 class="section-title">全方位服务体系</h2>
          <p class="section-subtitle" style="max-width:600px;margin:16px auto 0;">覆盖产品全生命周期，从购买到使用，从保修到换新，提供一站式品质服务</p>
        </div>
        <div class="care-services-grid">
          <div class="care-service-card fade-in">
            <div class="care-service-icon">
              <svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
            </div>
            <h3 class="care-service-title">360 CARE 换新服务</h3>
            <p class="care-service-desc">在ITO官方渠道购买的ITO主线商品，自购买之日起360天内（GINKGO系列720天）可享受一次免费换新服务。</p>
            <div class="care-service-highlight">
              <p>信用换新 24h 内发出新品</p>
            </div>
          </div>
          <div class="care-service-card fade-in fade-in-delay-1">
            <div class="care-service-icon">
              <svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
            </div>
            <h3 class="care-service-title">免费保修服务</h3>
            <p class="care-service-desc">根据产品系列享受2年、5年或10年不限次数免费保修，涵盖轮子、拉杆、密码锁、把手、拉链等配件。</p>
            <div class="care-service-highlight">
              <p>GINKGO 10年 · PISTACHIO 5年 · CLASSIC 2年</p>
            </div>
          </div>
          <div class="care-service-card fade-in fade-in-delay-2">
            <div class="care-service-icon">
              <svg viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
            </div>
            <h3 class="care-service-title">以换代修服务</h3>
            <p class="care-service-desc">经工厂检测确认产品无法通过维修恢复功能时，提供以换代修服务，快速恢复使用。</p>
            <div class="care-service-highlight">
              <p>24h 内发出官翻品或同款新品</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="care-warranty-section" style="background:var(--color-gray-light);padding:100px 5%;">
      <div style="max-width:1200px;margin:0 auto;">
        <div style="margin-bottom:64px;">
          <div class="section-label fade-in">保修年限</div>
          <h2 class="section-title fade-in">按产品系列的保修政策</h2>
          <p class="section-subtitle fade-in">根据各产品系列定位，提供不同年限的免费保修服务</p>
        </div>
        <div class="care-warranty-grid fade-in">
          <div class="care-warranty-item">
            <div class="care-warranty-years">10<span>年</span></div>
            <div class="care-warranty-product">GINKGO 系列</div>
            <div class="care-warranty-range">高端定位 · 十年质保</div>
            <span class="care-warranty-badge">旗舰服务</span>
          </div>
          <div class="care-warranty-item">
            <div class="care-warranty-years">5<span>年</span></div>
            <div class="care-warranty-product">PISTACHIO 系列</div>
            <div class="care-warranty-range">经典系列 · 五年质保</div>
            <span class="care-warranty-badge">长期保障</span>
          </div>
          <div class="care-warranty-item">
            <div class="care-warranty-years">5<span>年</span></div>
            <div class="care-warranty-product">包袋系列</div>
            <div class="care-warranty-range">配饰系列 · 五年质保</div>
            <span class="care-warranty-badge">长期保障</span>
          </div>
          <div class="care-warranty-item">
            <div class="care-warranty-years">2<span>年</span></div>
            <div class="care-warranty-product">CLASSIC 系列</div>
            <div class="care-warranty-range">入门系列 · 二年质保</div>
            <span class="care-warranty-badge">基础保障</span>
          </div>
        </div>
      </div>
    </section>

    <section class="care-products">
      <div class="care-products-inner">
        <div class="care-products-header">
          <div class="section-label fade-in">支持 ITO CARE 的产品</div>
          <h2 class="section-title fade-in">全系列产品均享服务保障</h2>
          <p class="section-subtitle fade-in">点击下方产品，查看详细参数和保修信息</p>
        </div>
        <div class="care-products-grid">
          <div class="care-product-card fade-in" onclick="showPage('products'); return false;">
            <div class="care-product-visual">
              <img src="''' + get_img('PISTACHIOSTRIPED') + '''" alt="PISTACHIO STRIPED">
            </div>
            <div class="care-product-info">
              <div class="care-product-series">PISTACHIO · 行李箱</div>
              <div class="care-product-name">PISTACHIO STRIPED</div>
              <div class="care-product-warranty">5年免费保修</div>
            </div>
          </div>
          <div class="care-product-card fade-in" onclick="showPage('products'); return false;">
            <div class="care-product-visual">
              <img src="''' + get_img('PISTACHIO2STRIPEDTRUNK') + '''" alt="PISTACHIO 2 STRIPED TRUNK">
            </div>
            <div class="care-product-info">
              <div class="care-product-series">PISTACHIO · 行李箱</div>
              <div class="care-product-name">PISTACHIO 2 STRIPED TRUNK</div>
              <div class="care-product-warranty">5年免费保修</div>
            </div>
          </div>
          <div class="care-product-card fade-in" onclick="showPage('products'); return false;">
            <div class="care-product-visual">
              <img src="''' + get_img('GINKGO4STRIPED10.23') + '''" alt="GINKGO 4">
            </div>
            <div class="care-product-info">
              <div class="care-product-series">GINKGO · 行李箱</div>
              <div class="care-product-name">GINKGO 4</div>
              <div class="care-product-warranty">10年免费保修</div>
            </div>
          </div>
          <div class="care-product-card fade-in" onclick="showPage('products'); return false;">
            <div class="care-product-visual">
              <img src="''' + get_img('TRUFFLEBACKPACK2') + '''" alt="TRUFFLE BACKPACK 2">
            </div>
            <div class="care-product-info">
              <div class="care-product-series">TRUFFLE · 双肩背包</div>
              <div class="care-product-name">TRUFFLE BACKPACK 2</div>
              <div class="care-product-warranty">5年免费保修</div>
            </div>
          </div>
        </div>
        <div style="text-align:center;margin-top:48px;">
          <a href="#" class="btn btn-care btn-arrow fade-in" onclick="showPage('products'); return false;">查看全部产品</a>
        </div>
      </div>
    </section>

    <section class="care-cta">
      <div class="care-cta-inner fade-in">
        <h2 class="care-cta-title">立即享受 <em>ITO CARE</em> 服务</h2>
        <p class="care-cta-desc">扫描产品上的二维码完成专属身份绑定，即可享受全方位的服务保障<br>有效地域：大陆地区全量服务 · 港澳台及海外提供远程诊断+维修邮寄支持</p>
        <a href="#" class="care-cta-btn">
          前往 ITO 小程序
          <svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </section>
  </div>
'''

about_page = '''
  <div id="page-about" class="page">
    <div class="page-hero">
      <div class="page-hero-bg"></div>
      <div class="page-hero-content">
        <div class="page-hero-label">About ITO</div>
        <h1 class="page-hero-title">关于伊稻</h1>
      </div>
    </div>

    <section class="about-intro">
      <div class="about-intro-inner container">
        <div class="about-intro-sticky">
          <div class="section-label fade-in">Our Story</div>
          <h2 class="section-title fade-in">品牌故事</h2>
          <p class="section-subtitle fade-in">专注旅行箱包<br>打造每一次旅程的最佳伴侣</p>
        </div>
        <div>
          <p class="about-intro-text fade-in">伊稻（上海）商业有限公司（ITO）是一家专注于旅行箱包领域的品牌企业，总部位于上海。自创立以来，ITO 始终坚持以产品质量和消费者体验为核心，致力于打造让旅行者真正喜爱和信赖的旅行装备品牌。</p>
          <div class="about-intro-highlight fade-in">品牌是我们讲述故事、影响他人对我们看法、激发潜能的途径。</div>
          <p class="about-intro-text fade-in">ITO 的产品线涵盖行李箱、手提箱、服装箱、双肩背包及旅行收纳包等多个品类，满足现代旅行者在商务出行、休闲旅游及日常通勤等不同场景下的多元化需求。</p>
          <p class="about-intro-text fade-in">我们深信，一件好的旅行产品不仅要具备卓越的功能性，更要在设计美学和情感体验上打动用户。为此，ITO 在产品研发上持续投入，融合东西方设计美学，以简洁现代的外观和人性化的内构设计，为每一位用户带来愉悦的使用体验。</p>
          <p class="about-intro-text fade-in">未来，ITO 将继续深耕旅行箱包领域，以创新为驱动，以卓越为追求，持续推出更多令消费者满意的优质产品，成为千万旅行者最值得信赖的旅行品牌。</p>
        </div>
      </div>
    </section>

    <section class="mvv">
      <div class="mvv-inner">
        <div class="mvv-header">
          <div class="section-label fade-in">Mission · Vision · Values</div>
          <h2 class="section-title fade-in">愿景 · 使命 · 价值观</h2>
        </div>
        <div class="mvv-grid">
          <div class="mvv-card fade-in">
            <div class="mvv-en">Vision</div>
            <div class="mvv-cn">愿景 · Target</div>
            <div class="mvv-title">成为最值得信赖的旅行品牌</div>
            <div class="mvv-text">成为千万消费者最值得信赖的旅行品牌，在每一位旅行者心中建立起品质与信任的连接。</div>
          </div>
          <div class="mvv-card fade-in fade-in-delay-1">
            <div class="mvv-en">Mission</div>
            <div class="mvv-cn">使命 · Mission</div>
            <div class="mvv-title">为人们提供喜欢、好用的旅行产品</div>
            <div class="mvv-text">以消费者需求为导向，持续研发设计人们真正喜欢、实际好用的旅行产品，让每一次旅程更加美好。</div>
          </div>
          <div class="mvv-card fade-in fade-in-delay-2">
            <div class="mvv-en">Values</div>
            <div class="mvv-cn">价值观 · Core Value</div>
            <div class="mvv-title">客户导向 · 创新 · 追求卓越</div>
            <div class="mvv-text">以客户价值为工作标准，视创新为责任，永不满足于现状，不断超越自我，追求更高的工作成果。</div>
          </div>
        </div>
      </div>
    </section>

    <section class="values">
      <div class="values-inner">
        <div class="values-header">
          <div class="section-label fade-in">Core Values</div>
          <h2 class="section-title fade-in">核心价值观</h2>
        </div>
        <div class="values-list">
          <div class="value-item fade-in">
            <div class="value-num">01</div>
            <div class="value-title">客户导向 <small>Customer Focus</small></div>
            <div class="value-text">倾听客户，洞察市场；以客户价值为一切工作的依据和标准；努力学习客户服务的专业方法和工具；努力搜索满足客户需求的机会，将客户的每一个反馈都转化为产品进步的动力。</div>
          </div>
          <div class="value-item fade-in fade-in-delay-1">
            <div class="value-num">02</div>
            <div class="value-title">创新 <small>Innovation</small></div>
            <div class="value-text">不固步自封，不满足于现状，视创新为责任；积极尝试，及时总结调整，乐于分享交流；包容和鼓励创新，并提供尽可能的支持；钻研创新方法，努力提升创新能力。</div>
          </div>
          <div class="value-item fade-in fade-in-delay-2">
            <div class="value-num">03</div>
            <div class="value-title">追求卓越 <small>Pursuit of Excellence</small></div>
            <div class="value-text">不满足于现状，积极探索可能的机会；不断提升对自己的工作要求；不怕困难，不轻言放弃；团结和鼓励他人一起获得更高的工作成果，让卓越成为每个人的工作标准。</div>
          </div>
        </div>
      </div>
    </section>
  </div>
'''

products_page = f'''
  <div id="page-products" class="page">
    <div class="page-hero">
      <div class="page-hero-bg"></div>
      <div class="page-hero-content">
        <div class="page-hero-label">Products & Services</div>
        <h1 class="page-hero-title">产品服务</h1>
      </div>
    </div>

    <section class="products-intro">
      <div class="products-intro-inner container">
        <div>
          <div class="section-label fade-in">全品类旅行装备</div>
          <h2 class="section-title fade-in">为每一种<br>旅行方式<br>量身打造</h2>
          <p class="section-subtitle fade-in">行李箱、背包、旅行袋，ITO 覆盖您旅途中的所有装备需求。</p>
        </div>
        <div>
          <div class="products-filter">
            <button class="filter-btn active" onclick="filterProducts('all', this)">全部<span class="filter-cat-count">26</span></button>
            <button class="filter-btn" onclick="filterProducts('luggage', this)">箱类<span class="filter-cat-count">12</span></button>
            <button class="filter-btn" onclick="filterProducts('backpack', this)">背包<span class="filter-cat-count">10</span></button>
            <button class="filter-btn" onclick="filterProducts('bag', this)">旅行袋<span class="filter-cat-count">4</span></button>
          </div>
        </div>
      </div>
    </section>

    <section class="products-full-grid">
      <div class="products-full-grid-inner container">
        {product_cards_html}
      </div>
    </section>

    <section class="why-choose">
      <div class="why-choose-inner">
        <div class="why-choose-header">
          <div class="section-label fade-in">Why Choose ITO</div>
          <h2 class="section-title fade-in">选择 ITO 的理由</h2>
        </div>
        <div class="why-grid">
          <div class="why-item fade-in">
            <div class="why-item-num">01</div>
            <div class="why-item-content">
              <div class="why-item-title">专业品类深耕</div>
              <div class="why-item-text">ITO 专注旅行箱包领域，持续深耕产品研发，每一款产品都凝聚了对旅行场景的深刻理解与专业积累。</div>
            </div>
          </div>
          <div class="why-item fade-in fade-in-delay-1">
            <div class="why-item-num">02</div>
            <div class="why-item-content">
              <div class="why-item-title">严苛品质管控</div>
              <div class="why-item-text">从材料采购到成品出厂，每个环节都经历严格的品质检测，camira面料经12,000,000次耐磨认证，用数据和标准守护每一位消费者的权益。</div>
            </div>
          </div>
          <div class="why-item fade-in fade-in-delay-2">
            <div class="why-item-num">03</div>
            <div class="why-item-content">
              <div class="why-item-title">贴心用户服务</div>
              <div class="why-item-text">完善的售前咨询与售后服务体系，让每一位选择 ITO 的消费者都能获得持续的品牌关怀。</div>
            </div>
          </div>
          <div class="why-item fade-in fade-in-delay-3">
            <div class="why-item-num">04</div>
            <div class="why-item-content">
              <div class="why-item-title">持续创新迭代</div>
              <div class="why-item-text">积极拥抱新材料、新工艺与新设计理念，PEBBLE圆锁、camira面料等创新应用，不断推出满足市场需求的创新产品。</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
'''

contact_page = '''
  <div id="page-contact" class="page">
    <div class="page-hero">
      <div class="page-hero-bg"></div>
      <div class="page-hero-content">
        <div class="page-hero-label">Contact Us</div>
        <h1 class="page-hero-title">联系我们</h1>
      </div>
    </div>

    <section class="contact-section">
      <div class="contact-inner container">
        <div>
          <div class="contact-info-label fade-in">Get In Touch</div>
          <h2 class="contact-info-title fade-in">期待与您<br>建立联系</h2>
          <p class="contact-info-text fade-in">无论是产品咨询、商务合作还是品牌合作，我们都欢迎您与我们取得联系。</p>
          <div class="contact-details">
            <div class="contact-detail-item fade-in">
              <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
              <div><div class="contact-detail-label">Address</div><div class="contact-detail-value">上海市，伊稻（上海）商业有限公司</div></div>
            </div>
            <div class="contact-detail-item fade-in fade-in-delay-1">
              <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 1.18h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 15z"/></svg></div>
              <div><div class="contact-detail-label">Phone</div><div class="contact-detail-value">请通过官网表单联系我们</div></div>
            </div>
            <div class="contact-detail-item fade-in fade-in-delay-2">
              <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
              <div><div class="contact-detail-label">Email</div><div class="contact-detail-value">business@ito-brand.com</div></div>
            </div>
            <div class="contact-detail-item fade-in fade-in-delay-3">
              <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
              <div><div class="contact-detail-label">Business Hours</div><div class="contact-detail-value">周一至周五  09:00 - 18:00</div></div>
            </div>
          </div>
        </div>

        <div class="fade-in">
          <div class="contact-form-title">发送消息</div>
          <form id="contactForm" onsubmit="submitForm(event)">
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">姓名 *</label>
                <input class="form-input" type="text" placeholder="您的姓名" required>
              </div>
              <div class="form-group">
                <label class="form-label">公司</label>
                <input class="form-input" type="text" placeholder="公司名称（选填）">
              </div>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">联系电话 *</label>
                <input class="form-input" type="tel" placeholder="您的联系电话" required>
              </div>
              <div class="form-group">
                <label class="form-label">电子邮箱</label>
                <input class="form-input" type="email" placeholder="your@email.com">
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">咨询类型 *</label>
              <select class="form-select" required>
                <option value="">请选择咨询类型</option>
                <option>产品咨询</option>
                <option>经销合作</option>
                <option>商务合作</option>
                <option>品牌合作</option>
                <option>其他</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">留言内容 *</label>
              <textarea class="form-textarea" placeholder="请详细描述您的需求或问题..." required></textarea>
            </div>
            <button type="submit" class="form-submit">提交留言 →</button>
          </form>
          <div class="form-success" id="formSuccess">
            <div class="form-success-icon"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
            <div class="form-success-title">留言提交成功！</div>
            <div class="form-success-text">感谢您的联系，我们将在 1-2 个工作日内与您取得联系。</div>
          </div>
        </div>
      </div>
    </section>

    <section class="map-section" style="padding:0 5% 100px;background:var(--color-white);">
      <div style="max-width:1200px;margin:0 auto;">
        <div style="height:400px;background:var(--color-gray-light);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;">
          <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,0.04) 1px, transparent 1px),linear-gradient(90deg, rgba(0,0,0,0.04) 1px, transparent 1px);background-size:40px 40px;"></div>
          <div style="position:relative;z-index:1;text-align:center;">
            <div style="width:16px;height:16px;background:var(--color-blue);border-radius:50%;margin:0 auto 8px;position:relative;"><div style="position:absolute;inset:-6px;border:2px solid rgba(0,117,179,0.3);border-radius:50%;animation:ping 2s ease-in-out infinite;"></div></div>
            <div style="font-size:13px;font-weight:600;background:var(--color-white);padding:8px 16px;box-shadow:0 4px 20px rgba(0,0,0,0.1);">伊稻（上海）商业有限公司</div>
          </div>
        </div>
      </div>
    </section>
  </div>
'''

footer = '''
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div>
          <div class="footer-logo">
            <div class="footer-logo-mark"><span>ITO</span></div>
            <div class="footer-brand-name">ITO 伊稻</div>
          </div>
          <p class="footer-brand-text">伊稻（上海）商业有限公司<br>专注旅行箱包，为每一次旅程提供最佳装备。</p>
          <p class="footer-brand-text">行李箱 · 手提箱 · 服装箱<br>双肩背包 · 旅行收纳包</p>
        </div>
        <div>
          <div class="footer-col-title">导航</div>
          <ul class="footer-links">
            <li><a href="#" onclick="showPage('home'); return false;">首页</a></li>
            <li><a href="#" onclick="showPage('products'); return false;">产品中心</a></li>
            <li><a href="ito-care.html">ITO CARE</a></li>
            <li><a href="#" onclick="showPage('about'); return false;">关于我们</a></li>
            <li><a href="#" onclick="showPage('contact'); return false;">联系我们</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">产品系列</div>
          <ul class="footer-links">
            <li><a href="#" onclick="showPage('products'); return false;">行李箱</a></li>
            <li><a href="#" onclick="showPage('products'); return false;">手提箱</a></li>
            <li><a href="#" onclick="showPage('products'); return false;">服装箱</a></li>
            <li><a href="#" onclick="showPage('products'); return false;">双肩背包</a></li>
            <li><a href="#" onclick="showPage('products'); return false;">旅行收纳包</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">联系方式</div>
          <ul class="footer-links">
            <li><a href="#">上海总部</a></li>
            <li><a href="mailto:business@ito-brand.com">business@ito-brand.com</a></li>
            <li><a href="#">工作日 09:00-18:00</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-copyright">© 2026 伊稻（上海）商业有限公司 ITO Brand. All Rights Reserved.</div>
        <div class="footer-icp">沪ICP备XXXXXXXXX号</div>
      </div>
    </div>
  </footer>

  <script>
    function showPage(pageId) {
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.getElementById('page-' + pageId).classList.add('active');
      document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
      const navEl = document.getElementById('nav-' + pageId);
      if (navEl) navEl.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(() => { observeElements(); }, 100);
    }

    window.addEventListener('scroll', () => {
      document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 20);
    });

    function toggleMobileMenu() {
      document.getElementById('mobileMenu').classList.toggle('open');
    }

    function observeElements() {
      const elements = document.querySelectorAll('.fade-in:not(.visible)');
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
      elements.forEach(el => observer.observe(el));
    }

    document.addEventListener('DOMContentLoaded', () => { observeElements(); });
    observeElements();

    function filterProducts(cat, btn) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.product-full-card').forEach(card => {
        if (cat === 'all' || card.dataset.cat === cat) {
          card.style.display = '';
          setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(20px)';
          setTimeout(() => { card.style.display = 'none'; }, 350);
        }
      });
    }

    function submitForm(e) {
      e.preventDefault();
      const form = document.getElementById('contactForm');
      const success = document.getElementById('formSuccess');
      form.style.opacity = '0';
      form.style.transform = 'translateY(20px)';
      setTimeout(() => {
        form.style.display = 'none';
        success.classList.add('show');
      }, 400);
    }

    function toggleDetail(btn) {
      const panel = btn.nextElementSibling;
      const isOpen = btn.classList.contains('open');
      // Close all
      document.querySelectorAll('.product-detail-toggle').forEach(b => {
        b.classList.remove('open');
        b.querySelector('.toggle-icon').textContent = '+';
        b.querySelector('.toggle-text').textContent = '查看详细参数';
      });
      document.querySelectorAll('.product-detail-panel').forEach(p => p.classList.remove('open'));
      // Open clicked if was closed
      if (!isOpen) {
        btn.classList.add('open');
        btn.querySelector('.toggle-icon').textContent = '−';
        btn.querySelector('.toggle-text').textContent = '收起详细参数';
        panel.classList.add('open');
      }
    }
  </script>
'''

# Now assemble full HTML
html_body = nav + home_page + products_page + care_page + about_page + contact_page + footer

# Write full HTML with complete structure
with open('d:/ITO产品手册/website/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_HEAD + html_body + HTML_TAIL)

print('Done! Products:', len(products))
print('HTML file generated with complete structure.')
