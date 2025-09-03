import yagmail
yag = yagmail.SMTP("baaby.dudu@gmail.com", "YOURPASSWORD")

ITEM_URL = "https://www.amazon.com/OLEVS-Business-Stainless-Luminous-Waterproof/dp/B0CY233WHW/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.7c01ce36-e5c1-4582-8c84-1c861e19c36d%3Aamzn1.sym.7c01ce36-e5c1-4582-8c84-1c861e19c36d&crid=238MASK99EB1U&cv_ct_cx=watches%2Bfor%2Bmen&keywords=watches%2Bfor%2Bmen&pd_rd_i=B0CY233WHW&pd_rd_r=ae0928f5-54c1-4943-85d7-29eeb826a30a&pd_rd_w=E5Lqe&pd_rd_wg=FzQMl&pf_rd_p=7c01ce36-e5c1-4582-8c84-1c861e19c36d&pf_rd_r=W2TMVK0YWGQ2FYS43QA9&qid=1735029437&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=watch%2Caps%2C1468&sr=1-1-41e47a6d-5f35-4db4-b071-6cb1fce345df-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "PHPSESSID=f1e47fd303618c2221ed2325260c9847; _ga=GA1.2.1094573868.1735029578; _gid=GA1.2.617763386.1735029578; _ga_VL41109FEB=GS1.2.1735029580.1.0.1735029580.0.0.0"
}
